from experta import Rule, MATCH, TEST

from facts.facts import State, NeedTotal, MaxLoad


class GoalRules:

    @Rule(
        NeedTotal(value=MATCH.total_needs),

        MaxLoad(value=MATCH.max_load),

        State(
            robot_x=MATCH.x,
            robot_y=MATCH.y,
            load=(),
            load_count=0,
            steps=MATCH.steps,
            g=MATCH.g,
            h=MATCH.h,
            f=MATCH.f,
            depth=MATCH.depth,
            visited_keys=MATCH.visited_keys,
            delivered_keys=MATCH.delivered_keys
        ),

        TEST(lambda delivered_keys, total_needs:
             len(delivered_keys) == total_needs),

        salience=100
    )
    def goal_reached(
        self,
        total_needs,
        max_load,
        x,
        y,
        steps,
        g,
        h,
        f,
        depth,
        visited_keys,
        delivered_keys
    ):
        print("\n" + "=" * 60)
        print("GOAL REACHED")
        print("=" * 60)

        print(f"Final Robot Position: ({x}, {y})")
        print("Robot Load Count: 0")
        print(f"Calculated Max Load: {max_load}")
        print(f"Delivered Needs: {len(delivered_keys)} / {total_needs}")
        print(f"Total Cost: {g}")

        print("\nA* Cost Values:")
        print(f"Final g(n): {g}")
        print(f"Final h(n): {h}")
        print(f"Final f(n): {f}")

        print(f"\nSearch Depth: {depth}")

        print("\n" + "-" * 60)
        print("SOLUTION PATH")
        print("-" * 60)

        self.print_solution_steps(steps, 1)

        print("-" * 60)
        print("Delivered Keys:")
        print(delivered_keys)

        print("=" * 60)

        self.halt()

    def print_solution_steps(self, steps, index):
        if len(steps) == 0:
            return

        print(f"{index}. {steps[0]}")

        self.print_solution_steps(steps[1:], index + 1)