from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v21-0/graph-meta/', include('api_graph_meta.urls')),
    path('app/user/', include('app_user_auth.urls')),
]

# VER TUDO | STORYES | REELS | POSTS | VIDEOS
# selecionar tudo
# [x] post 1 ---- doddodododoo - [vincular este post]
# [x] post 1 ---- doddodododoo - [vincular este post]
# [] post 1 ---- doddodododoo - [vincular este post]
# [] post 1 ---- doddodododoo - [vincular este post]
# [] post 1 ---- doddodododoo - [vincular este post]
# [] post 1 ---- doddodododoo - [vincular este post]
# [] post 1 ---- doddodododoo - [vincular este post]
# [] post 1 ---- doddodododoo - [vincular este post]
# [] post 1 ---- doddodododoo - [vincular este post]x'


# growzone.co/api/v21-0/graph-meta/account/authorize/