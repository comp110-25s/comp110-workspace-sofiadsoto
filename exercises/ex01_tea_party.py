"""my tea part"""
_author__: str = "730675549"


def main_planner(guests: int):
    """the main function"""


def tea_bags(people: int) -> int:
    """how mauch tea per person"""
    return people * 2


def treats(people: int) -> float:
    """the number of snacks patrons will eat"""
    return tea_bags(people) * 1.5


def cost(tea_count: int, treat_count: int) -> float:
    """the cost of everything"""
    return tea_count * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))