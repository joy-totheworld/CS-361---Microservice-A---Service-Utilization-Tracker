import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

subTrackerSubscriptions = ["Netflix", "Duolingo", "Dashpass", "Adobe Creative Cloud"]
taskManagerServices = ["Adobe Creative Cloud", "Office 365"]

# # TESTING AS TASK MANAGER

# UnusedSubscriptions = []
# UsedSubscriptions = []
# NeededSubscriptions = []

# # first request should identify sending program, either "task-manager" or "subscription-tracker"
# print(f"Sending request as task-manager - identifing sender")
# socket.send_string("task-manager")
# message = socket.recv_string()
# print(f"Response:")
# print(message)
# print()


# # second request should convey number of subscrption/service names to be sent next
# print(f"Sending request as task-manager - # of service names")
# socket.send_string(str(len(taskManagerServices)))
# message = socket.recv_string()
# print(f"Response:")
# print(message)
# print()

# # next requests send each subscription/service name
# for x in range(len(taskManagerServices)):
#     print(f"Sending request as task-manager - service name {x}")
#     socket.send_string(taskManagerServices[x])
#     message = socket.recv_string()
#     print(f"Response:")
#     print(message)
#     print()


# TESTING AS SUBSCRIPTION TRACKER

UnusedSubscriptions = []
UsedSubscriptions = []
NeededSubscriptions = []

# first request should identify sending program, either "task-manager" or "subscription-tracker"
print(f"Sending request as subscription-tracker - identifing sender")
socket.send_string("subscription-tracker")
message = socket.recv_string()
print(f"Response:")
print(message)
print()


# second request should convey number of subscrption/service names to be sent next
print(f"Sending request as subscription-tracker - # of service names")
socket.send_string(str(len(subTrackerSubscriptions)))
message = socket.recv_string()
print(f"Response:")
print(message)
print()

# next requests send each subscription/service name
for x in range(len(subTrackerSubscriptions)):
    print(f"Sending request as task-manager - service name {x}")
    socket.send_string(subTrackerSubscriptions[x])
    message = socket.recv_string()
    print(f"Response:")
    print(message)
    print()

# receive message about mode
socket.send_string("Done sending names.")
message = socket.recv_string()
print(f"Response:")
print(message)
print()

# request array of used services
socket.send_string("Used")
numNames = socket.recv_string()
print(f"Response:")
print(numNames)
print()
incomingNumNames = int(numNames)

# next receive each subscription/service name
for x in range(incomingNumNames):
    message = socket.recv_string()
    UsedSubscriptions.append(message)
    print(message)
    socket.send_string("Name received")
print("UsedSubscriptions: ")
print(UsedSubscriptions)

# request array of unused services
socket.send_string("Unused")
numNames = socket.recv_string()
print(f"Response:")
print(numNames)
print()
incomingNumNames = int(numNames)

# next receive each subscription/service name
for x in range(incomingNumNames):
    message = socket.recv_string()
    UnusedSubscriptions.append(message)
    print(message)
    socket.send_string("Name received")
print("UmusedSubscriptions: ")
print(UnusedSubscriptions)

# request array of needed services
socket.send_string("Needed")
numNames = socket.recv_string()
print(f"Response:")
print(numNames)
print()
incomingNumNames = int(numNames)

# next receive each subscription/service name
for x in range(incomingNumNames):
    message = socket.recv_string()
    NeededSubscriptions.append(message)
    print(message)
    socket.send_string("Name received")
print("NeededSubscriptions: ")
print(NeededSubscriptions)

# send exit message
socket.send_string("exit")
message = socket.recv_string()
print(f"Response:")
print(message)
print()

# # next reply should convey number of subscrption/service names to be received in Unused Services array
# print(f"Unused")
# socket.send_string(str(len(subTrackerSubscriptions)))
# numNames = socket.recv_string()
# print(f"Response:")
# print(numNames)
# print()
# incomingNumNames = int(numNames)

# # next receive each subscription/service name
# for x in range(incomingNumNames):
#     message = socket.recv_string()
#     UsedSubscriptions.append(message)
#     print(message)
#     socket.send_string("Name received")











