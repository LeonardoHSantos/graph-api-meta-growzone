from django.urls import path
from app_user_auth.views import *

urlpatterns = [
    path('account/',                        home,   name='app_account'),
    path('account/authorize/',              authorize, name='app_user_account_authorize'),    # authorize
    path('account/authorize/message/',      authorize_message, name='app_user_account_authorize_message'),    # authorize
    path('account/info/<int:user_id>',      info,   name='app_user_account_info'),      # read
    path('account/update/<int:user_id>',    update, name='app_user_account_update'),    # update
    path('account/delete/<int:user_id>',    delete, name='app_user_account_delete'),    # delete
]