from quart import Quart
from quart_auth import basic_auth_required

app = Quart(__name__)
app.config["QUART_AUTH_BASIC_USERNAME"] = "user" # Do not do this in real world scenario
app.config["QUART_AUTH_BASIC_PASSWORD"] = "password" # Save to database or .env

@app.get("/")
async def index():
    return "Hello"

@app.get("/private")
@basic_auth_required()
async def private():
    return "Something sensitive"