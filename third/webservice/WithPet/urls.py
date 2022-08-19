
#from . import views


#urlpatterns = [
    #path('', views.index, name='index'),

#]



from .views import *

from django.contrib import admin
from django.urls import path, include
# index는 대문, blog는 게시판
from WithPet.views import index, blog, posting, spot



# 이미지를 업로드하자
from django.conf import settings
from django.conf.urls.static import static


#app_name='main'

urlpatterns=[
    #path('',index),
    #path('blog/',blog),

    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>',posting, name="posting"),
    path('blog/new_post/', new_post),
    ##삭제 버튼
    path('blog/<int:pk>/remove/', remove_post),

    path('spot/', spot, name='spot'),
    path('spot-detail', spot_detail, name='spot-detail'),
    path('mypage/', my_page, name='mypage')
] 

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
