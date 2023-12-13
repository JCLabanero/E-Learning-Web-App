from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('dashboard/',views.dashboard, name="dashboard"),

    # Account CRUD
    path('login/submit/',views.login_submit, name="login_submit"),
    path('register/',views.register, name="register"),
    path('a/profile/id=<int:id>/',views.profile, name="profile"),
    path('a/profile/id=<int:id>/',views.deleteProfile, name="delete-profile"),


    path('a/',views.admin_home, name="admin_home"),
    path('a/students/',views.astudentlist, name="students"),
    path('a/students/new/',views.astudentnew, name="students_new"),
    path('a/students/new/student',views.funcStudentNew, name="func_students_new"),
    path('a/students/<int:pk>/edit/',views.astudentedit, name="students_edit"),
    path('a/students/<int:pk>/delete/',views.astudentdelete, name="students_delete"),
    path('a/lesson/',views.funcLessonList, name="lesson"),
    path('a/achievements/',views.aAchievements, name="achievements"),
    path('a/reports/',views.aReports, name="reports"),
    path('a/logs/',views.aLogs, name="logs"),

    path('a/lesson/id=<int:id>/',views.funcLoadLesson, name="viewLesson"),

    # Lesson CRUD
    path('a/unit-<int:unit>/lesson/create/',views.createLesson, name="create-lesson"),
    path('a/lesson/id=<int:id>/edit/',views.updateLesson, name="edit-lesson"), #if request method is not POST then load a ediatble lesson
    path('a/lesson/id=<int:id>/update/',views.updateLesson, name="update-lesson"), #if request method is POST the update Lesson
    path('a/lesson/<int:id>/delete/',views.deleteLesson, name="delete-lesson"),
    path('a/unit/<int:unit>/delete/',views.deleteUnit, name="delete-unit"),

    path('a/assessments/',views.aAssessments, name="assessments"),
    path('a/assessments/<str:type>/create/',views.assessmentCreate, name="create-assessment"),
    path('a/assessments/<str:type>/<int:id>/edit/',views.assessmentEdit, name="edit-assessment"),
    path('a/assessments/<int:id>/delete',views.assessmentDelete, name="delete-assessment"),
    path('a/assessments/submit/',views.assessmentCreate, name="add-quiz"),

    path('a/assessments/<str:type>/<int:id>/take/',views.studentTakeQuiz, name='take-assessment'),
    path('a/assessments/<str:type>/<int:id>/result/',views.result, name='score')


    

    # path('u/',views.use)
    # path('admin_add_student/',views.admin_add_student, name="admin_add_student"),
    # path('/',views.admin_save_student, name="admin_save_student"),
    # path('<int:id>/update/',views.admin_update_student,name="admin_update_student"),
    # path('<int:id>/delete/',views.funcStudentDelete,name="funcStudentDelete")
]
