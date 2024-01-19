from datetime import date
from flask_discord_interactions import ActionRow, TextInput


def get_fields(student):
    """Populate and return fields needed for form(modal)"""
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
                    value=f"{student}",
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
