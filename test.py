import socket
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

UnusedSubscriptions = []
UsedSubscriptions = []
NeededSubscriptions = []

jsonSubTrackerUsedReq = {"sender": "subscription-tracker", "services": ["Netflix", "Duolingo", "Dashpass", "Adobe Creative Cloud"], "requested": "Used"}
jsonSubTrackerUnusedReq = {"sender": "subscription-tracker", "services": ["Netflix", "Duolingo", "Dashpass", "Adobe Creative Cloud"], "requested": "Unused"}
jsonSubTrackerNeededReq = {"sender": "subscription-tracker", "services": ["Netflix", "Duolingo", "Dashpass", "Adobe Creative Cloud"], "requested": "Needed"}

jsonTaskManagerUsedReq = {"sender": "task-manager", "services": ["Adobe Creative Cloud", "Office 365"], "requested": "Used"}
jsonTaskManagerUnusedReq = {"sender": "task-manager", "services": ["Adobe Creative Cloud", "Office 365"], "requested": "Unused"}
jsonTaskManagerNeededReq = {"sender": "task-manager", "services": ["Adobe Creative Cloud", "Office 365"], "requested": "Needed"}

socket.send_json(jsonSubTrackerUsedReq)
message = socket.recv_json()
print("Received reply as SubTracker - Used subscriptions/services: ")
print(message)
print()
UsedSubscriptions = message["subscriptions"]

socket.send_json(jsonTaskManagerUsedReq)
message = socket.recv_json()
print("Received reply as TaskManager - Used subscriptions/services: ")
print(message)
print()
UsedSubscriptions = message["subscriptions"]

socket.send_json(jsonSubTrackerUnusedReq)
message = socket.recv_json()
print("Received reply as SubTracker - Unused subscriptions/services: ")
print(message)
print()
UnusedSubscriptions = message["subscriptions"]

socket.send_json(jsonTaskManagerUnusedReq)
message = socket.recv_json()
print("Received reply TaskManager - Unused subscriptions/services: ")
print(message)
print()
UnusedSubscriptions = message["subscriptions"]


socket.send_json(jsonSubTrackerNeededReq)
message = socket.recv_json()
print("Received reply as SubTracker - Needed subscriptions/services: ")
print(message)
print()
NeededSubscriptions = message["subscriptions"]

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