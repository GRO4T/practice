import secrets

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

SECRET = "very-secret-key"

app = FastAPI()

security = HTTPBasic()

fake_db = {'johndoe': 'hunter2'}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    print(credentials.username)
    print(credentials.password)
    correct_password = fake_db.get(credentials.username)
    is_password_correct = None
    try:
        is_password_correct = secrets.compare_digest(credentials.password, correct_password)
    except TypeError:
        pass

    if not (correct_password and is_password_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/logout")
def logout():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Logout",
        headers={"WWW-Authenticate": "Basic"},
    )


@app.get('/protected')
def protected_route():
    return {"message": "Congratulations you got to a protected zone"}
