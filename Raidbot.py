import discord
from discord import app_commands

class BotClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = BotClient()

@client.tree.command(name="say")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def say(interaction: discord.Interaction, message: str, ghost: bool = False):
    await interaction.response.send_message(".", ephemeral=True)
    FUCK_YOU_YXORD = await interaction.followup.send(
        message,
        ephemeral=False,
        wait=True
    )

    if ghost:
        await FUCK_YOU_YXORD.delete()

class Nagger(discord.ui.View):
    def __init__(self, message: str):
        super().__init__()
        self.message = message

    @discord.ui.button(label="spam", style=discord.ButtonStyle.danger)
    async def fl00d(self, interaction: discord.Interaction, button: discord.ui.Button):
        for _ in range(5):
            await interaction.followup.send(self.message, ephemeral=False)


@client.tree.command(name="spam")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def spam(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(view=Nagger(message), ephemeral=True)

client.run("")
