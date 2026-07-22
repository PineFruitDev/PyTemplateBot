"""Main entry point for the Discord bot."""

import discord
from dotenv import load_dotenv

from src.commands import ALL_COMMANDS
from src.core.bot import Bot
from src.services.environment import Environment
from src.services.logger import get_logger

log = get_logger("Main")

# Load environment variables
load_dotenv()


def main() -> None:
    Environment.validate()
    config = Environment.get_config()

    log.info("Initializing bot with %d commands", len(ALL_COMMANDS))

    intents = discord.Intents.default()
    bot = Bot(ALL_COMMANDS, intents=intents)

    bot.run(config.discord_token, log_handler=None)


if __name__ == "__main__":
    main()
