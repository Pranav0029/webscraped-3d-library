from django.http import HttpResponse
from .models import Student_Login, CartItem
from django.shortcuts import render, get_object_or_404
from myapp.models import Book

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect, get_object_or_404



def first(request):
    message = None
    scraped_news = []

    if request.method == "POST":
        action = request.POST.get("action")
        book_id = request.POST.get("book_id")

        if action == "add_to_cart" and request.user.is_authenticated:
            book = get_object_or_404(Book, id=book_id)
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                book=book
            )
            return redirect('first')

    query = request.GET.get("q")
    if query:
        books = Book.objects.filter(title__icontains=query)
        if not books.exists():
            message = f"No results found for '{query}'."
    else:
        books = Book.objects.all()

    try:
        url = "https://www.hindustantimes.com"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.find_all('div', class_='cartHolder')

        for article in articles[:10]:  # Sirf top 10 news ke liye
            title_tag = article.find('h2', class_='hdg3')
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = title_tag.find('a')['href']
                if not link.startswith('http'):
                    link = url + link

                scraped_news.append({
                    'title': title,
                    'link': link
                })
    except Exception as e:
        print(f"Scraping Error: {e}")

    return render(request, 'myapp1/first.html', {
        'books': books,
        'message': message,
        'scraped_news': scraped_news
    })


def home(request):
    return HttpResponse("hello to myaapp1 ...")


from django.shortcuts import render, redirect
from django.utils import timezone
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def stu_log(request):
    errors = {}
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        department = request.POST.get('department', '').strip()
        lib_card_no = request.POST.get('lib_card_no', '').strip()
        photo = request.FILES.get('photo')

        # Validation rules:

        # Name: required, min 2 chars, max 100 chars, only letters and spaces
        if not name:
            errors['name'] = "Name is required."
        elif len(name) < 2:
            errors['name'] = "Name must be at least 2 characters."
        elif len(name) > 100:
            errors['name'] = "Name can't exceed 100 characters."
        elif not re.match(r'^[A-Za-z\s]+$', name):
            errors['name'] = "Name can only contain letters and spaces."

        # Email: required, valid email format
        if not email:
            errors['email'] = "Email is required."
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors['email'] = "Enter a valid email address."

        # Department: required, max 100 chars
        if not department:
            errors['department'] = "Department is required."
        elif len(department) > 100:
            errors['department'] = "Department can't exceed 100 characters."

        # Library Card No: required, max 50 chars, alphanumeric only
        if not lib_card_no:
            errors['lib_card_no'] = "Library Card Number is required."
        elif len(lib_card_no) > 50:
            errors['lib_card_no'] = "Library Card Number can't exceed 50 characters."
        elif not re.match(r'^[A-Za-z0-9]+$', lib_card_no):
            errors['lib_card_no'] = "Library Card Number must be alphanumeric."

        # Photo: required, only images (check content_type)
        if not photo:
            errors['photo'] = "Photo is required."
        else:
            if not photo.content_type.startswith('image/'):
                errors['photo'] = "Uploaded file must be an image."

        if not errors:
            Student_Login.objects.create(
                name=name,
                email=email,
                department=department,
                lib_card_no=lib_card_no,
                photo=photo,
                login_time=timezone.now()
            )
            return redirect("http://127.0.0.1:8000/myapp1/first")

    else:
        errors = {}

    return render(request, 'myapp1/stu_log.html', {'errors': errors})



def lab_cat(request):
    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'myapp1/lab_cat.html', context)
