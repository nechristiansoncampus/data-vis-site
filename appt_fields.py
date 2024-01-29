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
                    "Fulltimers",
                    "Fulltimers (comma seperated)",
                )
            ]
        ),
        ActionRow(
            [
                TextInput(
                    "Students",
                    "Students (comma seperated)",
                    value=f"{student_fill}",
                )
            ]
        ),
        ActionRow(
            [
                TextInput(
                    "Date",
                    "Enter the Date",
                    placeholder=str(date.today().strftime("%m/%d/%Y")),
                    value=str(date.today().strftime("%m/%d/%Y")),
                )
            ]
        ),
        ActionRow(
            [
                TextInput("Notes", "Notes", required=False),
            ],
        ),
    ]
    return fields
