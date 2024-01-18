from datetime import date
from flask_discord_interactions import ActionRow, TextInput


def get_fields(fulltimer, student):
    """Populate and return fields needed for form(modal)"""
    fields = [
        ActionRow(
            [
                TextInput(
                    "Fulltimers",
                    "Fulltimers (comma seperated)",
                    value=f"{fulltimer}",
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
                TextInput("Notes", "Notes"),
            ],
        ),
    ]
    return fields
