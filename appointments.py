from flask_discord_interactions import (
    Message,
    Embed,
    Modal,
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
        Option(name="student3", type=str, required=False, description="optional", autocomplete=True),
        Option(name="student4", type=str, required=False, description="optional", autocomplete=True)
    ]
)
def appt(ctx, student: str, student2: str="", student3: str="", student4: str=""):
    """Form to submit an appointment with students"""
    fields = get_fields(student, student2, student3, student4)
    return Modal("appt", "Appointment Info", fields)


@bp.custom_handler("appt")
def modal_callback(ctx):
    """Handle user submitted data through the appointment modal"""

    data = {}
    for component in ctx.components:
        field_prop = component.components[0]
        data[field_prop.custom_id] = field_prop.value

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
        title="**Appt** with **" + data["students"] + "**",
        description=(data["date"] + "\n" + data["fulltimers"] + "\n\n" + data["notes"] ),
        color=3447003, # blue, google Discord color codes if you want to change
    )

    data["students"] = student_list
    # Save DATA TO DB
    save_appointment(data)

    return Message(embed=message_embed)
