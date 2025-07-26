import click

from app.agents.trade_assistant import TradeAssistant
from ..agents import TaskPlanner


@click.group()
def cli():
    """CLI for interacting with AI agents."""
    pass


@cli.command()
@click.option("--prompt", prompt="Your prompt", help="Task propmt to brak down")
def task(prompt):
    """Plan a task."""
    planner = TaskPlanner()
    response = planner.plan_steps(prompt, model="gemini-2.5-flash")
    print(response)


@cli.command()
@click.option("--prompt", prompt="Your prompt", help="Strategy brief description")
@click.option("--instrument", prompt="Your prompt", help="Instrument or type of instrument to trade",
              default="any instrument")
def trade(prompt, instrument):
    """Plan a trading strategy."""
    planner = TradeAssistant()
    response = planner.create_strategy(prompt, instrument, model="gemini-2.5-flash")
    print(response)


if __name__ == "__main__":
    cli()
