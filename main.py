from fastapi import FastAPI
from paths import home, bookings, users, contact, ratings
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status

app = FastAPI()

#Paths from the proyect.
app.include_router(home.router)
app.include_router(bookings.router)
app.include_router(ratings.router)
app.include_router(users.router)
app.include_router(contact.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins='http://localhost:5173/',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


