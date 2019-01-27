# ./main.py

#can create variables for client id and client secret as strings
import os
import smartcar 
from flask import Flask, redirect, request, jsonify
app=Flask("myapp")

vehicle_url = "http://localhost:8000/vehicle"
# TODO: Authorization Step 1a: Launch Smartcar authentication dialog
client = smartcar.AuthClient(
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET'),
    redirect_uri=os.environ.get('REDIRECT_URI'),
    scope=['read_vehicle_info','read_vin','read_odometer','read_location','control_security', 'control_security:unlock', 'control_security:lock'],
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
# global variable to save our access_token

def exchange():
    code = request.args.get('code')

    # TODO: Request Step 1: Obtain an access token
    # access our global variable and store our access tokens
    global access
    # in a production app you'll want to store this in some kind of
    # persistent storage
    access = client.exchange_code(code)
    print (access)
    return redirect(vehicle_url)

@app.route('/vehicle', methods=['GET'])
def vehicle():
    # access our global variable to retrieve our access tokens
    global access
    # the list of vehicle ids
    vehicle_ids = smartcar.get_vehicle_ids(
        access['access_token'])['vehicles']
    
    # TODO: Request Step 3: Create a vehicle    
    # instantiate the first vehicle in the vehicle id list
    vehicle = smartcar.Vehicle(vehicle_ids[0], access['access_token']) #Get vehicle general info
    info = vehicle.info()

    response = vehicle.vin() #Gets vehicle vin number

    call = vehicle.location() #Gets vehicle's location

    distance = vehicle.odometer()

    info["vin"]=response
    info["distance"]=distance
   
    info.update(call) #Merges data
    print(info)

    return jsonify(info)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)

'''@app.route('/user', methods=['GET'])    #gets user id
def userid():

    global access

    response = smartcar.get_user_id(access['access_token'])
    print(response)
    return jsonify(response)




    response = smartcar.get_user_id(access['access_token'])
    print(response)'''
