import hikari
import miru
from funcs import retrieve_tello_instructions_in_list

class BaseView(miru.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.state = hikari.MessageFlag.EPHEMERAL

    @miru.button(label="START STATUS", style=hikari.ButtonStyle.SECONDARY, custom_id="start_stat")
    async def start_stat(self, button: miru.Button, ctx: miru.ViewContext):
            pool = ctx.bot.d.pool

            tellos = []

            for _ in range(0, 10):
                tellos.append(f"tello{_}")

            async with pool.acquire() as conn:
                
                rec = await conn.fetch(f"SELECT * FROM tello_table WHERE key = 500")
                em = []
                for row in rec:
                      em.append(row[1])
                await ctx.respond(em, flags=self.state)
                await conn.close()

    @miru.button(label="START ALL", style=hikari.ButtonStyle.SECONDARY, custom_id="start_all")
    async def start_all_tellos(self, button: miru.Button, ctx: miru.ViewContext):
            pool = ctx.bot.d.pool

            tellos = []

            for _ in range(0, 10):
                tellos.append(f"tello{_}")

            async with pool.acquire() as conn:
                for tello in tellos:
                        await conn.execute(f"UPDATE tello_table SET {tello} = 'NOW' WHERE key = 500;")
                await ctx.respond("Done", flags=self.state)
                await conn.close()
                
    
    @miru.button(label="RESET ALL", style=hikari.ButtonStyle.SECONDARY, custom_id="reset_all")
    async def reset_all_tellos(self, button: miru.Button, ctx: miru.ViewContext):
            pool = ctx.bot.d.pool

            tellos = []

            for _ in range(0, 10):
                tellos.append(f"tello{_}")

            async with pool.acquire() as conn:
                for tello in tellos:
                        await conn.execute(f"UPDATE tello_table SET {tello} = 'NOT SET' WHERE key = 500;")
                await ctx.respond("Done", flags=self.state)
                await conn.close()
                
        

    @miru.button(label="tello0", style=hikari.ButtonStyle.SECONDARY, custom_id="id_0")
    async def tello0(self, button: miru.Button, ctx: miru.ViewContext):
        STRING = await retrieve_tello_instructions_in_list(ctx.bot.d.pool, "tello0")
        await ctx.respond(STRING, flags=self.state)

    @miru.button(label="tello1", style=hikari.ButtonStyle.SECONDARY, custom_id="id_1")
    async def tello1(self, button: miru.Button, ctx: miru.ViewContext):
            STRING = "Test String"
            await ctx.respond(STRING, flags=self.state)


    @miru.button(label="tello2", style=hikari.ButtonStyle.SECONDARY, custom_id="id_2")
    async def tello2(self, button: miru.Button, ctx: miru.ViewContext):
            STRING = "Test String"
            await ctx.respond(STRING, flags=self.state)


    @miru.button(label="tello3", style=hikari.ButtonStyle.SECONDARY, custom_id="id_3")
    async def tello3(self, button: miru.Button, ctx: miru.ViewContext):
            STRING = "Test String"
            await ctx.respond(STRING, flags=self.state)


    @miru.button(label="tello4", style=hikari.ButtonStyle.SECONDARY, custom_id="id_4")
    async def tello4(self, button: miru.Button, ctx: miru.ViewContext):
            STRING = "Test String"
            await ctx.respond(STRING, flags=self.state)


    @miru.button(label="tello5", style=hikari.ButtonStyle.SECONDARY, custom_id="id_5")
    async def tello5(self, button: miru.Button, ctx: miru.ViewContext):
            STRING = "Test String"
            await ctx.respond(STRING, flags=self.state)


    @miru.button(label="tello6", style=hikari.ButtonStyle.SECONDARY, custom_id="id_6")
    async def tello6(self, button: miru.Button, ctx: miru.ViewContext):
            STRING = "Test String"
            await ctx.respond(STRING, flags=self.state)


    @miru.button(label="tello7", style=hikari.ButtonStyle.SECONDARY, custom_id="id_7")
    async def tello7(self, button: miru.Button, ctx: miru.ViewContext):
            STRING = "Test String"
            await ctx.respond(STRING, flags=self.state)


    @miru.button(label="tello8", style=hikari.ButtonStyle.SECONDARY, custom_id="id_8")
    async def tello8(self, button: miru.Button, ctx: miru.ViewContext):
            STRING = "Test String"
            await ctx.respond(STRING, flags=self.state)


    @miru.button(label="tello9", style=hikari.ButtonStyle.SECONDARY, custom_id="id_9")
    async def tello9(self, button: miru.Button, ctx: miru.ViewContext):
            STRING = "Test String"
            await ctx.respond(STRING, flags=self.state)
    

    