from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('culture_g/', views.culture_g, name='culture_g'),
    path('fmp/', views.fmp, name='fmp'),
    path('mode_image/', views.mode_image, name='mode_image'),
    path('mode_image_inverse/', views.mode_image_inverse, name='mode_image_inverse'),
    path('mode_cri/', views.mode_cri, name='mode_cri'),
    path('lecon_du_jour/', views.lecon_du_jour, name='lecon_du_jour'),
]
