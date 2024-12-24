import json
import requests
import helper.constants as CNST
import helper.secrets as SEC

class API():
    """A class used to interact with an API by managing access tokens and sending requests."""

    def __init__(self):
        """Initializes the API class instance. Currently, no initialization logic is required."""
        pass

    def get_access_token(self):
        """Requests and retrieves an access token from the API.nThis method makes a POST request to the 
        token URL with the client ID and client secret in the request body.

        Returns:
            str: The access token retrieved from the API response.
        """
        CNST.TOKEN_REQUEST_BODY['client_id'] = SEC.CLIENT_ID
        CNST.TOKEN_REQUEST_BODY['client_secret'] = SEC.CLIENT_SECRET

        response = requests.request("POST",
                                    url=CNST.TOKEN_URL,
                                    headers=CNST.TOKEN_HEADER,
                                    data=CNST.TOKEN_REQUEST_BODY)
        
        access_token = response.json()['access_token']

        return access_token
    
    def get_spotify_data(self):
        pass