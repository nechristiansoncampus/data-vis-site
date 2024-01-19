from flask_discord_interactions import (
    Message,
    Embed,
    Modal,
    Autocomplete,
    DiscordInteractionsBlueprint,
)
from autocomplete import autocomplete_handler
from appt_fields import get_fields
from api import save_appointment

bp = DiscordInteractionsBlueprint()

bp.add_autocomplete_handler(autocomplete_handler, "appt")


@bp.command()
def appt(ctx, student: Autocomplete(str)):
    """Form to submit an appointment with students"""
    fields = get_fields(student)
    return Modal("appointment", "Appointment Info", fields)


@bp.custom_handler("appt")
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


def format_output(data):
    """Format the output for visual consumption within the context of discord upon submission"""
    output = ""
    for name, values in data.items():
        if values != "":
            output = output + f"{name}:\n  {values}" + "\n\n"
    return output
