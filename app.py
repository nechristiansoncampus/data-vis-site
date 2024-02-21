import os
from flask import Flask
from flask_discord_interactions import DiscordInteractions
from flask_discord_interactions import (
    DiscordInteractions,
)
from appointments import bp as appointment_bp
from events import bp as event_bp
from gospel import bp as gospel_bp

app = Flask(__name__)
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]
discord.register_blueprint(appointment_bp)
discord.register_blueprint(event_bp)
discord.register_blueprint(gospel_bp)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"


@app.route("/appt")
def appt():
    return "appointments endpoint"


@app.route("/event")
def event():
    return "event attendance endpoint"


discord.set_route("/interactions")

# Only uncomment this if you change the keywords on the commands
# discord.update_commands(guild_id=os.environ["TESTING_GUILD"])

if __name__ == "__main__":
    app.run(debug=True)
