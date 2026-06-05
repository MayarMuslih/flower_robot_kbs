from engine import FlowerRobotEngine
from data.initial_state import initial_facts


def declare_initial_facts(engine, facts, index=0):
    if index == len(facts):
        return

    engine.declare(facts[index])
    declare_initial_facts(engine, facts, index + 1)


def main():
    engine = FlowerRobotEngine()
    engine.reset()

    print("Knowledge Base System Started")
    print("=" * 60)
    print("Searching for solution...")
    print("=" * 60)

    declare_initial_facts(engine, initial_facts)

    engine.run()


if __name__ == "__main__":
    main()