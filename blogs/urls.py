from django.conf.urls import url
from . import views
from django.urls import path,include

app_name='blogs'

urlpatterns=[
    path("post/create/",views.create_view,name='create'),
    path('post/',views.home),
    path('view/results/like/',views.result_like),
    path('view/results/dislike/',views.result_dislike),
    path('view/',views.show_post),

    ]
