from datetime import date
from flask_discord_interactions import ActionRow, TextInput


def get_fields():
    """Populate and return fields needed for form(modal)"""
    fields = [
        ActionRow(
            [
                TextInput("Name", "Event Name"),
            ],
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


def add_student_fields():
    """Populate and return fields needed for form(modal)"""
    fields = [
        ActionRow(
            [
                TextInput("add_students", "Add Students (Comma Seperated)"),
            ],
        )
    ]
    return fields
