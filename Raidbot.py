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
    msg = await interaction.followup.send(message, ephemeral=False, wait=True)
    if ghost:
        await msg.delete()


class jeffreysballs(discord.ui.View):
    def __init__(self, message: str):
        super().__init__()
        self.message = message

    @discord.ui.button(label="spam", style=discord.ButtonStyle.danger)
    async def fl00d(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(".", ephemeral=True)
        for _ in range(5):
            await interaction.followup.send(self.message, ephemeral=False)


@client.tree.command(name="spam")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def spam(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(view=jeffreysballs(message), ephemeral=True)


class ilovewomenwithbigboobs(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Send", style=discord.ButtonStyle.green, custom_id="poll_raid_send")
    async def send_poll(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)

        try:
            import datetime
            poll = discord.Poll(
                question=discord.PollMedia(text="spammed"),
                duration=datetime.timedelta(hours=24),
            )
            for _ in range(10):
                poll.add_answer(text="spammed")
            for _ in range(5):
                await interaction.followup.send(poll=poll)
            await interaction.followup.send("poll sent", ephemeral=True)
        except discord.HTTPException as e:
            await interaction.followup.send(f"failed: {e}", ephemeral=True)


@client.tree.command(name="poll-raid")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def poll_raid(interaction: discord.Interaction):
    await interaction.response.send_message(
        "press the button to send a poll",
        view=ilovewomenwithbigboobs(),
        ephemeral=True,
    )


client.run("put-yo-token")
