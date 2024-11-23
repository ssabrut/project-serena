from src.utils import load_data

import uuid
import pandas as pd
from langchain_core.tools import tool
from datetime import date, datetime
from langchain_core.runnables import RunnableConfig
from typing import Optional

@tool
def search_booking(booking_date: date = None, booking_hour: str = None) -> dict:
    """Search for a booking in the database."""
    if booking_date is None and booking_hour is None:
        return "Please provide a booking date or booking hour to search for a booking."

    data = load_data()
    booking = data[(data["booking_date"] == booking_date) & (data["booking_hour"] == booking_hour)]
    if booking.empty:
        return "No booking found for the provided date and hour."
    return booking.to_dict(orient="records")

@tool
def insert_booking(name: str = None, booking_date: date = None, booking_hour: str = None, party_size: int = None, special_requests: str = None) -> str:
    """Insert a booking into the database."""
    if name is None or booking_date is None or booking_hour is None or party_size is None:
        return "Please provide all required information to make a booking."

    data = load_data()
    new_booking = pd.DataFrame({
        "id": [uuid.uuid4()],
        "name": [name],
        "booking_date": [booking_date],
        "booking_hour": [booking_hour],
        "party_size": [party_size],
        "special_requests": [special_requests]
    })

    data = pd.concat([data, new_booking], ignore_index=True)
    data.to_csv("data/booking.csv", index=False)
    return "Booking successfully added."

book_safe_tools = [search_booking]
book_sensitive_tools = [insert_booking]
book_restaurant_tools = book_safe_tools + book_sensitive_tools