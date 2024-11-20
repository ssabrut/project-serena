from src.utils import load_data

import uuid
import pandas as pd
from langchain_core.tools import tool
from datetime import date, datetime
from langchain_core.runnables import RunnableConfig
from typing import Optional

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