from dotenv import load_dotenv
from typing import Final
import os
from discord import Intents, Client, Message
from response import get_response
from storage import load_counts

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

swear_count = load_counts()
count_dictionary = {}
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Intents not enabled properly")
        return

    if is_private := user_message[0] == "@":
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message, message.author, swear_count, count_dictionary)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is running.')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel} {username}: {user_message}")
    await send_message(message, user_message)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
