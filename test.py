import socket
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

UnusedSubscriptions = []
UsedSubscriptions = []
NeededSubscriptions = []

# Acceptable JSON Examples for Subscription Tracker
jsonSubTrackerUsedReq = {"sender": "subscription-tracker", "services": ["Netflix", "Duolingo", "Dashpass", "Adobe Creative Cloud"], "requested": "Used"}
jsonSubTrackerUnusedReq = {"sender": "subscription-tracker", "services": ["Netflix", "Duolingo", "Dashpass", "Adobe Creative Cloud"], "requested": "Unused"}
jsonSubTrackerNeededReq = {"sender": "subscription-tracker", "services": ["Netflix", "Duolingo", "Dashpass", "Adobe Creative Cloud"], "requested": "Needed"}

# Acceptable JSON Examples for Task Manager
jsonTaskManagerUsedReq = {"sender": "task-manager", "services": ["Adobe Creative Cloud", "Office 365"], "requested": "Used"}
jsonTaskManagerUnusedReq = {"sender": "task-manager", "services": ["Adobe Creative Cloud", "Office 365"], "requested": "Unused"}
jsonTaskManagerNeededReq = {"sender": "task-manager", "services": ["Adobe Creative Cloud", "Office 365"], "requested": "Needed"}

# Empty JSON for assignment for values
jsonReq = {"sender": "", "services": [], "requested": ""}
subTrackerData = ["Netflix", "Duolingo", "Dashpass", "Adobe Creative Cloud"]
taskManagerData = ["Adobe Creative Cloud", "Office 365"]

# method A: assigning values to JSON template
print()
print("Method A: assigning values to JSON template")
print("############################################")
print("Sending json made with assigned values to template.")
jsonReq["sender"] = "subscription-tracker"
jsonReq["services"] = subTrackerData
jsonReq["requested"] = "Used"
# print(jsonReq)
socket.send_json(jsonReq)
message = socket.recv_json()
print("Received reply - Used subscriptions/services: ")
print(message)
print()
UsedSubscriptions = message["subscriptions"]

print("Sending json made with assigned values to template.")
jsonReq["sender"] = "task-manager"
jsonReq["services"] = taskManagerData
jsonReq["requested"] = "Used"
# print(jsonReq)
socket.send_json(jsonReq)
message = socket.recv_json()
print("Received reply - Used subscriptions/services.")
print(message)
print()
UsedSubscriptions = message["subscriptions"]

print("Sending json made with assigned values to template.")
jsonReq["sender"] = "subscription-tracker"
jsonReq["services"] = subTrackerData
jsonReq["requested"] = "Unused"
# print(jsonReq)
socket.send_json(jsonReq)
message = socket.recv_json()
print("Received reply - Unused subscriptions/services: ")
print(message)
print()
UnusedSubscriptions = message["subscriptions"]

print("Sending json made with assigned values to template.")
jsonReq["sender"] = "task-manager"
jsonReq["services"] = taskManagerData
jsonReq["requested"] = "Unused"
# print(jsonReq)
socket.send_json(jsonReq)
message = socket.recv_json()
print("Received reply - Unused subscriptions/services.")
print(message)
print()
UnusedSubscriptions = message["subscriptions"]

print("Sending json made with assigned values to template.")
jsonReq["sender"] = "subscription-tracker"
jsonReq["services"] = subTrackerData
jsonReq["requested"] = "Needed"
# print(jsonReq)
socket.send_json(jsonReq)
message = socket.recv_json()
print("Received reply - Needed subscriptions/services: ")
print(message)
print()
NeededSubscriptions = message["subscriptions"]

print("Sending json made with assigned values to template.")
jsonReq["sender"] = "task-manager"
jsonReq["services"] = taskManagerData
jsonReq["requested"] = "Needed"
# print(jsonReq)
socket.send_json(jsonReq)
message = socket.recv_json()
print("Received reply - Needed subscriptions/services.")
print(message)
print()
NeededSubscriptions = message["subscriptions"]

# method B: sending custom typed JSON
print()
print("Method B: sending custom typed JSON")
print("############################################")
print("Sending custom typed JSON.")
socket.send_json(jsonSubTrackerUsedReq)
message = socket.recv_json()
print("Received reply as SubTracker - Used subscriptions/services: ")
print(message)
print()
UsedSubscriptions = message["subscriptions"]

print("Sending custom typed JSON.")
socket.send_json(jsonTaskManagerUsedReq)
message = socket.recv_json()
print("Received reply as TaskManager - Used subscriptions/services: ")
print(message)
print()
UsedSubscriptions = message["subscriptions"]

print("Sending custom typed JSON.")
socket.send_json(jsonSubTrackerUnusedReq)
message = socket.recv_json()
print("Received reply as SubTracker - Unused subscriptions/services: ")
print(message)
print()
UnusedSubscriptions = message["subscriptions"]

print("Sending custom typed JSON.")
socket.send_json(jsonTaskManagerUnusedReq)
message = socket.recv_json()
print("Received reply TaskManager - Unused subscriptions/services: ")
print(message)
print()
UnusedSubscriptions = message["subscriptions"]

print("Sending custom typed JSON.")
socket.send_json(jsonSubTrackerNeededReq)
message = socket.recv_json()
print("Received reply as SubTracker - Needed subscriptions/services: ")
print(message)
print()
NeededSubscriptions = message["subscriptions"]

print("Sending custom typed JSON.")
socket.send_json(jsonTaskManagerNeededReq)
message = socket.recv_json()
print("Received reply TaskManager - Needed subscriptions/services: ")
print(message)
print()
NeededSubscriptions = message["subscriptions"]

print("UsedSubscriptions: ")
print(UsedSubscriptions)
print("UnusedSubscriptions: ")
print(UnusedSubscriptions)
print("NeededSubscriptions: ")
print(NeededSubscriptions)

