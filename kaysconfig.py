from dotenv import load_dotenv

load_dotenv("config.env")

HEROKU = (
    True  # NOTE Make it false if you're not deploying on heroku or docker.
)

if HEROKU:
    from os import environ
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
