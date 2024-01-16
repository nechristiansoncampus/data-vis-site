import os
from flask import Flask
from flask_discord_interactions import DiscordInteractions

class AppConfig:
    app = Flask(__name__)
    discord = DiscordInteractions(app)
    app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
    app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
    app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]

    @classmethod
    def getApp():
        return AppConfig.app
    
    @staticmethod
    def getDiscord():
        return AppConfig.discord