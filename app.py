from secrets import compare_digest

from quart import Quart, redirect, request, url_for
from quart_auth import QuartAuth, AuthUser, login_required, login_required, login_user

app = Quart(__name__)
app.secret_key = "prEZVMOjCXcN1QP12eOAHw" # Store in .env
auth_manager = QuartAuth(app)

@app.get("/")
async def index():
    return "Hello"

@app.get("/private")
@login_required
async def private():
    return "Something sensitive"

@app.route("/login", methods={"GET", "POST"})
async def login():
    if request.method == "POST":
        data = await request.form
        if data["username"] == "user" and compare_digest(data["password"], "password"): # Do not hard code
            login_user(AuthUser("user"))
            return redirect(url_for("private"))

    return """
    <form method="POST">
    <input name="username">
    <input name="password" type="password">
    <input type="submit" value="Login">
    </form>
    """