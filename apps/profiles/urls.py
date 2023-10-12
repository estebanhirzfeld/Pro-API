from django.urls import path

from .views import (
    FollowersListView,
    FollowingListView,
    ProfileDetailAPIView,
    YourProfileDetailView,
    ProfileListAPIView,
    FollowAPIView,
    UnfollowAPIView,
    UpdateProfileAPIView,
)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="all-profiles"),
    path("me/", YourProfileDetailView.as_view(), name="my-profile"),
    path("me/update/", UpdateProfileAPIView.as_view(), name="update-profile"),
    path("me/following/", FollowingListView.as_view(), name="following"),
    path("<uuid:user_id>/profile/", ProfileDetailAPIView.as_view(), name="user-profile"),
    path("<uuid:user_id>/followers/", FollowersListView.as_view(), name="followers"),
    path("<uuid:user_id>/follow/", FollowAPIView.as_view(), name="follow"),
    path("<uuid:user_id>/unfollow/", UnfollowAPIView.as_view(), name="unfollow"),
]
