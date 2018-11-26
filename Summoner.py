import requests
from AbstractClassDeveloper import Invocador
from AbstractClassDeveloper import AbstractSummoner
import sys

class AppInvocador(AbstractSummoner):

    def DatosSummoner(self, summoner):
        key = 'RGAPI-2fccde75-639d-4139-bfa2-e267b83e68ff'
        region = 'la1'

        chall_r = requests.get('https://' + region + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summoner + '?api_key=' + key)
        if(chall_r.status_code == 200):
            chall_J = chall_r.json()
            Id = chall_J['id']
            Name = chall_J['name']
            Level = chall_J['summonerLevel']

        chall_m = requests.get('https://' + region + '.api.riotgames.com/lol/league/v3/positions/by-summoner/' + str(Id) + '?api_key=' + key)

        if(chall_m.status_code == 200):
            chall_n = chall_m.json()

        Wins = 0
        Losses = 0
        Tier = 'No tiene rankeds'

        for i in chall_n:
            if i['queueType'] == 'RANKED_SOLO_5x5': #Veriacion que sea el diccionario de soloQ
                Wins = i['wins']
                Losses = i['losses']
                Tier = i['tier']

        #Comportamimento = "aqui va el comportamiento"
        return Invocador(Id, Name, Level, Wins, Losses, Tier)

##############################################################################################################################################
if __name__ == "__main__":

    player = AppInvocador()

    invocador1 = player.DatosSummoner('l irving l')
    print(invocador1)