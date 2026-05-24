TOKEN = os.getenv("TOKEN")

import discord
import random
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

keywords = ["初音ミク", "ミク", "みく", "39"]

replies = [
    "ミク呼んだ？🎤✨",
    "39！🩵",
    "ミクだよ♪",
    "呼ばれた気がした！",
    "ねえねえ、なに〜？","誰か、助けてね(^^♪","いますぐ輪廻！！","もう一回、もう一回","死ぬまでピュアピュアやってんのん？🐇","ほざくな馬鹿め。","誰に会ってもときめかない..あ！あ！あ！あたし以外にときめかない..？"
]

@client.event
async def on_ready():
    print(f"起動したよ: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if any(word in message.content for word in keywords):
        await message.channel.send(random.choice(replies))

client.run(TOKEN)
