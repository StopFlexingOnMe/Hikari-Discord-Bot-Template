import hikari
import lightbulb

example_plugin = lightbulb.Plugin("example plugin")


@example_plugin.command
@lightbulb.command("Ping", "responds with pong")
async def ping_command(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")


def load(bot):
    bot.add_plugin(example_plugin)

def unload(bot):
    bot.remove_plugin(example_plugin)