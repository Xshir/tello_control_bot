import lightbulb
import hikari
import miru
import asyncio
import asyncpg
from credentials import bot_creds, db_creds
from views import BaseView
#from lightbulb.ext import tasks


class OverriddenBot(lightbulb.BotApp):
    def __init__(self):
        print(bot_creds["TOKEN"], type(bot_creds["TOKEN"]))
        super().__init__(token=bot_creds["TOKEN"], prefix="!", intents=hikari.Intents.ALL)

bot = OverriddenBot()
miru.load(bot)
#tasks.load(bot)



@bot.listen()
async def startup_function(event: hikari.StartedEvent) -> None:
    persistent_views = [
    BaseView()
    ]

    for view in persistent_views:
        view.start_listener()
    print("Persistent views have been started.")

    try:
        bot.d.pool = await asyncpg.create_pool(
        f"postgres://{db_creds['user']}:{db_creds['password']}@{db_creds['host']}:{db_creds['port']}/{db_creds['database']}"
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

@bot.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command(
    "update",
    "executes a git pull before killing the bot, the restart should be handled by a process manager",
)
@lightbulb.implements(lightbulb.PrefixCommand)
async def update_git_backup(ctx: lightbulb.Context) -> None:

    
    RET = f"```bash\ngit pull https://github.com/Xshir/tello_control_bot\n```"

    async def run(cmd):
        ret_stdout_ = "```\n**[stdout]**\nNO STDOUT\n```"
        ret_stderr_ = "```\n**[stderr]**\nNO STDERR\n```"
        proc = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await proc.communicate()
        

        if stdout:
            ret_stdout_ = f"```\n**[stdout]**\n{stdout.decode()}\n```"
            
        if stderr:
            ret_stderr_ = f"```\n**[stderr]**\n{stderr.decode()}\n```"
        
        tup = ('Bot App will restart now.', ret_stdout_, ret_stderr_)
        return tup

    tup_ = await run(RET)
    desc = "\n".join((tup_[1], tup_[2]))
    embed = hikari.Embed(title=tup_[0], description=desc, colour=(250, 250, 250))
    await ctx.respond(embed)

    await ctx.bot.close()

@bot.command()
@lightbulb.add_checks(
    lightbulb.checks.has_guild_permissions(hikari.Permissions.ADMINISTRATOR)
    | lightbulb.owner_only
)
@lightbulb.command("console", "Tello Control Console")
@lightbulb.implements(lightbulb.PrefixCommand)
async def prefix_setter(ctx: lightbulb.Context) -> None:
    view = BaseView() # view obj

    response = await ctx.respond(
        embed=hikari.Embed(
            description=
                f"Embed"
            ,
            colour=(255, 255, 255),
        ),
        components=view.build(),
    )
    await view.start(await response.message())
    await view.wait()

@bot.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("restart", "restarts the bot")
@lightbulb.implements(lightbulb.PrefixCommand)
async def restart(ctx: lightbulb.Context) -> None:
    await ctx.respond("Attempting to restart.")
    await ctx.bot.close()
    await ctx.respond("Attempt failed.")

bot.run()
