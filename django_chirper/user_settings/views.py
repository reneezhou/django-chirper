from datetime import datetime
from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import (SettingsAuthForm, UpdateUsernameForm, UpdateProfileForm,
    UpdateScreenNameForm)


def settings(request):
    if request.user.is_authenticated:
        return redirect('settings_account')
    else:
        return redirect('settings_account_personalization')


@login_required
def settings_account(request):
    return render(request, 'settings_account.html')


def settings_yourChirperData_account(request):
    if request.user.is_authenticated:
        if 'auth_timestamp' not in request.session.keys():
            form = SettingsAuthForm(request.POST or None)

            if form.is_valid():
                password = form.cleaned_data.get('password')
                username = request.user.username
                if authenticate(request, username = username, password = password):
                    encoded_auth_timestamp = DjangoJSONEncoder().encode(timezone.now())
                    request.session['auth_timestamp'] = encoded_auth_timestamp
                    return render(request, 'settings_yourChirperData_account.html')
                else:
                    form.add_error(field = None, error = 'The password you entered was incorrect.')

            context = {'form': form}
            return render(request, 'settings_yourChirperData_auth.html', context)

        else:
            datetime_auth_timestamp = datetime.strptime(
                request.session.get('auth_timestamp')[1:-1], 
                "%Y-%m-%dT%H:%M:%S.%fZ"
            )
            if (timezone.now().replace(tzinfo = None) - datetime_auth_timestamp).total_seconds() > 300:
                request.session.pop('auth_timestamp')
                return redirect('settings_yourChirperData_account')

    return render(request, 'settings_yourChirperData_account.html')


def settings_yourChirperData(request):
    if request.user.is_authenticated:
        if 'auth_timestamp' not in request.session.keys():
            form = SettingsAuthForm(request.POST or None)

            if form.is_valid():
                password = form.cleaned_data.get('password')
                username = request.user.username
                if authenticate(request, username = username, password = password):
                    encoded_auth_timestamp = DjangoJSONEncoder().encode(timezone.now())
                    request.session['auth_timestamp'] = encoded_auth_timestamp
                    return render(request, 'settings_yourChirperData.html')
                else:
                    form.add_error(field = None, error = 'The password you entered was incorrect.')

            context = {'form': form}
            return render(request, 'settings_yourChirperData_auth.html', context)

        else:
            datetime_auth_timestamp = datetime.strptime(
                request.session.get('auth_timestamp')[1:-1], 
                "%Y-%m-%dT%H:%M:%S.%fZ"
            )
            if (timezone.now().replace(tzinfo = None) - datetime_auth_timestamp).total_seconds() > 300:
                request.session.pop('auth_timestamp')
                return redirect('settings_yourChirperData')
    return render(request, 'settings_yourChirperData.html')


def settings_account_personalization(request):
    return render(request, 'settings_account_personalization.html')


@login_required
def settings_password(request):
    return render(request, 'settings_password.html')


@login_required
def settings_screenName(request):
    form = UpdateScreenNameForm(request.POST or None, instance = request.user.profile)

    if form.is_valid():
        request.user.profile.handle = form.cleaned_data.get('handle')
        request.user.save()
        return redirect('settings_yourChirperData_account')

    context = {'form': form}
    return render(request, 'settings_screenName.html', context)


@login_required
def settings_securityAndAccountAccess(request):
    return render(request, 'settings_securityAndAccountAccess.html')


@login_required
def settings_privacyAndSafety(request):
    return render(request, 'settings_privacyAndSafety.html')


@login_required
def settings_notifications(request):
    return render(request, 'settings_notifications.html')


@login_required
def settings_accessibilityDisplayAndLanguages(request):
    return render(request, 'settings_accessibilityDisplayAndLanguages.html')


def settings_about(request):
    return render(request, 'settings_about.html')


@login_required
def settings_phone(request):
    return render(request, 'settings_phone.html')


@login_required
def settings_addPhone_auth(request):
    return render(request, 'settings_addPhone_auth.html')


@login_required
def settings_addPhone(request):
    return render(request, 'settings_addPhone.html')


@login_required
def settings_deletePhone(request):
    return render(request, 'settings_deletePhone.html')



@login_required
def settings_email(request):
    return render(request, 'settings_email.html')


@login_required
def settings_addEmail_auth(request):
    return render(request, 'settings_addEmail_auth.html')


@login_required
def settings_addEmail(request):
    return render(request, 'settings_addEmail.html')


@login_required
def settings_audienceAndTagging(request):
    return render(request, 'settings_audienceAndTagging.html')


@login_required
def settings_country(request):
    return render(request, 'settings_country.html')


def settings_languages(request):
    return render(request, 'settings_languages.html')


def settings_yourChirperData_gender(request):
    return render(request, 'settings_yourChirperData_gender.html')


def settings_yourChirperData_age(request):
    return render(request, 'settings_yourChirperData_age.html')


@login_required
def settings_trends(request):
    return render(request, 'settings_trends.html')


@login_required
def settings_contentPreferences(request):
    return render(request, 'settings_contentPreferences.html')


@login_required
def settings_appsAndSessions(request):
    return render(request, 'settings_appsAndSessions.html')


@login_required
def settings_profile(request):
    if request.method == 'POST':
        u_form = UpdateUsernameForm(request.POST, instance = request.user) 
        p_form = UpdateProfileForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile', handle = request.user.profile.handle)
        

    elif request.method == 'GET':
        u_form = UpdateUsernameForm(instance = request.user)
        p_form = UpdateProfileForm(instance = request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'settings_profile.html', context)