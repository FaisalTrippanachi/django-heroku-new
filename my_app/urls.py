from django.urls import path,include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('my_app.urls'))
    path('',views.testfun,name="home"),
    path('index',views.fnhome,name="index")
]