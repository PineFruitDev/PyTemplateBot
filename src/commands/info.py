"""Info command - bot statistics in an embed."""

import platform

import discord
from discord import app_commands

from src.core.command import Command, CommandHelpInfo


class InfoCommand(Command):
    help_info = CommandHelpInfo(
        name="info",
        description="Bot information and statistics",
        usage="/info",
        examples=["/info"],
        category="Utility",
    )

    def register(self, tree: app_commands.CommandTree) -> None:
        @tree.command(name="info", description="Bot information and statistics")
        async def info(interaction: discord.Interaction) -> None:
            if not await self.guard(interaction):
                return
            await self.execute(interaction)

    async def execute(self, interaction: discord.Interaction) -> None:
        client = interaction.client
        embed = (
            discord.Embed(title="🤖 Bot Information", color=0x5865F2)
            .add_field(name="📡 Latency", value=f"{round(client.latency * 1000)}ms", inline=True)
            .add_field(name="🌐 Servers", value=str(len(client.guilds)), inline=True)
            .add_field(name="🐍 Python", value=platform.python_version(), inline=True)
            .add_field(name="📚 discord.py", value=discord.__version__, inline=True)
        )
        embed.timestamp = discord.utils.utcnow()
        await interaction.response.send_message(embed=embed)
