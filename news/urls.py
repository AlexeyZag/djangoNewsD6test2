from django.urls import path
from.views import AuthorsList, AuthorDetail, PostList, PostDetail, SearchList, SearchDetail, AddView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name= 'post_detail'),
    path('authors', AuthorsList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
    path('search', SearchList.as_view(), name= 'search'),
    path('search/<int:pk>', SearchDetail.as_view(), name= 'search_detail'),
    path('add', AddView.as_view()),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name= 'post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name= 'post_delete'),

]