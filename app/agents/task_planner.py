from ..llm import get_openai_client, get_gemini_client
from logging import getLogger

logger = getLogger(__name__)


class TaskPlanner:
    def __init__(self):
        """
        Initialize Task Planner.
        """
        self.llm_client = get_gemini_client()
        logger.info("Task Planner initialized")

    def plan_steps(self, task_description: str) -> str:
        # response = self.llm_client.responses.create(
        #     model="gpt-4.1",
        #     instructions="Based on the following task description, create detailed steps to complete the task. Return"
        #                  "the steps as a list.",
        #     input=task_description
        # )

        response = self.llm_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Very briefly describe some steps to complete the following task: ${task_description}. "
                     f"Return the steps as a list."
        )
        return response.text
