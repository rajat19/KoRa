from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django_countries.widgets import CountrySelectWidget
from .models import Book, BookSeries, BookAuthor
from .forms import BookForm, UploadForm, ReviewForm
from common.helper import StaticTemplates
from common.constants import Constants, BookConstants

decorators = [login_required]


class IndexView(generic.ListView):
    template_name = StaticTemplates.view(Constants.index_template_name)
    context_object_name = BookConstants.books_context_name

    def get_queryset(self):
        return Book.objects.all().order_by(Constants.title)


class BookView(generic.DetailView):
    model = Book
    template_name = StaticTemplates.view(BookConstants.book_template_name)


@method_decorator(login_required, name="dispatch")
class BookCreate(CreateView):
    form_class = BookForm
    template_name = StaticTemplates.create(BookConstants.book_template_name)


@method_decorator(login_required, name="dispatch")
class BookUpdate(UpdateView):
    model = Book
    template_name = StaticTemplates.update(BookConstants.book_template_name)
    fields = Book.db_fields()


@method_decorator(login_required, name="dispatch")
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:index')


@method_decorator(login_required, name="dispatch")
class BookUpload(View):
    form_class = UploadForm
    template_name = StaticTemplates.create(Constants.upload_template_name)

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            upload = form.save(commit=False)
            upload.uploader = request.user
            upload.save()

        return render(request, self.template_name, {'form': form})


class SeriesList(generic.ListView):
    template_name = StaticTemplates.view(BookConstants.series_list_template_name)
    context_object_name = BookConstants.series_context_name

    def get_queryset(self):
        return BookSeries.objects.all().order_by(Constants.title)


class SeriesView(generic.DetailView):
    model = BookSeries
    template_name = StaticTemplates.view(BookConstants.series_template_name)


@method_decorator(login_required, name="dispatch")
class SeriesCreate(CreateView):
    model = BookSeries
    fields = BookSeries.db_fields()
    template_name = StaticTemplates.create(BookConstants.series_template_name)


class SearchEverything(generic.ListView):
    template_name = StaticTemplates.view(BookConstants.series_template_name)
    context_object_name = Constants.data_context_name

    def get_queryset(self):
        search_string = self.request.GET.get('search') or '-created'
        # query_string = super(SearchEverything, self).get_queryset()
        books = Book.objects.filter(title__contains=search_string)
        authors = BookAuthor.objects.filter(name__contains=search_string)
        series = BookSeries.objects.filter(title__contains=search_string)
        data = {
            'books': books,
            'authors': authors,
            'series': series,
            'search_text': search_string
        }
        return data


class AuthorsView(generic.ListView):
    template_name = StaticTemplates.view(BookConstants.authors_template_name)
    context_object_name = BookConstants.author_context_name

    def get_queryset(self):
        return BookAuthor.objects.all().order_by(Constants.name)


class AuthorView(generic.DetailView):
    model = BookAuthor
    template_name = StaticTemplates.view(BookConstants.author_template_name)


@method_decorator(login_required, name="dispatch")
class AuthorCreate(CreateView):
    model = BookAuthor
    fields = BookAuthor.db_fields()
    widgets = {'country': CountrySelectWidget()}
    template_name = StaticTemplates.create(BookConstants.author_template_name)


@method_decorator(login_required, name='dispatch')
class ReviewCreate(View):
    form_class = ReviewForm
    template_name = StaticTemplates.view(BookConstants.author_template_name)

    def get(self, request):
        pass

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.book = form.cleaned_data['book']
            print(review)
            review.save()

        else:
            print(request.user)
            print('error in form')
            test_template = StaticTemplates.view(Constants.test_template_name)
            return render(request, test_template, {'errors': form.errors})

        return redirect('books:detail', slug=form.cleaned_data['book'].slug)
