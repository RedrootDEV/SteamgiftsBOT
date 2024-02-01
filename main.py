import os
import time
import configparser
import client as clientLog

config = configparser.ConfigParser()

class valProject:
    def __init__(self):
        self._valLogs = False
        self._cookie = ""

    @property
    def valLogs(self):
        return self._valLogs

    @valLogs.setter
    def valLogs(self, value):
        self._valLogs = value

    @property
    def cookie(self):
        return self._cookie

    @cookie.setter
    def cookie(self, value):
        self._cookie = value

thisConfig = valProject()

def workingWithConfig():
    config.read('config.ini')
    thisConfig.cookie = config['DEFAULT'].get('cookie', "")
    thisConfig.valLogs = bool(config['DEFAULT'].get('log_info', False))
    if not config['DEFAULT'].get('cookie') or not config['DEFAULT'].get('log_info'):
        clientLog.askReadConfig(thisConfig.cookie, thisConfig.valLogs)

def run():
    from method.method import SteamGift as steamGif
    workingWithConfig()

    while True:
        try:
            # Coloca toda la lógica de tu aplicación aquí
            pinnedGames = False
            giftTYPE = 'All'
            minPoin = 20
            clientLog.createdLogs(thisConfig.valLogs)
            steamGif(thisConfig.cookie, giftTYPE, pinnedGames, minPoin).start()

        except Exception as e:
            print(f"Error: {str(e)}")
            print("Reiniciando la aplicación en 5 segundos...")
            time.sleep(5)

if __name__ == '__main__':
    run()
