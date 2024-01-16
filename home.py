import os
from flask import Flask
from flask_discord_interactions import DiscordInteractions
from flask_discord_interactions import (
    DiscordInteractions,
)
from appointments import bp as appointment_bp

app = Flask(__name__)
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]
discord.register_blueprint(appointment_bp)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/appt")
def appt():
    return "appointments endpoint"

@app.route("/event")
def event():
    return "event attendance endpoint"

@discord.command()
def ping(ctx):
    "Respond with a friendly 'pong'!"
    return "Pong!"

discord.set_route("/interactions")
discord.update_commands(guild_id=os.environ["TESTING_GUILD"])

if __name__ == '__main__':
    app.run(debug=True)