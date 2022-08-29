from fastapi import FastAPI
from paths import home, bookings, travels, users, contact

app = FastAPI()

#Paths from the proyect.
app.include_router(home.router)
app.include_router(bookings.router)
app.include_router(travels.router)
app.include_router(users.router)
app.include_router(contact.router)