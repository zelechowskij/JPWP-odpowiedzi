from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session



# Korzystając z trzech zaimportowanych narzędzi napisz funkcję zwracającą token autoryzacyjny
# przy pomocy ścieżki Client_credentials flow
# Pomocne mogą okazać się dokumentacje zaimportowanych plików oraz Allegro API
# https://developer.allegro.pl/auth/

def get_access_token():
    client_id = 'd9532d834b4b49c2a6d3b21bb533d118'
    client_secret = "glbJfGbd7fLODVJ743a2SQbZbBFeuOD6krO6WTbNVdam6bQojfC0D6km3f5CwcTO"
    url = "https://allegro.pl/auth/oauth/token"

    auth = HTTPBasicAuth(client_id, client_secret)

    client = BackendApplicationClient(client_id=client_id)

    oauth = OAuth2Session(client=client)

    token = oauth.fetch_token(token_url="https://allegro.pl/auth/oauth/token", auth=auth)
    print(token)
    return token["access_token"]

    return access_token

# Zadanie można prosto rozwiązać nie tylko przy użyciu zaimportowanych bibliotek, ważne by dołączyć nagłówek authorisation
# co w powyższym rozwiązaniu zrobione jest w linijce 15
# każdy ze studentów powinien dostać ten sam token, ze względu na pominięcie autoryzacji przez użytkownika w tym work flow
# jednak poprawność wykonania tego zadania zostanie zweryfikowana w zadaniu 2 i 3