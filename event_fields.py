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


def add_student_fields(event_id):
    """Populate and return fields needed for form(modal)"""
    fields = [
        ActionRow(
            [
                TextInput("firstname", "First Name"),
            ],
        ),
        ActionRow(
            [
                TextInput("lastname", "Last Name"),
            ],
        ),
        ActionRow(
            [
                TextInput("event_id", "Event ID", value=f"{event_id}"),
            ],
        ),
    ]
    return fields
