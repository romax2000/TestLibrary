from django import forms
from sys import float_info
from app.models import User, Book


class NewUserForm(forms.Form):
    Years = list(range(2013, 1930, -1))

    full_name = forms.CharField(max_length=200, min_length=5)
    middle_name = forms.CharField(max_length=100, min_length=5)
    birth_day = forms.DateField(widget=forms.SelectDateWidget(years=Years))
    phone = forms.CharField(max_length=20, min_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'full_name',
            'middle_name',
            'birth_day',
            'phone',
            'email'

        ]

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, *kwargs)
        self.fields['full_name'].label = 'Имя и фамилия'
        self.fields['middle_name'].label = 'Отчество'
        self.fields['birth_day'].label = 'Дата рождения'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['phone'].initial = '+375()--'
        self.fields['phone'].help_text = 'Формат: +375(ХХ)ХХХ-ХХ-ХХ'


class EditUserForm(forms.Form):
    Years = list(range(2013, 1930, -1))

    full_name = forms.CharField(max_length=200, min_length=5)
    middle_name = forms.CharField(max_length=100, min_length=5)
    birth_day = forms.DateField(widget=forms.SelectDateWidget(years=Years))
    phone = forms.CharField(max_length=20, min_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'full_name',
            'middle_name',
            'birth_day',
            'phone',
            'email'

        ]

    def __init__(self, user, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, *kwargs)
        self.fields['full_name'].label = 'Имя и фамилия'
        self.fields['full_name'].initial = user.full_name
        self.fields['middle_name'].label = 'Отчество'
        self.fields['middle_name'].initial = user.middle_name
        self.fields['birth_day'].label = 'Дата рождения'
        self.fields['birth_day'].initial = user.birth_day
        self.fields['phone'].label = 'Номер телефона'
        self.fields['phone'].initial = user.phone
        self.fields['phone'].help_text = 'Формат: +375(ХХ)ХХХ-ХХ-ХХ'
        self.fields['email'].initial = user.email


'''
        #Дополнительные проверки
        def clean(self):
                full_name = self.cleaned_data['full_name']
                birth_day = self.cleaned_data['birth_day']

'''


class NewBookForm(forms.Form):
    book_name = forms.CharField(max_length=200, min_length=1)
    author_full_name = forms.CharField(max_length=200, min_length=5)
    year = forms.IntegerField(max_value=2020, min_value=1)
    cost = forms.FloatField(max_value=float_info.max, min_value=float_info.min)
    pages = forms.IntegerField(min_value=1, max_value=23675)

    class Meta:
        model = Book
        fields = [
            'book_name',
            'author_full_name',
            'year',
            'cost',
            'pages'
        ]

    def __init__(self, *args, **kwargs):
        super(NewBookForm, self).__init__(*args, *kwargs)
        self.fields['book_name'].label = 'Название книги'
        self.fields['author_full_name'].label = 'Автор'
        self.fields['year'].label = 'Год издания'
        self.fields['cost'].label = 'Цена'
        self.fields['pages'].label = 'Страниц'


class EditBookForm(forms.Form):
    book_name = forms.CharField(max_length=200, min_length=1)
    author_full_name = forms.CharField(max_length=200, min_length=5)
    year = forms.IntegerField(max_value=2020, min_value=1)
    cost = forms.FloatField(max_value=float_info.max, min_value=float_info.min)
    pages = forms.IntegerField(min_value=1, max_value=23675)

    class Meta:
        model = Book
        fields = [
            'book_name',
            'author_full_name',
            'year',
            'cost',
            'pages'
        ]

    def __init__(self, book, *args, **kwargs):
        super(EditBookForm, self).__init__(*args, *kwargs)
        self.fields['book_name'].label = 'Название книги'
        self.fields['book_name'].initial = book.book_name
        self.fields['author_full_name'].label = 'Автор'
        self.fields['author_full_name'].initial = book.author_full_name
        self.fields['year'].label = 'Год издания'
        self.fields['year'].initial = book.year
        self.fields['cost'].label = 'Цена'
        self.fields['cost'].initial = book.cost
        self.fields['pages'].label = 'Страниц'
        self.fields['pages'].initial = book.pages
