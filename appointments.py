from flask_discord_interactions import (
    Message,
    ActionRow,
    Embed,
    SelectMenu,
    SelectMenuOption,
    Modal,
    Autocomplete,
)
from autocomplete import autocomplete_handler
from modal_fields import get_fields
from flask_discord_interactions import DiscordInteractionsBlueprint

bp = DiscordInteractionsBlueprint()

bp.add_autocomplete_handler(autocomplete_handler, "appointment")

@bp.custom_handler("appointment")
def modal_callback(ctx):
    message_embed = Embed(title="Submitted", description=("Backend ctx data is" + str(ctx.components)
    ))
    return Message(embed=message_embed) 

    """
    TODO: REMOVE THE COMMENTED CODE ONCE TAKEN OUT FOR EVENTS

    THE COMMENTED OUT CODE WILL BE USEFUL FOR EVENTS. TO CALL A SELECT MENU TO
    TAKE ATTENDANCE. HOWEVER IT IS NOT NEEDED FOR APPOINTMENT. LEAVING AS BOILER
    PLATE CODE FOR NOW
    """
    # return make_appointment()

@bp.command()
def appointment(ctx, fulltimer: Autocomplete(str), student: Autocomplete(str)):
    fields = get_fields(fulltimer, student)
    return Modal("appointment", "Appointment Info", fields)

# def make_appointment(**kwargs):
#     message_embed = Embed(
#         title="Select Student attending",
#         description=(
#             "Students attending so far: \n"
#         ),
#     )

#     menu = SelectMenu(
#         placeholder="Select Students attending event!",
#         custom_id=handle_selected,
#         options=[
#             SelectMenuOption(
#                 label="Ben",
#                 value="Ben",
#                 description="Ben"
#             ),
#             SelectMenuOption(
#                 label="John",
#                 value="John",
#                 description="John"
#             ),
#         ],
#         max_values=2,
#     )

#     return Message(
#         embed=message_embed, components=[ActionRow(components=[menu])], **kwargs)


# @bp.custom_handler()
# def handle_selected(ctx, **kwargs):
#     message_embed = Embed(
#     title="Submitted",
#     description=(
#       "Backend ctx data is" + str(ctx.values)
#     ),
#     )
#     return Message(embed=message_embed)

