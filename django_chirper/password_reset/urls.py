from django.urls import path
from .views import (BeginPasswordResetView, ConfirmPasswordResetView, 
    ResetPasswordView, ResetPasswordCompleteView)


urlpatterns = [
    path('begin_password_reset/', BeginPasswordResetView.as_view(), name = 'account_beginPasswordReset'),
    path('confirm_password_reset/', ConfirmPasswordResetView.as_view(), name = 'account_confirmPasswordReset'),
    path('reset_password/<uidb64>/<token>/', ResetPasswordView.as_view(), name = 'password_reset_confirm'),
    # name = 'password_reset_confirm' can't be customized
    path('password_reset_complete/', ResetPasswordCompleteView.as_view(), name = 'password_reset_complete')
]