from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.login, name="login"),
    path('register/',views.register, name="register"),
    path('admin_home/',views.admin_home, name="admin_home"),
    # path('admin_add_student/',views.admin_add_student, name="admin_add_student"),
    # path('/',views.admin_save_student, name="admin_save_student"),
    # path('<int:id>/update/',views.admin_update_student,name="admin_update_student"),
    # path('<int:id>/delete/',views.funcStudentDelete,name="funcStudentDelete")
]
