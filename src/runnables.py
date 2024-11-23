from src.llms import llm
from src.config.states import CompleteOrEscalate
from src.tools.booking import book_restaurant_tools
from src.config.prompts import book_restaurant_prompt

book_restaurant_runnable = book_restaurant_prompt | llm.bind_tools(book_restaurant_tools) + [CompleteOrEscalate]