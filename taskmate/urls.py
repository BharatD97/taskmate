from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_app_views
from users_app import views as users_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_app_views.index, name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('blog/', todolist_app_views.blog, name='blog'),
    path('about/', todolist_app_views.about, name='about'),
    path('contact/', todolist_app_views.contact, name='contact'),
]
