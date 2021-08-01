from django.urls import path
from blog.views import PostList, UserCreate, LoginView, PostDetailAPIView, CategoriaList,CategoriaDetailAPIView, TagsCisco, TagsPython

urlpatterns = [
    path('v1/post/', PostList.as_view(),name='post_list' ),
    path('v1/postdetail/<slug:slug>', PostDetailAPIView.as_view(),name='post_detail' ),
    path('v1/usuarios/', UserCreate.as_view(),name='usuario_crear' ),

    path('v1/categorias/cisco', TagsCisco.as_view(),name='categoria_list_Cisco' ),
    path('v1/categorias/python', TagsPython.as_view(),name='categoria_list_Python' ),
    ]
