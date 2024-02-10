from datetime import date
from flask_discord_interactions import ActionRow, TextInput

def get_fields():
    """Populate and return fields needed for form(modal)"""
    fields = [
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
                TextInput(
                    "fulltimers",
                    "Fulltimers (comma separated)",
                )
            ]
        ),
        ActionRow(
            [
                TextInput(
                    "numOfPeopleContacted",
                    "# of people contacted",
                )
            ]
        ),
        ActionRow(
            [
                TextInput(
                    "numOfTractsPassed",
                    "# of tracts passed",
                )
            ]
        ),
        ActionRow(
            [
                TextInput("notes", "Notes", placeholder="Positive reports, names to pray for, other info", required=False),
            ],
        ),
    ]
    return fields