import os
import secrets
import requests
from django.conf           import settings
from django.shortcuts      import redirect
from django.contrib.auth   import login, get_user_model
from app.models import Holding
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from google.oauth2         import id_token
from google.auth.transport import requests as grequests
from django.contrib.auth import logout as django_logout

# Usa el modelo configurado en AUTH_USER_MODEL
User = get_user_model()


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
    auth_url = 'https://accounts.google.com/o/oauth2/v2/auth?' + '&'.join(f'{k}={v}' for k, v in params.items())
    return redirect(auth_url)


def google_callback(request):
    # 0. Comprobar si hay error en la respuesta (como cancelar)
    error = request.GET.get('error')
    if error:
        frontend_url = os.getenv('FRONTEND_URL', 'http://localhost:5173')
        return redirect(f'{frontend_url}?error_login')

    # 1. Validar state
    state = request.GET.get('state')
    if state != request.session.get('oauth_state'):
        return redirect('/?error=state_mismatch')

    # 2. Recuperar el código de autorización
    code = request.GET.get('code')
    if not code:
        return redirect('/?error=no_code')

    # 3. Intercambiar código por tokens
    token_response = requests.post(
        'https://oauth2.googleapis.com/token',
        data={
            'code'         : code,
            'client_id'    : settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri' : settings.GOOGLE_REDIRECT_URI,
            'grant_type'   : 'authorization_code'
        }
    ).json()

    # 4. Verificar el ID‑Token
    idinfo = id_token.verify_oauth2_token(
        token_response.get('id_token'),
        grequests.Request(),
        settings.GOOGLE_CLIENT_ID
    )

    # 5. Crear o recuperar el usuario 
    email = idinfo.get('email')
    name  = idinfo.get('name', '')
    user, _ = User.objects.get_or_create(
        username=email,
        defaults={'first_name': name, 'email': email, 'auth_provider': 'google'}
    )

    # 6. Iniciar sesión
    login(request, user)

    # 7. Redirigir al frontend
    frontend_url = os.getenv('FRONTEND_URL', 'http://localhost:5173')
    return redirect(f'{frontend_url}?logged_in=1')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    '''
    #Buscamos al usuario que se ha autenticado y devolvemos su balance
    return Response({'user_balance': balance}, status=status.HTTP_200_OK)
    '''
    #request.user devuelve el email del usuario
    
    user = request.user
    if not user or not user.is_authenticated:
        return Response({}, status=status.HTTP_200_OK)
        
    
    
    try:
        dolar_holding = Holding.objects.get(user_id=user.id, asset_id=1)    # asset_id=1 del dolar
        balance = dolar_holding.amount * dolar_holding.mean_price
    except Exception as e:
        balance = 0

    
    user_data = {
        'email' : user.email,
        'balance': balance,
        'plan_id': user.plan.id if user.plan else None,
    }

    return Response(user_data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    django_logout(request) 
    return Response({'detail': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)