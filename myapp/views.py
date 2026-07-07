from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import Book



def home(request):
    messages=" "
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        link = request.POST.get('link')
        published_year = request.POST.get('published_year')
        category = request.POST.get('category')
        cover_image = request.FILES.get('cover_image')

        # Basic validation could be added here if needed

        Book.objects.create(
            title=title,
            author=author,
            link=link,
            published_year=int(published_year),
            category=category,
            cover_image=cover_image
        )

        messages = f'Book "{title}" added successfully!'

    # Dynamic counts
    total_books = Book.objects.count()
    total_members = Student_Login.objects.count()
    recent_books = Book.objects.order_by('-id')[:4]

    return render(request, 'myapp/AA1.html', {
        "message": messages,
        "total_books": total_books,
        "total_members": total_members,
        "recent_books": recent_books,
    })




def lib_log(request):
    message = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'Pass123':

            return redirect('http://127.0.0.1:8000/myapp/')

        else:
            message = '❌ Invalid username or password.'

    return render(request, 'myapp/lib_log.html', {'message': message})


from myapp1.models import Student_Login

def members(request):

    students = Student_Login.objects.all().order_by('-login_time')

    return render(request, "myapp/members.html", {'students': students})

from django.shortcuts import render
from myapp1.models import CartItem
from django.contrib.auth.models import User


def report(request):
    # Summary counts
    total_books = Book.objects.count()
    total_members = Student_Login.objects.count()
    total_cart_items = CartItem.objects.count()

    # Table data:
    #  Table 1: list of recent members
    members = Student_Login.objects.order_by('-login_time')[:10]
    #  Table 2: list of latest books
    recent_books = Book.objects.order_by('-id')[:10]
    #  Table 3: top users by cart items
    top_users = User.objects.all().order_by('id')[:10]  # placeholder

    # Graph data 1: Books by category
    cat_labels = list(Book.objects.values_list('category', flat=True).distinct())
    cat_counts = [ Book.objects.filter(category=cat).count() for cat in cat_labels ]

    # Graph data 2: Cart items per user (top 5)
    users = User.objects.all().order_by('-id')[:5]
    user_labels = [ u.username for u in users ]
    user_counts = [ CartItem.objects.filter(user=u).count() for u in users ]

    context = {
        'total_books': total_books,
        'total_members': total_members,
        'total_cart_items': total_cart_items,
        'members': members,
        'recent_books': recent_books,
        'top_users': zip(user_labels, user_counts),
        'cat_labels': cat_labels,
        'cat_counts': cat_counts,
        'user_labels': user_labels,
        'user_counts': user_counts,
    }
    return render(request, 'myapp/report.html', context)
