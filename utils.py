import json
import requests
import urllib.parse
from urllib.parse import urlencode

items_ids = {'safer': 'c3f48419b19a4d839449125dfd2deb9d',
             'cleaner': '588b2c9a770b4a6fb1acff2a176a1d03',
             'greener': '4016d459aeaa4c8cb4a298328a4059a6',
             'economic': '79977e7183844b61b742225f8c918686',
             'core' : '44e83e52931e4e16aae3e8aa6babd2ed',
             'housing': 'ace6a4e12b08463fbd37289c85d68ed0'} 

def generate_token(username, password):
    """Generates an ArcGIS Online token."""
    url = 'https://arcgis.com/sharing/rest/generateToken'

    payload = {
        'username': username,
        'password': password,
        'referer': 'https://arcgis.com',
        'f': 'json'
    }
    encoded_payload = urlencode(payload)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=encoded_payload, headers=headers)
    response.raise_for_status()
    token_data = response.json()
    if "error" in token_data:
        raise ValueError(f"Error generating token: {token_data['error']}")
    return token_data['token'] 

def fetch_dashboard_data(org_id, token, dashboard_itemid):
    """Fetches the dashboard configuration JSON."""
    url = f"https://{org_id}.maps.arcgis.com/sharing/rest/content/items/{dashboard_itemid}/data"
    params = {'token': token, 'f': 'json'}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def update_dashboard(token, dashboard_itemid, updated_json):
        regular_json = json.dumps(updated_json)
        #encoded_json = urllib.parse.quote(json.dumps(parsed_json))
        #compressed_data = gzip.compress(json.dumps(parsed_json).encode('utf-8'))

        form_data = {
            'f': 'json',
            'id': dashboard_itemid,
            'token': token,
            'text': regular_json
        }
        # Seems to be necessary to encode it all, otherwise we get an error about our URI being too long
        # since the entire json contents are passed in the URL, encoding makes it more compact I believe?
        encoded_form_data = urllib.parse.urlencode(form_data)

        update_url = f'https://www.arcgis.com/sharing/rest/content/users/maps.phl.data/items/{dashboard_itemid}/update'
        print(update_url)

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(update_url, headers=headers, data=encoded_form_data)
        print(response.text)
        assert response.status_code == 200
        if 'success' in response.text:
            print('Dashboard successfully updated.')
        else:
            print('Failure???')