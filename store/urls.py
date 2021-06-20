from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import CategoriesListView, TagsListView, CommentCreateView, ProductViewSet


router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include("account.urls")),
    path('api/categories/', CategoriesListView.as_view(), name="categories-list"),
    path('api/tags/', TagsListView.as_view(), name="tags-list"),
    path('api/comments/', CommentCreateView.as_view(), name="create-comment")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


