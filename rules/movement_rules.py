from experta import Rule, MATCH, TEST

from facts.facts import Grid, State


MAX_DEPTH = 80


class MovementRules:

    @Rule(
        Grid(width=MATCH.width, height=MATCH.height),
        State(
            robot_x=MATCH.x,
            robot_y=MATCH.y,
            load=MATCH.load,
            load_count=MATCH.load_count,
            steps=MATCH.steps,
            g=MATCH.g,
            h=MATCH.h,
            f=MATCH.f,
            depth=MATCH.depth,
            visited_keys=MATCH.visited_keys,
            delivered_keys=MATCH.delivered_keys
        ),
        TEST(lambda x, width: x < width),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, load, delivered_keys, visited_keys:
             (x + 1, y, load, delivered_keys) not in visited_keys)
    )
    def move_right(self, x, y, width, height, load, load_count, steps, g, h, f, depth, visited_keys, delivered_keys):
        new_x = x + 1
        new_y = y
        new_key = (new_x, new_y, load, delivered_keys)

        # print(f"Move Right: ({x}, {y}) -> ({new_x}, {new_y})")

        self.declare(
            State(
                robot_x=new_x,
                robot_y=new_y,
                load=load,
                load_count=load_count,
                steps=steps + (f"move_right to ({new_x}, {new_y})",),
                g=g + 1,
                h=h,
                f=f + 1,
                depth=depth + 1,
                visited_keys=visited_keys + (new_key,),
                delivered_keys=delivered_keys
            )
        )

    @Rule(
        Grid(width=MATCH.width, height=MATCH.height),
        State(
            robot_x=MATCH.x,
            robot_y=MATCH.y,
            load=MATCH.load,
            load_count=MATCH.load_count,
            steps=MATCH.steps,
            g=MATCH.g,
            h=MATCH.h,
            f=MATCH.f,
            depth=MATCH.depth,
            visited_keys=MATCH.visited_keys,
            delivered_keys=MATCH.delivered_keys
        ),
        TEST(lambda x: x > 1),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, load, delivered_keys, visited_keys:
             (x - 1, y, load, delivered_keys) not in visited_keys)
    )
    def move_left(self, x, y, width, height, load, load_count, steps, g, h, f, depth, visited_keys, delivered_keys):
        new_x = x - 1
        new_y = y
        new_key = (new_x, new_y, load, delivered_keys)

        print(f"Move Left: ({x}, {y}) -> ({new_x}, {new_y})")

        self.declare(
            State(
                robot_x=new_x,
                robot_y=new_y,
                load=load,
                load_count=load_count,
                steps=steps + (f"move_left to ({new_x}, {new_y})",),
                g=g + 1,
                h=h,
                f=f + 1,
                depth=depth + 1,
                visited_keys=visited_keys + (new_key,),
                delivered_keys=delivered_keys
            )
        )

    @Rule(
        Grid(width=MATCH.width, height=MATCH.height),
        State(
            robot_x=MATCH.x,
            robot_y=MATCH.y,
            load=MATCH.load,
            load_count=MATCH.load_count,
            steps=MATCH.steps,
            g=MATCH.g,
            h=MATCH.h,
            f=MATCH.f,
            depth=MATCH.depth,
            visited_keys=MATCH.visited_keys,
            delivered_keys=MATCH.delivered_keys
        ),
        TEST(lambda y: y > 1),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, load, delivered_keys, visited_keys:
             (x, y - 1, load, delivered_keys) not in visited_keys)
    )
    def move_up(self, x, y, width, height, load, load_count, steps, g, h, f, depth, visited_keys, delivered_keys):
        new_x = x
        new_y = y - 1
        new_key = (new_x, new_y, load, delivered_keys)

        # print(f"Move Up: ({x}, {y}) -> ({new_x}, {new_y})")

        self.declare(
            State(
                robot_x=new_x,
                robot_y=new_y,
                load=load,
                load_count=load_count,
                steps=steps + (f"move_up to ({new_x}, {new_y})",),
                g=g + 1,
                h=h,
                f=f + 1,
                depth=depth + 1,
                visited_keys=visited_keys + (new_key,),
                delivered_keys=delivered_keys
            )
        )

    @Rule(
        Grid(width=MATCH.width, height=MATCH.height),
        State(
            robot_x=MATCH.x,
            robot_y=MATCH.y,
            load=MATCH.load,
            load_count=MATCH.load_count,
            steps=MATCH.steps,
            g=MATCH.g,
            h=MATCH.h,
            f=MATCH.f,
            depth=MATCH.depth,
            visited_keys=MATCH.visited_keys,
            delivered_keys=MATCH.delivered_keys
        ),
        TEST(lambda y, height: y < height),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, load, delivered_keys, visited_keys:
             (x, y + 1, load, delivered_keys) not in visited_keys)
    )
    def move_down(self, x, y, width, height, load, load_count, steps, g, h, f, depth, visited_keys, delivered_keys):
        new_x = x
        new_y = y + 1
        new_key = (new_x, new_y, load, delivered_keys)

        # print(f"Move Down: ({x}, {y}) -> ({new_x}, {new_y})")

        self.declare(
            State(
                robot_x=new_x,
                robot_y=new_y,
                load=load,
                load_count=load_count,
                steps=steps + (f"move_down to ({new_x}, {new_y})",),
                g=g + 1,
                h=h,
                f=f + 1,
                depth=depth + 1,
                visited_keys=visited_keys + (new_key,),
                delivered_keys=delivered_keys
            )
        )