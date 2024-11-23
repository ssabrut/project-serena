from src.config.states import AgentState
from langchain_core.runnables import Runnable, RunnableConfig

class Assistant:
    def __init__(self, runnable: Runnable) -> None:
        self.runnable = runnable

    def __call__(self, state: AgentState, config: RunnableConfig) -> dict:
        while True:
            result = self.runnable.invoke(state)
            if not result.tool_calls and (not result.content or isinstance(result.content, list) and not result.content[0].get("text")):
                messages = state["messages"] + [("user", "Respond with a real output.")]
                state = {**state, "messages": messages}
            else:
                break
        return {"messages": result}