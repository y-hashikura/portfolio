"""
DjangoプロジェクトのURL管理モジュール
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponseRedirect

urlpatterns = [
    # 管理画面のURL
    path('admin/', admin.site.urls), 
    # ルートディレクトリにアクセス時にデフォルトでタスク管理ツールのメインパスを指定するように変更
    path('', lambda request: HttpResponseRedirect('/my_profile/')),
    # マイプロフィールパス
    path('my_profile/', include('my_profile.urls'))
    # # タスク管理ツール
    # path('task_manager/', include('task_manager.urls')),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
