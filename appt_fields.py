from datetime import date
from flask_discord_interactions import ActionRow, TextInput


def get_fields(student, *args):
    """
    Populate and return fields needed for form(modal)
    
    Args may contain students in the case that an appointment was with multiple students
    """
    student_fill = student
    for stud in args:
        if stud:
            student_fill = student_fill + ", " + stud

    fields = [
        ActionRow(
            [
                TextInput(
                    "fulltimers",
                    "Fulltimers (comma seperated)",
                )
            ]
        ),
        ActionRow(
            [
                TextInput(
                    "students",
                    "Students (comma seperated)",
                    value=f"{student_fill}",
                )
            ]
        ),
        ActionRow(
            [
                TextInput(
                    "date",
                    "Enter the Date",
                    placeholder=str(date.today().strftime("%m/%d/%Y")),
                    value=str(date.today().strftime("%m/%d/%Y")),
                )
            ]
        ),
        ActionRow(
            [
                TextInput("notes", "Notes", required=False),
            ],
        ),
    ]
    return fields
