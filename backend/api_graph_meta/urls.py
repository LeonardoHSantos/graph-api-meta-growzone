from django.urls import path
from api_graph_meta.views import *

urlpatterns = [
    path('authorize/',   authorize ,  name='api_graph_account_authorize'),  # create
    # path('account/user/info/<int:user_id>',     home ,  name='api_graph_account_info'),    # read
    # path('account/user/update/<int:user_id>',   home ,  name='api_graph_account_update'),  # update
    # path('account/user/delete/<int:user_id>',   view ,  name='api_graph_account_delete'),  # delete
]