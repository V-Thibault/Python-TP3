from discord import Client


class commande():

    def __init__(self):
        super().__init__()

    async def Feur(self,message):
        msg=message.content
        if msg.endswith("quoi"):
            await message.channel.send("feur")
        ####################################################
    async def DEL(self,message):
        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()
    #######################################################################
    async def Help (self,message):
        msg=message.content
        if msg.startswith("!help"):
            await message.channel.send("Liste des commandes :\n \n -> !del x (suprime les x dernier message) \n\n -> !help (affiche la liste des commandes)")