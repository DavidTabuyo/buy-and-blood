import secrets, requests
from django.shortcuts  import redirect
from django.conf       import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from google.oauth2 import id_token
from google.auth.transport import requests as grequests

def google_login(request):
    state = secrets.token_urlsafe(16)
    request.session['oauth_state'] = state
    params = {
        'client_id'    : settings.GOOGLE_CLIENT_ID,
        'response_type': 'code',
        'scope'        : 'openid email profile',
        'redirect_uri' : settings.GOOGLE_REDIRECT_URI,
        'state'        : state,
        'access_type'  : 'offline',
        'prompt'       : 'select_account'
    }
    url = 'https://accounts.google.com/o/oauth2/v2/auth?' + '&'.join(f'{k}={v}' for k,v in params.items())
    return redirect(url)

def google_callback(request):
    # 1. Validar state
    state = request.GET.get('state')
    if not state or state != request.session.get('oauth_state'):
        return redirect('/?error=state_mismatch')

    code = request.GET.get('code')
    if not code:
        return redirect('/?error=no_code')

    # 2. Intercambiar código por tokens
    token_resp = requests.post(
        'https://oauth2.googleapis.com/token',
        data={
            'code'         : code,
            'client_id'    : settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri' : settings.GOOGLE_REDIRECT_URI,
            'grant_type'   : 'authorization_code'
        }
    ).json()
    idinfo = id_token.verify_oauth2_token(
        token_resp['id_token'],
        grequests.Request(),
        settings.GOOGLE_CLIENT_ID
    )

    # 3. Obtener o crear Django User
    email = idinfo['email']
    name  = idinfo.get('name', '')
    user, _ = User.objects.get_or_create(username=email, defaults={'first_name': name})
    # opcional: actualizar datos de perfil aquí

    # 4. Loguear y crear sesión
    login(request, user)

    # 5. Redirigir a tu frontend
    frontend_url = 'http://localhost:8080/'  # o lee de settings
    return redirect(f'{frontend_url}?logged_in=1')
