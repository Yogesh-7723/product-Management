from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),
    path("signup/",views.signup),
    path("ragistration/",views.ragistration),
    path("Login/",views.Login),
    path("dashboard/",views.dashboard),
    path("product/",views.product),
    path("view_update/",views.view_update),
    path("delete/<int:qk>/",views.delete ,name="delete"),
    path("update/<int:uid>/",views.updateuser,name='update'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

