from django.test import TestCase

# Create your tests here.

from ..models import Author, Genre, Book, BookInstance


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')


class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(name='fantastic')

    def test_genre_name(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_genre_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Book.objects.create(title='Lord', summary='abracadabra')

    def test_title_label(self):
        title = Book.objects.get(id=1)
        field_label = title._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max(self):
        title = Book.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_summary_label(self):
        summary = Book.objects.get(id=1)
        field_label = summary._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_summary_max(self):
        summary = Book.objects.get(id=1)
        max_length = summary._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1')


class BookInstanceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BookInstance.objects.create(imprint='burka')

    def test_id_label(self):
        id_field = BookInstance.objects.get(imprint='burka')
        field_label = id_field._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'id')

    def test_id_length(self):
        id_field = BookInstance.objects.get(imprint='burka')
        max_length = id_field._meta.get_field('id').max_length
        self.assertEquals(max_length, 32)
