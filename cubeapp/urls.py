from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('view/<int:pk>/', views.VideoView.as_view(), name='view'),
    path('comment/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    path('upload/', views.upload, name='upload'),
    path('view/<int:pk>/like', views.like, name='like'),
    path('view/<int:pk>/dislike', views.dislike, name='dislike')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
