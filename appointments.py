from flask_discord_interactions import (
    Message,
    Embed,
    Modal,
    Autocomplete,
    DiscordInteractionsBlueprint,
    Option,
)
from autocomplete import autocomplete_handler
from appt_fields import get_fields
from api import save_appointment, save_student

bp = DiscordInteractionsBlueprint()

bp.add_autocomplete_handler(autocomplete_handler, "appt")


@bp.command(
    options=[
        Option(name="student", type=str, required=True, description="required", autocomplete=True),
        Option(name="student2", type=str, required=False, description="optional", autocomplete=True),
        Option(name="student3", type=str, required=False, description="optional", autocomplete=True)
    ]
)
def appt(ctx, student: str, student2: str="", student3: str=""):
    """Form to submit an appointment with students"""
    print(student, student2, student3)
    fields = get_fields(student, student2, student3)
    return Modal("appt", "Appointment Info", fields)


@bp.custom_handler("appt")
def modal_callback(ctx):
    """Handle user submitted data through the appointment modal"""

    data = {}
    for component in ctx.components:
        field_prop = component.components[0]
        data[field_prop.custom_id.lower()] = field_prop.value

    students = data["students"]
    if ',' in students:
        student_list = students.split(', ')
        for student in student_list:
            firstname, lastname = student.split(' ')
            save_student(firstname, lastname)
    else:
        student_list = [students]
        firstname, lastname = students.split(' ')
        save_student(firstname, lastname)

    message_embed = Embed(
        title="Appointment Submitted", description=(format_output(data))
    )

    data["students"] = student_list
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
