from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.login, name="login"),
    path('register/',views.register, name="register"),
    path('a/',views.admin_home, name="admin_home"),
    path('a/students/',views.astudentlist, name="students"),
    path('a/students/new/',views.astudentnew, name="students_new"),
    path('a/students/new/student',views.funcStudentNew, name="func_students_new"),
    path('a/students/<int:pk>/edit/',views.astudentedit, name="students_edit"),
    path('a/students/<int:pk>/delete/',views.astudentdelete, name="students_delete"),
    path('a/lesson/',views.alessonList, name="lesson"),
    path('a/assessments/',views.aAssessments, name="assessments"),
    path('a/achievements/',views.aAchievements, name="achievements"),
    path('a/reports/',views.aReports, name="reports"),
    path('a/logs/',views.aLogs, name="logs"),

    path('a/viewLesson/',views.aOpenLesson, name="viewLesson"),
    path('a/lesson/lessonEditor/',views.aLessonEditor, name="edit-lesson"),

    path('a/profile/',views.profile, name="profile"),




    # path('u/',views.use)
    # path('admin_add_student/',views.admin_add_student, name="admin_add_student"),
    # path('/',views.admin_save_student, name="admin_save_student"),
    # path('<int:id>/update/',views.admin_update_student,name="admin_update_student"),
    # path('<int:id>/delete/',views.funcStudentDelete,name="funcStudentDelete")
]
