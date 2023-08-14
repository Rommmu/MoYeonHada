from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # home
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup_end/', views.signup_end, name='signup_end'),

    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # path('profile/', views.profile_view, name='profile'),
    # path('profile/update/', views.profile_update_view, name='profile_update'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)