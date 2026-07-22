"""Developer tools command - requires DEVELOPER_IDS."""

import discord
from discord import app_commands

from src.core.command import Command, CommandHelpInfo
from src.services.environment import Environment


class DevCommand(Command):
    help_info = CommandHelpInfo(
        name="dev",
        description="Developer tools (requires DEVELOPER_IDS)",
        usage="/dev <info|sync>",
        examples=["/dev action:info", "/dev action:sync"],
        category="Developer",
    )

    developer_only = True

    def register(self, tree: app_commands.CommandTree) -> None:
        @tree.command(name="dev", description="Developer tools")
        @app_commands.describe(action="What to do")
        @app_commands.choices(action=[
            app_commands.Choice(name="info", value="info"),
            app_commands.Choice(name="sync", value="sync"),
        ])
        async def dev(interaction: discord.Interaction, action: app_commands.Choice[str]) -> None:
            if not await self.guard(interaction):
                return
            if action.value == "info":
                await self._show_info(interaction)
            elif action.value == "sync":
                await self._sync_tree(interaction, tree)

    async def execute(self, interaction: discord.Interaction) -> None:
        await self._show_info(interaction)

    async def _show_info(self, interaction: discord.Interaction) -> None:
        config = Environment.get_config()
        client = interaction.client
        await interaction.response.send_message(
            f"🛠️ **Developer Info**\n"
            f"🌐 Guilds: {len(client.guilds)}\n"
            f"⚙️ Environment: {config.environment}\n"
            f"👤 Developers configured: {len(config.developer_ids)}",
            ephemeral=True,
        )

    async def _sync_tree(self, interaction: discord.Interaction, tree: app_commands.CommandTree) -> None:
        await interaction.response.defer(ephemeral=True)
        synced = await tree.sync()
        await interaction.followup.send(f"✅ Synced {len(synced)} application commands.")
