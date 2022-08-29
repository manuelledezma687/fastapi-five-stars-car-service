#Python packages

#Pydantic packages

#FastAPI packages
from fastapi import FastAPI

#Local packages
from paths import users

app = FastAPI()

#Paths from the proyect.
#app.include_router(Home.router)
#app.include_router(Bookings.router)
#app.include_router(Travels.router)
app.include_router(users.router)
#app.include_router(Contact.router)