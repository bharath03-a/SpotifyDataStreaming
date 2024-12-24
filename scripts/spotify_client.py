import os
import sys
import json
import requests
import webbrowser
from urllib.parse import urlencode, urlparse, parse_qs

# Add the parent directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import helper.constants as CNST
import helper.secrets as SEC

class SpotifyClient():
    """A class used to interact with an API by managing access tokens and sending requests."""

    def __init__(self):
        """Initializes the API class instance. Currently, no initialization logic is required."""
        self.access_token = None
    
    def get_authorization_code(self):
        params = {
            "client_id": SEC.CLIENT_ID,
            "response_type": "code",
            "redirect_uri": CNST.REDIRECT_URI
        }
        auth_url = f"{CNST.AUTH_URL}?{urlencode(params)}"
        webbrowser.open(auth_url)
        redirect_response = input("Paste the full redirect URL here: ")
        parsed_url = urlparse(redirect_response)
        auth_code = parse_qs(parsed_url.query).get('code')[0]
        return auth_code

    def get_access_token(self):
        try: 
            CNST.TOKEN_REQUEST_BODY['client_id'] = SEC.CLIENT_ID
            CNST.TOKEN_REQUEST_BODY['client_secret'] = SEC.CLIENT_SECRET

            response = requests.request("POST",
                                        url=CNST.TOKEN_URL,
                                        headers=CNST.TOKEN_HEADER,
                                        data=CNST.TOKEN_REQUEST_BODY)
            
            access_token = response.json()['access_token']
        except Exception as e:
            print(f"Error: {e}")
            access_token = None

        return access_token
    
    def get_top_artists(self):
        try:
            access_token = self.get_access_token()
            CNST.API_HEADER['Authorization'] = CNST.API_HEADER['Authorization'].format(access_token = access_token)

            params = {
                "time_range": "long_term",
                "limit": 10,
                "offset": 0,
            }

            response = requests.get(
                url = CNST.SPOTIFY_BASE_URL + CNST.TOP_ITEMS.format(type='artists'),
                headers = CNST.API_HEADER,
                params = params
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                print("Error: Unauthorized access.")
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Body: {response.text}")
                return None
            else:
                print(f"Error: {response.status_code}")
                print(f"Response Body: {response.text}")
                return None
            
        except Exception as e:
            print(f"Error: {e}")
            return None


if __name__ == "__main__":
    client = SpotifyClient()
    auth_code = client.get_authorization_code()
    client.get_access_token(auth_code)
    top_artists = client.get_top_artists()
    print(top_artists)