from django.contrib import admin
from django.urls import path
from events import views
from django.conf import settings
from django.conf.urls.static import static
from events.admin import researcher_site



app_name = 'events'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('admin/', views.AdminPage, name='admin'),
    # URL pattern for approving user creation with activation checkbox
    path('approve/<str:token>/', views.approve_user_creation, name='approve_user_creation'),
    path('delete/<int:user_creation_id>/', views.delete_user_creation, name='delete_user_creation'),
    path('signup/confirmation/', views.SignupConfirmationPage, name='signup_confirmation'),
    path('', views.index, name='index'),
    path('event.html', views.PostList.as_view(), name='event'),
    path('event/<int:pk>/', views.PostDetail.as_view(), name='event_details'),
    path('research/', researcher_site.urls),
    path('publications/', views.publications, name='publications'),
    path('generate_bibtex/<int:article_id>/', views.generate_bibtex, name='generate_bibtex'),
    path('bibtex/', views.bibtex_view, name='bibtex'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


