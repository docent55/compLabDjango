from django.urls import path

from . import views


urlpatterns = [
    path('work/', views.WorkListAPIView.as_view()),
    path('work/<int:pk>', views.WorkDetailView.as_view()),
    path('typework/', views.TypeWorkListAPIView.as_view(), name='typeWork'),
    path('work/add/', views.WorkAddAPIView.as_view(), name='addWork'),
    path('initiator/', views.InitiatorListAPIView.as_view(), name='initiator'),
    path('rank/', views.RankListAPIView.as_view(), name='rank'),
    path('rank/<int:pk>', views.RankUpadateDeleteView.as_view(), name='updateDeleteRank'),
    path('positions/', views.PositionListAPIView.as_view(), name='position'),
    path('positions/<int:pk>', views.PositionUpdateDeleteView.as_view(), name='updateDeletePosition'),
    path('subdivision/', views.SubdivisionListAPIView.as_view(), name='subdivision'),
    path('subdivision/<int:pk>', views.SubdivisionUpdateDeleteView.as_view(), name='updateDeleteSubdivision'),
    path('employee/', views.EmployeeListView.as_view(), name='employee'),



]
