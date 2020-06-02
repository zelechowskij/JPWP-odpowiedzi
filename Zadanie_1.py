from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session



# Korzystając z trzech zaimportowanych narzędzi napisz funkcję zwracającą token autoryzacyjny
# przy pomocy ścieżki Client_credentials flow
# Pomocne mogą okazać się dokumentacje zaimportowanych plików oraz Allegro API
# https://developer.allegro.pl/auth/
# uzyskany token można dołączyć na końcu pliku

def get_access_token():
    client_id = 'd9532d834b4b49c2a6d3b21bb533d118'
    client_secret = "glbJfGbd7fLODVJ743a2SQbZbBFeuOD6krO6WTbNVdam6bQojfC0D6km3f5CwcTO"
    url = "https://allegro.pl/auth/oauth/token"




    print(token)
    return access_token