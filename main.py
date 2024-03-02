import scratchattach as scratch3
import os

USERNAME = os.environ['username']
PASSWORD = os.environ['password']

session = scratch3.login(USERNAME, PASSWORD)
conn = session.connect_cloud("950783494")

client = scratch3.CloudRequests(conn)


@client.request
def balance(argument1):
    print(f"Balance requested for user {argument1}")
    return ["NOTICE:",
            "The ScratchCredit API hasn't been implemented yet, but the request has still been ",
            f"recieved successfully either way. (Balance requested by {argument1})",
            "Your balance will be automatically set to 100 ScratchCredits when the API gets ",
            "up and running."]


@client.request
def give_sc(argument1, argument2):
    print(f"Somebody requested giving {argument2} SC to {argument1}")
    return ["NOTICE:",
            "The ScratchCredit API hasn't been implemented yet, but the request has still been ",
            f"recieved successfully either way. (You tried giving {argument2} SC to {argument1})",
            f"You'll be able to give {argument2} SC to {argument1} when the API gets up and running.",
            "THANKS FOR THE GENEROSITY, THOUGH!"]


@client.event
def on_ready():
    print("Request handler is running")


@client.event
def on_request(request):
    print("Received request", request.name, request.requester, request.arguments, request.timestamp, request.id)


client.run(thread=True)
