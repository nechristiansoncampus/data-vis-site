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
from api import save_student, get_students

bp = DiscordInteractionsBlueprint()
test_students = ["Isaac", "Coven", "Cassia", "Ethan", "Luke", "Garett"]
event_data = {}


@bp.command()
def event(ctx):
    """Form to submit an event with attendance"""
    global event_data
    event_data = {}
    global test_students
    test_students = get_students()
    fields = get_fields()
    return Modal("event", "Event Info", fields)


@bp.custom_handler("event")
def event_modal_callback(ctx):
    """Handle user submitted data through the event modal"""
    data = {}
    for component in ctx.components:
        field_prop = component.components[0]
        data[field_prop.custom_id] = field_prop.value
    global event_data
    event_data = data
    return student_select_menu(data)


def student_select_menu(data, **kwargs):
    global event_data
    """Select menu to select from exisiting students for event attendees"""
    message_embed = Embed(
        title=f"Select Students Attending the {event_data['Name']}!",
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
        embed=message_embed,
        components=[ActionRow(components=[menu])],
        **kwargs,
    )


@bp.custom_handler()
def handle_selected(ctx, **kwargs):
    """Process data after attendees have been selected from existing students"""
    global event_data
    event_data["attendees"] = ctx.values

    return students_attending_msg(event_data["Name"], event_data["attendees"])


@bp.custom_handler()
def handle_add_click(ctx):
    fields = add_student_fields()
    return Modal("add", "Add Student", fields)


@bp.custom_handler("add")
def response_msg(ctx):
    print("FIRES EACH TIME?!")
    global event_data
    new_student_firstname = ctx.get_component("firstname").value
    new_student_lastname = ctx.get_component("lastname").value
    fullname = new_student_firstname + " " + new_student_lastname
    save_student(new_student_firstname, new_student_lastname)
    event_data["attendees"] = event_data.get("attendees", []) + [fullname]
    attendees = event_data["attendees"]
    return students_attending_msg(event_data["Name"], attendees, replace_last_msg=True)


def students_attending_msg(event_name, attendees, replace_last_msg=False):
    attendee_count = len(attendees)
    attendee_string = ", ".join(attendees)

    message_embed = Embed(
        title=f"{attendee_count} students attending the {event_name}:",
        description=(" \n\n" + attendee_string),
    )
    return Message(
        embed=message_embed,
        components=[
            ActionRow(
                components=[
                    Button(
                        style=ButtonStyles.PRIMARY,
                        custom_id=handle_add_click,
                        label="Add New Student!",
                    )
                ]
            )
        ],
        update=replace_last_msg,
    )
