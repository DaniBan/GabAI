from ..llm import get_openai_client
from logging import getLogger

logger = getLogger(__name__)

class TaskPlanner:
    def __init__(self):
        """
        Initialize Task Planner.
        """
        self.llm_client = get_openai_client()
        logger.info("Task Planner initialized")

    def plan_steps(self, task_description: str):
        response = self.llm_client.responses.create(
            model="gpt-4.1",
            instructions="Based on the following task description, create detailed steps to complete the task. Return"
                         "the steps as a list.",
            input=task_description
        )
        return response.output_text