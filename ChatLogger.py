import discord
import aiohttp
from io import BytesIO

client = discord.Client()

@client.event
async def on_ready():
    print(f"[Online] {client.user}")

@client.event
async def on_message(message):
    if message.channel.id != 0000000000000: # Put channel ID here
        return

    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(
            "https://discord.com/api/webhooks/....", # Your webhook URL here
            session=session
        )

        content = message.content or None

        files = []
        for attachment in message.attachments:
            async with session.get(attachment.url) as resp:
                if resp.status == 200:
                    data = await resp.read()
                    files.append(discord.File(BytesIO(data), filename=attachment.filename))

        if content or files:
            await webhook.send(
                content=content,
                files=files,
                username=message.author.name,
                avatar_url=str(message.author.display_avatar.url)
            )

if __name__ == "__main__":
    client.run("YOUR_TOKEN_HERE") # Your ACCOUNT token here; Do not put a bot token!
