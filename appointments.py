from flask_discord_interactions import (
    Message,
    Embed,
    Modal,
    Autocomplete,
    DiscordInteractionsBlueprint,
)
from autocomplete import autocomplete_handler
from modal_fields import get_fields
from api import save_appointment

bp = DiscordInteractionsBlueprint()

bp.add_autocomplete_handler(autocomplete_handler, "appointment")


def format_output(data):
    """Format the output for visual consumption within the context of discord upon submission"""
    output = ""
    for name, values in data.items():
        if values != "":
            output = output + f"{name}:\n  {values}" + "\n\n"
    return output


@bp.custom_handler("appointment")
def modal_callback(ctx):
    """Handle user submitted data through the appointment modal"""

    data = {}
    for component in ctx.components:
        field_prop = component.components[0]
        data[field_prop.custom_id] = field_prop.value

    message_embed = Embed(
        title="Appointment Submitted", description=(format_output(data))
    )

    # Save DATA TO DB
    save_appointment(data)

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
    """Form to submit an appointment with students"""
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
