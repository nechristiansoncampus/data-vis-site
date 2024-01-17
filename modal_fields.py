from flask_discord_interactions import (
    ActionRow,
    TextInput
)

from datetime import date

def get_fields(fulltimer, student):
    fields = [
                ActionRow(
            [
                TextInput(
                    "user_input_fter",
                    "Enter the Full Timer",
                    value=f"{fulltimer}"
                )
            ]
        ),
                ActionRow(
            [
                TextInput(
                    "user_input_student",
                    "Enter the Student",
                    value=f"{student}"
                )
            ]
        ),
                ActionRow(
            [
                TextInput(
                    "user_input_other_fter",
                    "Other Fulltimer/Trainee (optional)",
                    required=False
                )
            ]
        ),
                ActionRow(
            [
                TextInput(
                    "user_input_other_student",
                    "Enter additional students (optional)",
                    required=False
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
        )
    ]
    return fields