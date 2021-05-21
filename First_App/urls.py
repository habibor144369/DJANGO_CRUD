from django.urls import path
from . import views 

app_name = "First_App"

urlpatterns = [
    path('', views.Index, name = 'index'),  
    path('?P\w+Add_Musicianw+[\w-]/', views.Musician_Form, name='Add_Musician'),
    path('?P\w+Add_Albumw+[\w-]/', views.Album_Form, name='Add_Album'),  
    path('Album_List/<int:artist_id>/?P\w+[\w-]+?/Musician_Name:-/<str:username>/', views.Album_List, name='album_list' ),
    path('?P\w+Edit_Artist+[\w-]/Album_List/<int:artist_id>/Edit_Musician_Name:-/<str:username>/', views.Edit_Artist, name='Edit_Artist'),  
    path('?P\w+Edit_Album+[\w-]/Album_List/<int:album_id>/Edit_Album_List:-/<str:username>/', views.Edit_Album, name='Edit_Album'),
    path('?P\w+Deleted_Album+[\w-]/<int:album_id>/', views.Delete_Album, name='Delete_Album'),
    path('?P\w+Delete_Musician+[\w-]/<int:artist_id>/', views.Delete_Musician, name='Delete_Musician'),
]