from ..llm import LLMClient
from logging import getLogger

logger = getLogger(__name__)


class TaskPlanner:
    def __init__(self, agent: str = "gemini"):
        """
        Initialize Task Planner.
        """
        self.llm_client = LLMClient(agent)
        logger.info("Task Planner initialized")

    def plan_steps(self, task_description: str) -> str:
        response = self.llm_client.generate(
            prompt=f"Very briefly describe some steps to complete the following task: ${task_description}. "
                     f"Return the steps as a list.",
            model="gemini-2.5-flash"
        )
        return response
