import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

incomingNumNames = -1
taskManagerSubscriptions = []
subscriptionTrackerSubscriptions = []



while True:

    UnusedSubscriptions = []
    UsedSubscriptions = []
    NeededSubscriptions = []

    clientIdentifier = socket.recv_string()
    print(f"Received client identification: {clientIdentifier}")

    #  Send reply back to client
    socket.send_string("Please send an integer representing the number of subscrption/service names to be sent next:")

    numNames = socket.recv_string()
    print(f"Received integer: {numNames}")
    socket.send_string("Integer received. Please send any subscription/service names next:")
    incomingNumNames = int(numNames)

    if (clientIdentifier == "task-manager"):
        taskManagerSubscriptions = []
        for x in range( incomingNumNames):
            message = socket.recv_string()
            taskManagerSubscriptions.append(message)
            print(message)
            socket.send_string("Name received")

    if (clientIdentifier == "subscription-tracker"):
        subscriptionTrackerSubscriptions = []
        for x in range( incomingNumNames):
            message = socket.recv_string()
            subscriptionTrackerSubscriptions.append(message)
            print(message)
            socket.send_string("Name received")

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

    # receive 'done sending names' message. 
    message = socket.recv_string()
    print(f"Message from client: {message}")
    socket.send_string('Please send "Used", "Unused", or "Needed" to get a list of service/subscription names. Send "exit" when done. ')

    mode = ""
    while (mode != "exit"):
        mode = socket.recv_string()
        print(f"mode: {mode}")

        if (mode == "exit"):
            socket.send_string('exit command received.')

        elif (mode == "Used"):
            print(message)
            print()
            print(f"Sending # of names in UsedSubscriptions")
            socket.send_string(str(len(UsedSubscriptions)))

            # next replies send each subscription/service name
            for x in range(len(UsedSubscriptions)):
                message = socket.recv_string()
                print(f"Response:")
                print(message)
                print()
                print(f"Sending used subscription name at idx {x}")
                socket.send_string(UsedSubscriptions[x])

        elif (mode == "Unused"):
            print(message)
            print()
            print(f"Sending # of names in UnusedSubscriptions")
            socket.send_string(str(len(UnusedSubscriptions)))

            # next replies send each subscription/service name
            for x in range(len(UnusedSubscriptions)):
                message = socket.recv_string()
                print(f"Response:")
                print(message)
                print()
                print(f"Sending unused subscription name at idx {x}")
                socket.send_string(UnusedSubscriptions[x])

        elif (mode == "Needed"):
            print(message)
            print()
            print(f"Sending used # of names in NeededSubscriptions")
            socket.send_string(str(len(NeededSubscriptions)))

            # next replies send each subscription/service name
            for x in range(len(NeededSubscriptions)):
                message = socket.recv_string()
                print(f"Response:")
                print(message)
                print()
                print(f"Sending needed subscription name at idx {x}")
                socket.send_string(NeededSubscriptions[x])


    
    




    






        


    
    

