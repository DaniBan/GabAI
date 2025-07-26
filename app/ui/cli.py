import click

from ..agents import TaskPlanner


@click.group()
def cli():
    """CLI for interacting with AI agents."""
    pass

@cli.command()
@click.option("--prompt", prompt="Your prompt", help="Task propmt to brak down")
def plan(prompt):
    """Plan a task."""
    planner = TaskPlanner()
    response = planner.plan_steps(prompt)
    print(response)


if __name__ == "__main__":
    cli()
