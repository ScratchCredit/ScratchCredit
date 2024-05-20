import scratchattach as scratch3
import sc_debugging as debugging

# TODO: Put this in a secret
sessionID = ".eJxVj8FugzAQRP_F54RiDNjklqqnSO0haivRC1rsNbiAnYIRUqr-e22JS26rmZ3Zt79kXXC2MCE5kdqty4La91j4nhxIA6vvm7jQGBV8ynIuuGB58DwuXjo3mBjc3Dygeky0IAe0MRY1tN5I8MbZZDeW5Iq3cRef9-XQ68IQQlph2TItskyrvJAcoFKgZVVkTCoF7HT8qK-oL9NYST--Tu94eenuP1_8c91Czeg6Y4_mFpoyypOM0oRWNBEsQo5guxW6SB5uHYj6DoJrvJnw7myUzxPOAe3pDbemDs89vtbD0kdEbJGC1pBy3mqq2yoVQgFngTyVOU1pWbCSCvL3D-NrddA:1s8LHE:a7I5ArAhl5Di-J1u-UZEJ3yUn30"
projectID = "1000486809"

session = scratch3.Session(session_id=sessionID, username="Youssefthe5th")
conn = session.connect_cloud(projectID)

client = scratch3.CloudRequests(conn)
events = scratch3.WsCloudEvents(projectID, conn)

is_debug_mode_enabled = True

debug = debugging.DebugMode(debug_mode=is_debug_mode_enabled, session=session)


@client.request
def sc_balance(argument1: str):
    print(f"{argument1} requested their balance")
    return ["NOTICE:",
            "The ScratchCredit API hasn't been implemented yet, but the request has still ",
            "been recieved successfully either way.",
            f"({argument1} tried looking at their balance)",
            "Your balance will be automatically set to 100 ScratchCredits when the API gets ",
            "up and running. If the API were to be implemented, it would've only outputted:",
            "100 (or more, if you get more SC from hosting your own shop)",
            "COME BACK SOON!"]


@client.request
def give_sc(argument1: str, argument2: str):
    receipent = argument1
    args2and3 = argument2.split()
    giver = args2and3[0]
    sc_to_give = args2and3[1]
    
    print(f"{giver} requested giving {sc_to_give} SC to {receipent}")
    return ["NOTICE:",
            "The ScratchCredit API hasn't been implemented yet, but the request has still ",
            "been recieved successfully either way.",
            f"({giver} tried giving {sc_to_give} SC to {argument1})",
            f"You'll be able to give {sc_to_give} SC to {argument1} when the API gets up and running.",
            "THANKS FOR THE GENEROSITY, THOUGH!"]


@client.event
def on_ready():
    print("\033[1mScratchCredit's ScratchAttach server has gone up and is currently receiving requests!\n\033[0mNow people can start using ScratchCredit!")
    debug.print_if_debug_mode_is_enabled()


@client.event
def on_request(request):
    print("Received request:", request.name, request.requester, request.arguments, request.timestamp, request.id)


client.run(thread=True)
