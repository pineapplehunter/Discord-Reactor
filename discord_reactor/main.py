import discord
from discord_reactor.config.token import TOKEN


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


def main():
    bot = Reactor()
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
