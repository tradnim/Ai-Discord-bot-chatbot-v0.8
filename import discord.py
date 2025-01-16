import discord
from discord.ext import commands
import requests

# Discord bot token (Make sure to replace this with your actual token)
DISCORD_TOKEN = "YOUR_DISCORD_TOKEN"

# LM Studio API URL
LM_API_URL = "http://localhost:Your-local-host/v1/chat/completions"

# Model name
MODEL_NAME = "Your-Model-name"

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Variable to store the allowed channel ID
allowed_channel_id = None


# Slash command to set the allowed channel
@bot.tree.command(name="setchannel", description="Set the channel where the bot can talk")
async def set_channel(interaction: discord.Interaction):
    global allowed_channel_id
    allowed_channel_id = interaction.channel.id
    await interaction.response.send_message(
        f"Okay! I will now only respond in this channel: {interaction.channel.mention}",
        ephemeral=True
    )


# Bot ready event
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync slash commands
    print(f"{bot.user} is now online and ready to chat!")


# Respond only in the allowed channel
@bot.event
async def on_message(message):
    global allowed_channel_id

    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the allowed channel is set and if the message is in the allowed channel
    if allowed_channel_id and message.channel.id != allowed_channel_id:
        return

    user_input = message.content.strip()
    print(f"User: {user_input}")

    # Prepare payload for AI response
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a friendly and casual AI who chats like a normal human."}, # change this to change the ai's personality and context
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.8,
        "max_tokens": 150,
        "stream": False
    }

    try:
        # Send request to LM Studio API
        response = requests.post(LM_API_URL, json=payload)
        response.raise_for_status()

        # Extract the AI's response
        ai_response = response.json().get("choices", [])[0].get("message", {}).get("content", "Sorry, I didn't quite catch that.")
        print(f"Bot: {ai_response}")

        # Send the AI's response back to the channel
        await message.channel.send(ai_response)

    except Exception as e:
        print(f"Error: {e}")
        await message.channel.send("Oops, something went wrong while trying to respond!")


# Run the bot
bot.run(DISCORD_TOKEN)
