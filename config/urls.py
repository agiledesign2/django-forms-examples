
from django.contrib import admin
from django.urls import path
from contact import views as contact
from user import views as user


urlpatterns = [
    path('admin/', admin.site.urls),

    # app_1
    #FBV
    path('', contact.contactPage),
    path('ajax/contact', contact.postContact, name = 'contact_submit'),
    #CBV
    path('contact_cbv', contact.ContactAjax.as_view(), name = 'contact_submit_cbv'),

    #app_2
    path('user', user.userPanel),
    path('ajax/get_user_info', user.getUserInfo, name = 'get_user_info'),

]
