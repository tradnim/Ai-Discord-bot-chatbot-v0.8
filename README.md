# Discord Chatbot

This is a chatbot that uses a custom AI model via the LM Studio API. It allows you to set a specific channel for the bot to respond in, and the bot will only respond in that channel.

## Features
- Use a slash command `/setchannel` to set the channel where the bot can talk.
- The bot will only respond to messages in the designated channel.
- The bot uses an AI model via LM Studio API to generate responses to user messages.

## Setup
- Replace The Discord bot id
- Replace The localhost and the model name
### 1. Prerequisites

- Python 3.8 or higher
- A Discord bot token (from the [Discord Developer Portal](https://discord.com/developers/applications))
- LM Studio API running locally (or accessible over the network)
- Install the necessary Python packages

### 2. Install Dependencies

Run the following command to install the required packages:

```bash
pip install discord.py requests


