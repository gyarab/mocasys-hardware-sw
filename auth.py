import requests

middleend_host = "127.0.0.1"
middlend_port = "80"
endpoints = {'ping' : '/ping', 'dbquery' : '/qdb', 'auth_methods' : '/auth', 'pass_auth' : '/auth/password', 'card_auth' : '/auth/reader', 'google_auth' : '/auth/google'}

def auth_pass(login, password):
    response = response.post(
            middleend_host+endpoints['pass_auth']
            params = {'username' : login, 'password' : password}
            )
    json_response = response.json()
    session_token = json_response['sessionToken']
    token_expiration = json_response['expiresAt']
    return json_response

def auth_card(card_key, secret_key):
    response = response.post(
            middleend_host+endpoints['card_auth']
            params = {'card_id' : card_key, 'secret_key' : secret_key}
            )
    json_response = response.json()
    session_token = json_response['sessionToken']
    token_expiration = json_response['expiresAt']
    return json_response

def db_query(session_token, query, data):
    if(data not NONE):
        params = {'query_str' : query, 'data' : data}
    else:
        params = {'query_str' : query}

    response = requests.post(
        middleend_host+endpoints['dbquery']
        params = params
        headers = session_token
        )
    json_response = response.json()
    return json_response

