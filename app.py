from secrets import compare_digest

from quart import Quart, request
from quart_auth import (
    QuartAuth, AuthUser, current_user, login_required, login_required, login_user, logout_user
    )

app = Quart(__name__)
app.secret_key = "prEZVMOjCXcN1QP12eOAHw" # Store in .env
app.config["QUART_AUTH_MODE"] = "bearer"
auth_manager = QuartAuth(app)

@app.get("/")
async def index():
    return {"Hello": "World"}

@app.get("/private")
@login_required
async def private():
    return {"message": f"Something sensitive being viewed by {current_user.auth_id}"}

@app.post("/login")
async def login():
    data = await request.get_json()
    if data["username"] == "user" and compare_digest(data["password"], "password"): # Do not hard code
        token = auth_manager.dump_token("user")
        return {"token": token}, 200
    else:
        return {}, 400

