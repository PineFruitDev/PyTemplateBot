# Discord Bot Template (Python)

A clean, modular Discord bot template with discord.py, featuring a command class pattern and single source of truth architecture. Python sibling of [TSTemplateBot](https://github.com/PineFruitDev/TSTemplateBot).

## Features

- **Single Source of Truth**: Add commands in one place, automatically available everywhere
- **Command Class Pattern**: Self-contained command classes with built-in validation
- **Environment Validation**: Comprehensive startup checks with helpful error messages
- **Auto-Generated Help**: Commands self-document with metadata
- **Contextual Logging**: Detailed logging with class and function context
- **Production Ready**: Error handling, validation, and clean architecture

## Quick Start

### 1. Setup

```bash
git clone <your-repo>
cd discord-bot-template-py
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### 2. Configure

Edit `.env` with your bot credentials:

```env
DISCORD_TOKEN=your_bot_token_here
DEVELOPER_IDS=your_user_id_here  # Optional
ENVIRONMENT=development          # Optional
```

### 3. Deploy

```bash
python register.py   # Register commands with Discord
python main.py       # Start the bot
```

## Project Structure

```
src/
├── core/
│   ├── bot.py                # Main bot class
│   ├── command.py            # Abstract command base
│   └── command_manager.py    # Command management
├── commands/
│   ├── __init__.py           # ← Command registry (single source of truth)
│   ├── ping.py               # Basic example
│   ├── info.py               # Embed example
│   ├── help_command.py       # Auto-generated help
│   └── dev.py                # Developer tools
└── services/
    ├── logger.py             # Contextual logging
    └── environment.py        # Config validation
main.py                       # Entry point
register.py                   # Command registration
```

## Adding Commands

### 1. Create Command Class

```python
# src/commands/my_command.py
import discord
from discord import app_commands

from src.core.command import Command, CommandHelpInfo


class MyCommand(Command):
    help_info = CommandHelpInfo(
        name="mycommand",
        description="Does something awesome",
        usage="/mycommand",
        examples=["/mycommand"],
        category="General",
    )

    def register(self, tree: app_commands.CommandTree) -> None:
        @tree.command(name="mycommand", description="My awesome command")
        async def mycommand(interaction: discord.Interaction) -> None:
            if not await self.guard(interaction):
                return
            await self.execute(interaction)

    async def execute(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello World!")
```

### 2. Register Command

```python
# src/commands/__init__.py
from src.commands.my_command import MyCommand

commands: list[Command] = [
    # ... existing commands
    MyCommand(),  # ← Add here
]
```

That's it! Your command is automatically:

- ✅ Registered with Discord
- ✅ Available in the bot
- ✅ Listed in help system
- ✅ Validated and logged

## Built-in Commands

- `/ping` - Basic ping/pong with latency
- `/info` - Bot information and statistics
- `/help [command]` - Auto-generated help system
- `/dev <info|sync>` - Developer tools (requires DEVELOPER_IDS)

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DISCORD_TOKEN` | ✅ | Bot token from Discord Developer Portal |
| `DEVELOPER_IDS` | ❌ | Comma-separated user IDs for developer commands |
| `ENVIRONMENT` | ❌ | Environment mode (defaults to production) |

## License

MIT License - See LICENSE file for details.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
