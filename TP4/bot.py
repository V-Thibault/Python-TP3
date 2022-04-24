
from discord import Client
import logging
from argparse import ArgumentParser
import json
from logger import Logger
from commande import commande

class MyBot(Client):

    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")


    async def on_message(self,message):
        com=commande()
        await com.Feur(message)
        await com.DEL(message)
        await com.Help(message)
        msg=(f"{message.author} écrit: {message.content}")
        Logger.Print_log(msg)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", help="Config file", required=True, dest="config")
    return parser.parse_args()
 


args=parse_args()
file=json.load(open(args.config))
client= MyBot()

client.run(str(file["token"]))



