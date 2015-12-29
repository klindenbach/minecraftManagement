import sys
import subprocess
import random 

PLAYERFILE = "/home/minecraft/known-players.txt"

'''
  EDIT HERE TO CHANGE MINECRAFT COMMAND
'''
def getCommand(uuid):
    teams = ['Kalokairi', 'Fons', 'Mavet',	'Bagno']
    return "scoreboard teams join "  + teams[random.randint(0,10000000) % 4] + " " + uuid

def main():
    while 1:
        line = sys.stdin.readline()
        if line == "":
            break
        elif "Starting minecraft" in line:
            log("Scraping Started")
        elif "UUID of player" in line:
            uuid = line.split()[-1]

            if not isKnownPlayer(uuid):
                addNewPlayer(uuid)
                executeNewPlayer(uuid)

def log(s):
    print ">>>>>>>>>>>>>>>>>>>>>FILTER.PY>>>>>>>>>>>>>>>>>>>>"
    print s
    print "<<<<<<<<<<<<<<<<<<<<<FILTER.PY<<<<<<<<<<<<<<<<<<<<"

def isKnownPlayer(uuid):
    try:
        with open(PLAYERFILE, "r") as f:
            for line in f:
                if line.strip() == uuid:
                    return True
    except IOError:
        return False

    return False

def addNewPlayer(uuid):
    with open(PLAYERFILE, "a") as f:
        f.write(uuid + "\n")

    log("Added " + uuid)

def executeNewPlayer(uuid):

    command = getCommand(uuid)

    log("RUNNING: " + command)
    subprocess.call([
        'screen', '-S', 'minecraft', '-p', '0', '-X', 'stuff',
        command + '\r'
    ])
    


if __name__ == "__main__":
    main()
