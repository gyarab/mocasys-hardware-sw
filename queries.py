import auth, requests

lunch_price = 20

def get_lunch(token):
    #get card key
    user = auth.db_query("SELECT * FROM users_current WHERE username = $"+card_key).json()
    if (user["money"] >= lunch_price):
        #display lunch id
        #substract money
    elif (user["money"] < lunch_price):
        #not enoung money exception
    elif (user["lunch"] == NONE or user["lunch"]  == 0):
        #no lunch choice
    elif (user["isTaken"] == 1):
        #user already recieved lunch

