from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import AnyMessage, add_messages
from pydantic import BaseModel

def update_dialog_state(left: list[str], right: Optional[str]) -> list[str]:
    if right is None:
        return left
    if right == "pop":
        return left[:-1]
    return left + [right]

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    user_info: str
    dialog_state: Annotated[
        list[
            Literal[
                "assistant",
                "book_restaurant",
                "menu_request",
            ]
        ],
        update_dialog_state
    ]

class CompleteOrEscalate(BaseModel):
    cancel: bool = True
    reason: str

    class Config:
        json_schema_extra = {
            "example": {
                "cancel": True,
                "reason": "User changed their mind about the current task."
            },
            "example 2": {
                "cancel": True,
                "reason": "I have fully completed the task."
            }
        }