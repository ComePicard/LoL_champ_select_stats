from lcu_driver import Connector

connector = Connector()

#For some reason, the register executes the function 3 times, I use this variable to fix it... rather drunkenly I must agree
no_multiple = 0

@connector.ready
async def connect(connection):
    print("LCU Driver ready !")

#Listen to changes on the /lol-champ-select/v1/session endpoints, which is the responsible endpoint of champ select data, such as your position in the lobby
@connector.ws.register('/lol-champ-select/v1/session', event_types=('UPDATE',))
async def find_position(connection, event):
    cell = -1
    global no_multiple
    no_multiple +=1
    if(no_multiple%3 == 0) :
        get_cs_data = await connection.request('get', '/lol-champ-select/v1/session') #Get current summoner's Champ select data
        cs_data = await get_cs_data.json()
        if(cs_data["isCustomGame"]==True | cs_data["isSpectating"]!=True):
            cell = str(cs_data["localPlayerCellId"])
            print(f"You have been placed {int(cell)+1}")
            if(cell != -1):
                f = open("data_lol.txt", "a")
                f.write(cell)
                f.close
            else :
                print("ça a pô marché")
    return no_multiple

@connector.close
async def disconnect(connection):
    await connector.stop()

connector.start()

        