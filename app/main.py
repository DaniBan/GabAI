from dotenv import load_dotenv

from app.agents import TaskPlanner

load_dotenv()

if __name__ == "__main__":
    task_planner = TaskPlanner()
    task_description = "Write a program that prints the first 100 natural numbers."
    print(task_planner.plan_steps(task_description))
