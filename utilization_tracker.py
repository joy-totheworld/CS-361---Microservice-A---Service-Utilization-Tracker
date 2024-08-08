import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

taskManagerSubscriptions = []
subscriptionTrackerSubscriptions = []

while True:
    UnusedSubscriptions = []
    UsedSubscriptions = []
    NeededSubscriptions = []

    message = socket.recv_json()
    print("Received request: ", message)
    print('message["sender"]: ', message["sender"])
    print('message["services"]: ', message["services"])
    print('message["requested"]: ', message["requested"])

    if (message["sender"] == "task-manager"):
        taskManagerSubscriptions = message["services"]
    elif (message["sender"] == "subscription-tracker"):
        subscriptionTrackerSubscriptions = message["services"]

    for i in range(len(subscriptionTrackerSubscriptions)):
        used = 0
        for j in range(len(taskManagerSubscriptions)):
            if (subscriptionTrackerSubscriptions[i]==taskManagerSubscriptions[j]):
                UsedSubscriptions.append(subscriptionTrackerSubscriptions[i])
                used = 1
                j = len(taskManagerSubscriptions)
        
        if (used == 0):
            UnusedSubscriptions.append(subscriptionTrackerSubscriptions[i])

    for j in range(len(taskManagerSubscriptions)):
        exsisting = 0
        for i in range(len(subscriptionTrackerSubscriptions)):
            if (subscriptionTrackerSubscriptions[i]==taskManagerSubscriptions[j]):
                exsisting = 1
                i = len(subscriptionTrackerSubscriptions)
        
        if (exsisting == 0):
            NeededSubscriptions.append(taskManagerSubscriptions[j])

    print("UsedSubscriptions: ")
    print(UsedSubscriptions)
    print("UnusedSubscriptions: ")
    print(UnusedSubscriptions)
    print("NeededSubscriptions: ")
    print(NeededSubscriptions)
    
    if (message["requested"] == "Used"):
        print("Sent UsedSubscriptions")
        socket.send_json({"error": "no", "subscriptions": UsedSubscriptions})
    elif (message["requested"] == "Unused"):
        print("Sent UnusedSubscriptions")
        socket.send_json({"error": "no", "subscriptions": UnusedSubscriptions})
    elif (message["requested"] == "Needed"):
        print("Sent NeededSubscriptions")
        socket.send_json({"error": "no", "subscriptions": NeededSubscriptions})
    else:
        print("Sent Error")
        socket.send_json({"error": "yes", "subscriptions": []})
        
        



        


    
    

