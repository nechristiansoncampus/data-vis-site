from flask_discord_interactions import (
    ActionRow,
    TextInput
)

from datetime import date

def get_fields(fulltimer):
    fields = [
                ActionRow(
            [
                TextInput(
                    "user_input_time",
                    "Enter the Event Name",
                    value="Bible Study"
                )
            ]
        ),

                ActionRow(
            [
                TextInput(
                    "user_input_fter",
                    "Enter the Full Timer",
                    value=f"You selected **{fulltimer}**!"
                )
            ]
        ),

                ActionRow(
            [
                TextInput(
                    "user_input_new",
                    "Enter the Date",
                    placeholder=str(date.today()),
                    value=str(date.today())
                )
            ]
        ),

          ActionRow(
            [
                TextInput(
                    "user_input_name",
                    "Enter New Attendee *only if first mtg*",
                    required=False
                )
            ]
        )
    ]
    return fields