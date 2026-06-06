from typing import Optional, List
from app.models.game import Scenario

# In-memory store with sample scenarios
scenarios_db = {
    "1": Scenario(
        id="1",
        title="Emergency Fund",
        description="You lost your job",
        situation="You just lost your job and have 3 months of expenses saved. What should you do?",
        options=[
            "Invest in the stock market",
            "Keep it in a savings account",
            "Spend it on a vacation",
            "Give it to family"
        ],
        correct_answer=1,
        explanation="An emergency fund should be liquid and safe.",
        difficulty="easy"
    ),
    "2": Scenario(
        id="2",
        title="Debt Payoff Strategy",
        description="You have multiple debts",
        situation="You have credit card debt at 18% APR and student loans at 5% APR. Which should you pay off first?",
        options=[
            "Student loans (lower balance)",
            "Credit card (higher interest)",
            "Pay both equally",
            "Pay neither"
        ],
        correct_answer=1,
        explanation="Higher interest rates cost you more money over time.",
        difficulty="medium"
    ),
}


class GameRepository:
    @staticmethod
    async def list_scenarios(limit: int = 10) -> List[Scenario]:
        return list(scenarios_db.values())[:limit]

    @staticmethod
    async def get_scenario(scenario_id: str) -> Optional[Scenario]:
        return scenarios_db.get(scenario_id)

    @staticmethod
    async def create_scenario(scenario_data: dict) -> Scenario:
        scenario_id = str(len(scenarios_db) + 1)
        scenario = Scenario(id=scenario_id, **scenario_data)
        scenarios_db[scenario_id] = scenario
        return scenario
