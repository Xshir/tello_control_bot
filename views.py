import hikari
import miru

class BaseView(miru.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.state = hikari.MessageFlag.EPHEMERAL


    @miru.button(label="MODAL1", style=hikari.ButtonStyle.SECONDARY, custom_id="id_1")
    async def information(self, button: miru.Button, ctx: miru.ViewContext):
        STRING = "Test String"
        await ctx.respond(STRING, flags=self.state)

    @miru.button(label="MODAL2", style=hikari.ButtonStyle.SECONDARY, custom_id="id_2")
    async def booking(self, button: miru.Button, ctx: miru.ViewContext):
        modal = miru.Modal(title="MODAL TITLE", timeout=None) # modal object

        # input objects
        TEXTINPUT_1 = miru.TextInput(
            label="TEXT 1 LABEL",
            required=True,
            min_length=2,
            max_length=15,
        )
        TEXTINPUT_2 = miru.TextInput(
            label="TEXT 2 LABEL",
            required=True,
            min_length=5,
            max_length=20,
        )

        # add input objects to modal object
        modal.add_item(TEXTINPUT_1)
        modal.add_item(TEXTINPUT_2)

        # sends the modal after button click
        await ctx.respond_with_modal(modal)
        await modal.wait() # waits for a resp
        responses = []
        for k, v in modal.values.items():
            responses.append(v) #responses[0] is 1st text input, responses[1] is 2nd text input etc etc
        
        await ctx.respond(f"{responses[0]}") # sends response(s) to discord via ephemeral (self.state)