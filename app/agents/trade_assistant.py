from ..llm import LLMClient
from logging import getLogger

logger = getLogger(__name__)


class TradeAssistant:
    def __init__(self, agent: str = "gemini"):
        """
        Initialize Trade Assistant.
        """
        self.llm_client = LLMClient(agent)
        logger.info("Task Planner initialized")

    def create_strategy(self, description: str, instrument: str, model: str) -> str:
        response = self.llm_client.generate(
            prompt=f"Create a brief trading strategy for ${instrument} based on the following "
                   f"description: ${description}.",
            model=model
        )
        return response
