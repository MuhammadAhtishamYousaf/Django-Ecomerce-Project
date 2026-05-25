from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("allah/", views.allah),
    path(
        "courses/<courseid>", views.course_details
    ),  # int, str, slug, not know then leave empty
    path(route="about.html", view=views.about, name="About"),
    path("contact.html", views.contact, name="Contact"),
    path("blog.html", views.blog, name="Blog"),
    path("shop.html", views.shop, name="Shop"),
    path("submit.html", views.submit, name="Submit"),
    path("signup.html", views.signup, name="Signup"),
    path("login", views.login_form, name="login"),
    path("calculator.html", views.calculator),
    path("even_odd.html", views.even_odd),
    path("marksheet.html", views.marksheet),
    path("blog/<blog_slug>", views.blog_detail, name="blog"),
    # path ('shop/<title>',views.search),
    path("forgot_password.html", views.forgot_password, name="forgot_password"),
    path("form_testing", views.form_testing, name="Form_Testing"),
]
