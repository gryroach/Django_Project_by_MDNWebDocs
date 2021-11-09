from django.shortcuts import render
from django.views import generic
from .models import Author, Book, BookInstance, Language, Genre
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .forms import RenewBookForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.
    num_genres = Genre.objects.count()
    num_lang = Language.objects.count()
    num_book_war = Book.objects.filter(title__icontains='война').count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_genres': num_genres, 'num_book_war': num_book_war, 'num_lang': num_lang,
                 'num_visit': num_visits},
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class AllBorrowedBooks(PermissionRequiredMixin, generic.ListView):
    """
    Generic all borrowed book librarian
    """
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/all_borrowed_books.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)

    # Если данный запрос типа POST, тогда
    if request.method == 'POST':

        # Создаём экземпляр формы и заполняем данными из запроса (связывание, binding):
        form = RenewBookForm(request.POST)

        # Проверка валидности данных формы:
        if form.is_valid():
            # Обработка данных из form.cleaned_data
            # (здесь мы просто присваиваем их полю due_back)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # Переход по адресу 'all-borrowed':
            return HttpResponseRedirect(reverse('all-borrowed-books'))

    # Если это GET (или какой-либо ещё), создать форму по умолчанию.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date, })

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst': book_inst})


class AuthorCreate(CreateView, PermissionRequiredMixin):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '12/10/2016', }
    permission_required = 'catalog.can_change'


class AuthorUpdate(UpdateView, PermissionRequiredMixin):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', ]
    permission_required = 'catalog.can_change'


class AuthorDelete(DeleteView, PermissionRequiredMixin):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_change'


class BookCreate(CreateView, PermissionRequiredMixin):
    model = Book
    fields = '__all__'
    initial = {'language': 'русский'}
    permission_required = 'catalog.can_change'


class BookUpdate(UpdateView, PermissionRequiredMixin):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.can_change'


class BookDelete(DeleteView, PermissionRequiredMixin):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.can_change'
