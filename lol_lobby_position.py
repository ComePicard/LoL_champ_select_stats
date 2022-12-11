from lcu_driver import Connector

connector = Connector()

@connector.ready
async def connect(connection):
    cell = -1
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    if summoner.status == 200 :
        summoner = await summoner.json()
        if(str(summoner["displayName"]) == "Cosmöx"):
            summoner = summoner['summonerId']
            get_cs_data = await connection.request('get', '/lol-champ-select/v1/session')
            cs_data = await get_cs_data.json()
            team_data = cs_data['myTeam']
            for x in range(len(team_data)):
                if(team_data[x]["summonerId"]==summoner):
                    cell = str(team_data[x]["cellId"]+1)
            
    print(cell)
    if(cell != -1):
        f = open("data_lol.txt", "a")
        f.write(cell)
        f.close
    else :
        print("ça a pô marché")

@connector.close
async def disconnect(connection):
    await connector.stop()

connector.start()

        