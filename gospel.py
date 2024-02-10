from flask_discord_interactions import (
    Message,
    Embed,
    Modal,
    DiscordInteractionsBlueprint,
)
from autocomplete import autocomplete_handler
from gospel_fields import get_fields
from api import save_gospel

bp = DiscordInteractionsBlueprint()

@bp.command()
def gospel(ctx):
    """Form to submit stats from a gospel preaching time"""
    fields = get_fields()
    return Modal("gospel", "Gospel Stats", fields)

@bp.custom_handler("gospel")
def modal_callback(ctx):
    """Handle user submitted data through the gospel modal"""

    data = {}
    for component in ctx.components:
        field_prop = component.components[0]
        data[field_prop.custom_id] = field_prop.value

    message_embed = Embed(
        title="**Gospel** on **" + data["date"] + "**",
        description=("**\# of people contacted: " + data["numOfPeopleContacted"] + "\n" + "\# of tracts passed: " + data["numOfTractsPassed"] + "**\n\n" + data["notes"]),
        color=10038562, # dark red, google Discord color codes if you want to change
    )

    # Save DATA TO DB
    save_gospel(data)

    return Message(embed=message_embed)
