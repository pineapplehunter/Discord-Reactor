import discord
from config.token import TOKEN


class Reactor(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User):
        author = reaction.message.author
        await author.send(f"{user} さんがリアクションをしました")
        print(f"sent message to {author}")


bot = Reactor()
bot.run(TOKEN)
