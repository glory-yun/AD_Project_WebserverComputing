from django.contrib import admin
from django.urls import path, include
from pybo.views import book_views
from pybo.views import base_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ pybo 네임스페이스 등록
    path('pybo/', include(('pybo.urls', 'pybo'), namespace='pybo')),

    # ✅ 책 관련 뷰는 직접 등록
    path('books/', book_views.book_list, name='book_list'),
    path('books/<int:book_id>/history/',
         book_views.book_history, name='book_history'),

    # ✅ 회원 관련 URL
    path('common/', include('common.urls')),

    # ✅ 루트는 pybo의 index
    path('', base_views.index, name='index'),
]

# 정적/미디어 파일
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 404 에러 핸들링
handler404 = 'common.views.page_not_found'
