# CS 361 - Microservice A - Service Utilization Tracker
 
 Communication Contract
 Requests will be made via ZeroMQ’s request/reply system. 

 To request data to this service utilization tracker microservice, a required parameter will be a JSON with the following fields:
    {“sender”: “”, “services”: [“”, “”], “requested”: “”}

    - The request-type field of the JSON parameter will contain a string reading "subscription-tracker" or "task-manager".
    - The services field of the JSON parameter will contain an array of strings, where each string is the name is the name of a subscription/service. The subscription tracker will send an array containing the name of every exsisting subscription, whereas the task manager will send an array containing the name of every service needed for planned tasks. 
    - The requested field of the JSON parameter will contain a string reading either "Used", "Unused", or "Needed"

 Replies will consist of JSON with the following fields:
     {“error”: “”, 
      “services”: [“”, “”]}
 The error field of the JSON returned in the reply will contain either a string reading "yes" or a string reading "no".
 The subscriptions field of the JSON returned in the reply will contain an array of strings, where each string is the name of a subscription/service. Please note that there can be instances where an empty array is returned in the subscriptions field of the JSON


Pseudocode for requesting program:
    socket.send_json({“sender”: “”, “services”: [“”, “”], “requested”: “”})
    response = socket.recv_json

Pseudocode for this microservice:

    requested = socket.recv_json

    If (requested == Unused):
        socket.send_json({“error”: “no”, “subscriptions”: [“”, “”]})
    Elif (requested == Used):
        socket.send_json({“error”: “no”, “subscriptions”: [“”, “”]})
    Elif (requested == Needed):
        socket.send_json({“error”: “no”, “subscriptions”: [“”, “”]})
    Else:
        socket.send_json({“error”: “yes”, “subscriptions”: []})
