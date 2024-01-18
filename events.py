from flask_discord_interactions import (
    Message,
    Embed,
    Modal,
    DiscordInteractionsBlueprint,
    SelectMenu,
    SelectMenuOption,
    ActionRow,
    Button,
    ButtonStyles,
)
from event_fields import get_fields, add_student_fields

bp = DiscordInteractionsBlueprint()
test_students = ["Isaac", "Coven", "Cassia", "Ethan", "Luke", "Garett"]
event_data = {}


@bp.command()
def event(ctx):
    """Form to submit an event with attendance"""
    global event_data
    event_data = {}
    fields = get_fields()
    return Modal("event", "Event Info", fields)


@bp.custom_handler("event")
def modal_callback(ctx):
    """Handle user submitted data through the event modal"""
    data = {}
    for component in ctx.components:
        field_prop = component.components[0]
        data[field_prop.custom_id] = field_prop.value
    global event_data
    event_data = data
    return student_select_menu(data)


def student_select_menu(data, **kwargs):
    message_embed = Embed(
        title="Select Students Attending!",
        description=("Students attending so far: \n"),
    )
    options = [SelectMenuOption(label=name, value=name) for name in test_students]
    menu = SelectMenu(
        placeholder="Select Students attending event!",
        custom_id=handle_selected,
        options=options,
        max_values=len(options),
    )

    return Message(
        embed=message_embed, components=[ActionRow(components=[menu])], **kwargs
    )


@bp.custom_handler()
def handle_selected(ctx, **kwargs):
    global event_data
    event_data["attendees"] = ctx.values
    attendee_count = len(ctx.values)

    return Message(
        content=f"{attendee_count} students attending the {event_data['Name']}!",
        components=[
            ActionRow(
                components=[
                    Button(
                        style=ButtonStyles.PRIMARY,
                        custom_id=handle_click,
                        label="Add New Students!",
                    )
                ]
            )
        ],
    )


@bp.custom_handler()
def handle_click(ctx):
    fields = add_student_fields()
    return Modal("add", "Add Student", fields)


@bp.custom_handler("add")
def print_attendees(ctx):
    new_students = ctx.get_component("add_students").value.split(",")
    global event_data
    event_data["attendees"] = event_data.get("attendees", []) + new_students

    message_embed = Embed(
        title="Students attending the {event_data['Name']}",
        description=(f"{event_data['attendees']}\n"),
    )
    return Message(embed=message_embed)
