import threading
import os
import subprocess
import time

os.system('pip install scratchattach local-simple-database Flask')

print('\033[1m===== ScratchCredit Server =====\033[0m')
print("--------------------------------")

def kill_process_by_name(name):
    subprocess.call(['pkill', '-f', name])


def api():
    os.system("python API.py")


def server():
    os.system("python server.py")


t = threading.Thread(target=api, args=())
t2 = threading.Thread(target=server, args=())
t.start()
t2.start()
