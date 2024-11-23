from src.llms import llm
from src.config.states import CompleteOrEscalate
from src.tools.booking import book_restaurant_tools
from src.tools.primary import ToBookRestaurant
from src.config.prompts import book_restaurant_prompt, primary_assistant_prompt

book_restaurant_runnable = book_restaurant_prompt | llm.bind_tools(book_restaurant_tools) + [CompleteOrEscalate]
primary_assistant_runnable = primary_assistant_prompt | llm.bind_tools([ToBookRestaurant])