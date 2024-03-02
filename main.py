import scratchattach as scratch3
from termcolor import colored

sessionID = ".eJxVT8tOhDAU_ZeuZ7AtFMrsNEYTkzFqzERWpKUX6AAtwyNjNP67twmb2d2c1z3nl6wzTE4NQA6k8Os8Q_15IjtSqnVpy0CW1iDHeJoJlicZcgvMS-V9Z4Pp6qcOzK1Dq6oDF2wBA7fYSi3Wu2gj5ugDxn4DHzYx5no80ERpnplEGg2JTkyKXynVMadMatAyNoeLT9--7WNb0K-x2dvz6dI9vz8d8_rliDG9b6zb2xGTOMsizljEchbJOJTslWtW1YTm-GtHzBkBXy52gB_vAnw_wITV7l7hWhY47nZaq-YWRTLhqahjFlcZU3WSQq54bCpBqdB1xZUUAiQYQf7-AR_Xce4:1rgN3s:GlqAueVchPxBWIEnnZCw_h9laxg"
projectID = "950783494"

session = scratch3.Session(session_id=sessionID, username="YoussefTV")
conn = session.connect_cloud(projectID)

client = scratch3.CloudRequests(conn)
events = scratch3.WsCloudEvents(projectID, conn)


@client.request
def balance(argument1):
    print(f"Balance requested for user {argument1}")
    return ["NOTICE:",
            "The ScratchCredit API hasn't been implemented yet, but the request has still been ",
            f"recieved successfully either way. (Balance requested by {argument1})",
            "Your balance will be automatically set to 100 ScratchCredits when the API gets ",
            "up and running. If the API were to be implemented, it would've only outputted this:",
            "100"]


@client.request
def give_sc(argument1, argument2):
    args2and3 = argument2.split()
    print(f"{args2and3[0]} requested giving {args2and3[1]} SC to {argument1}")
    return ["NOTICE:",
            "The ScratchCredit API hasn't been implemented yet, but the request has still been ",
            "recieved successfully either way.",
            f"({args2and3[0]} tried giving {args2and3[1]} SC to {argument1})",
            f"You'll be able to give {args2and3[1]} SC to {argument1} when the API gets up and running.",
            "THANKS FOR THE GENEROSITY, THOUGH!"]


@client.event
def on_ready():
    print("\033[1mScratchCredit's server has gone up and is currently receiving requests!\n\033[0mNow people can start using ScratchCredit!")


@client.event
def on_request(request):
    print("Received request", request.name, request.requester, request.arguments, request.timestamp, request.id)


client.run(thread=True)
