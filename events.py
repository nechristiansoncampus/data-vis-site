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
from api import save_student, get_students, save_event, add_one_attendee_to_event, get_event

bp = DiscordInteractionsBlueprint()
event_data = {}
event_id = None

# constant variable to be used in the student select menu in the case that
# you create an event and all the students at the event have never been met before
# admittedly a rare edge case but an edge case nonetheless
ADD_NEW_STUDENT = "NEED TO ADD NEW STUDENT"

@bp.command()
def event(ctx):
    """Form to submit an event with attendance"""
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
        title=f"Select students attending {event_data['name']}",
        description=("Students attending so far: \n"),
        color=color_coding(event_data['name']),
    )
    students = get_students() + [ADD_NEW_STUDENT]
    options = [SelectMenuOption(label=name, value=name) for name in students]
    menu = SelectMenu(
        placeholder="Select students attending event!",
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
    if ADD_NEW_STUDENT in ctx.values:
        ctx.values.remove(ADD_NEW_STUDENT)
    event_data["attendees"] = ctx.values
    global event_id
    event_id = None
    event_id = save_event(event_data)
    return students_attending_msg(event_data)


def students_attending_msg(event_data, replace_last_msg=False):
    attendee_count = len(event_data["attendees"])
    attendee_string = ", ".join(event_data["attendees"])

    message_embed = Embed(
        title=f"{event_data['name']} on {event_data['date']}",
        description=("\n" + event_data["notes"] + "\n\n" + "**" + str(attendee_count) + "**" + " students attended:" + "\n" + attendee_string),
        color=color_coding(event_data['name']),
    )
    return Message(
        embed=message_embed,
        components=[
            ActionRow(
                components=[
                    Button(
                        style=ButtonStyles.PRIMARY,
                        custom_id=[handle_add_click, event_id],
                        label="Add New Student!",
                    )
                ]
            )
        ],
        update=replace_last_msg,
    )


@bp.custom_handler()
def handle_add_click(ctx, event_id):
    fields = add_student_fields(event_id)
    return Modal("add", "Add Student", fields)


@bp.custom_handler("add")
def response_msg(ctx):
    new_student_firstname = ctx.get_component("firstname").value
    new_student_lastname = ctx.get_component("lastname").value
    event_id = ctx.get_component("event_id").value
    fullname = new_student_firstname + " " + new_student_lastname
    save_student(new_student_firstname, new_student_lastname)
    db_event_data = add_one_attendee_to_event(event_id, fullname)
    return students_attending_msg(db_event_data, replace_last_msg=True)


def color_coding(event_name):
    """
    function that color codes events based on key words in event name
    https://gist.github.com/thomasbnt/b6f455e2c7d743b796917fa3c205f812

    event_name - (str) name of event
    """
    # this should catch Bible study
    if "bible" in event_name.lower():
        return 15844367 # gold
    # this should catch home meeting
    elif "home" in event_name.lower():
        return 2067276 # green
    # this should catch church meetings (aka LD and prayer)
    elif "meeting" in event_name.lower():
        return 1146986 # dark aqua
    # this should catch IPMM
    elif "ipmm" in event_name.lower() or "intercollegiate" in event_name.lower():
        return 11342935 # dark vivid pink
    # all others
    return 7419530 # dark purple
    