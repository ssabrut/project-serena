from pydantic import BaseModel, Field

class ToBookRestaurant(BaseModel):
    """Transfer work to a specialized assistant for booking reservations at Serena Restaurant."""

    name: str = Field(description="The name of the customer.")
    booking_date: str = Field(description="The date of the booking.")
    booking_time: str = Field(description="The time of the booking.")
    party_size: int = Field(description="The number of people in the booking.")
    special_request: str = Field(description="Any special requests for the booking.")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "booking_date": "2022-01-01",
                "booking_time": "18:00",
                "party_size": 4,
                "special_request": "Window seat"
            },
            "example 2": {
                "name": "Jane Doe",
                "booking_date": "2022-01-01",
                "booking_time": "18:00",
                "party_size": 4,
                "special_request": ""
            }
        }