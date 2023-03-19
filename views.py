import hikari
import miru

class BaseView(miru.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.state = hikari.MessageFlag.EPHEMERAL


    @miru.button(label="tello0", style=hikari.ButtonStyle.SECONDARY, custom_id="id_0")
    async def tello0(self, button: miru.Button, ctx: miru.ViewContext):
        STRING = "Test String"
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
    

    