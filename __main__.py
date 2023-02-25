import lightbulb
import hikari
import miru
import asyncio
import asyncpg
from credentials import bot_creds
from views import BaseView


class OverriddenBot(lightbulb.BotApp):
    def __init__(self):
        print(bot_creds["TOKEN"], type(bot_creds["TOKEN"]))
        super().__init__(token=bot_creds["TOKEN"], prefix="!", intents=hikari.Intents.ALL)

bot = OverriddenBot()
miru.load(bot)

@bot.listen()
async def startup_function(event: hikari.StartedEvent) -> None:
    persistent_views = [
    BaseView
    ]

    for view in persistent_views:
        view.start_listener()
    print("Persistent views have been started.")

    try:
        bot.d.pool = await asyncpg.create_pool(
        "postgres://postgres:xwb_con_^^_203@database:5432/postgres"
    )
        print("POSTGRESQL connected = ", bot.d.pool)
    except Exception as e:
        print('Something went wrong:', e)

    bot.load_extensions("lightbulb.ext.filament.exts.superuser")

@bot.command()
@lightbulb.command("ping", "A simple command to check bot's functionality")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Pong! @ {bot.heartbeat_latency*1000}ms")

bot.run()
