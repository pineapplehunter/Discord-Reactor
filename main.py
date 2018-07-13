import discord
from config.token import TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
    author = reaction.message.author
    await client.send_message(author, f"{user} さんがリアクションをしました")

    print(f"sent message to {author}")


client.run(TOKEN)
