# ./main.py

#can create variables for client id and client secret as strings
import os
import smartcar 
from flask import Flask, redirect, request, jsonify
app=Flask("myapp")


# TODO: Authorization Step 1a: Launch Smartcar authentication dialog
client = smartcar.AuthClient(
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET'),
    redirect_uri=os.environ.get('REDIRECT_URI'),
    scope=['read_vehicle_info'],
    test_mode=True,
)

@app.route('/login', methods=['GET'])

#def index
def login():
    # TODO: Authorization Step 1b: Launch Smartcar authentication dialog
    auth_url = client.get_auth_url()
    return redirect(auth_url)

access = None

@app.route('/exchange', methods=['GET'])
def exchange():
    # TODO: Authorization Step 3: Handle Smartcar response
    code = request.args.get('code')
    
    print(code)
    
    return '', 200