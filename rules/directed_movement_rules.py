from experta import Rule, MATCH, TEST

from facts.facts import Warehouse, Pavilion, State
from utils.search_logger import log_state


MAX_DEPTH = 120


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class DirectedMovementRules:

    @Rule(
        Warehouse(x=MATCH.wx, y=MATCH.wy),
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
        TEST(lambda x, wx: x < wx),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, delivered_keys, visited_keys:
             (x + 1, y, (), delivered_keys) not in visited_keys),
        salience=15
    )
    def empty_move_right_to_warehouse(self, x, y, wx, wy, steps, g, h, f, depth, visited_keys, delivered_keys):
        new_x = x + 1
        new_y = y
        new_key = (new_x, new_y, (), delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(new_x, new_y, wx, wy)
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"move_right to ({new_x}, {new_y})"

        log_state(
            action=action,
            x=new_x,
            y=new_y,
            load=(),
            load_count=0,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=delivered_keys
        )

        self.declare(State(
            robot_x=new_x,
            robot_y=new_y,
            load=(),
            load_count=0,
            steps=steps + (action,),
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            visited_keys=visited_keys + (new_key,),
            delivered_keys=delivered_keys
        ))

    @Rule(
        Warehouse(x=MATCH.wx, y=MATCH.wy),
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
        TEST(lambda x, wx: x > wx),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, delivered_keys, visited_keys:
             (x - 1, y, (), delivered_keys) not in visited_keys),
        salience=15
    )
    def empty_move_left_to_warehouse(self, x, y, wx, wy, steps, g, h, f, depth, visited_keys, delivered_keys):
        new_x = x - 1
        new_y = y
        new_key = (new_x, new_y, (), delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(new_x, new_y, wx, wy)
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"move_left to ({new_x}, {new_y})"

        log_state(
            action=action,
            x=new_x,
            y=new_y,
            load=(),
            load_count=0,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=delivered_keys
        )

        self.declare(State(
            robot_x=new_x,
            robot_y=new_y,
            load=(),
            load_count=0,
            steps=steps + (action,),
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            visited_keys=visited_keys + (new_key,),
            delivered_keys=delivered_keys
        ))

    @Rule(
        Warehouse(x=MATCH.wx, y=MATCH.wy),
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
        TEST(lambda y, wy: y < wy),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, delivered_keys, visited_keys:
             (x, y + 1, (), delivered_keys) not in visited_keys),
        salience=15
    )
    def empty_move_down_to_warehouse(self, x, y, wx, wy, steps, g, h, f, depth, visited_keys, delivered_keys):
        new_x = x
        new_y = y + 1
        new_key = (new_x, new_y, (), delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(new_x, new_y, wx, wy)
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"move_down to ({new_x}, {new_y})"

        log_state(
            action=action,
            x=new_x,
            y=new_y,
            load=(),
            load_count=0,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=delivered_keys
        )

        self.declare(State(
            robot_x=new_x,
            robot_y=new_y,
            load=(),
            load_count=0,
            steps=steps + (action,),
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            visited_keys=visited_keys + (new_key,),
            delivered_keys=delivered_keys
        ))

    @Rule(
        Warehouse(x=MATCH.wx, y=MATCH.wy),
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
        TEST(lambda y, wy: y > wy),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, delivered_keys, visited_keys:
             (x, y - 1, (), delivered_keys) not in visited_keys),
        salience=15
    )
    def empty_move_up_to_warehouse(self, x, y, wx, wy, steps, g, h, f, depth, visited_keys, delivered_keys):
        new_x = x
        new_y = y - 1
        new_key = (new_x, new_y, (), delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(new_x, new_y, wx, wy)
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"move_up to ({new_x}, {new_y})"

        log_state(
            action=action,
            x=new_x,
            y=new_y,
            load=(),
            load_count=0,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=delivered_keys
        )

        self.declare(State(
            robot_x=new_x,
            robot_y=new_y,
            load=(),
            load_count=0,
            steps=steps + (action,),
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            visited_keys=visited_keys + (new_key,),
            delivered_keys=delivered_keys
        ))

    @Rule(
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
        Pavilion(
            id=MATCH.pid,
            x=MATCH.px,
            y=MATCH.py,
            flower_type=MATCH.flower_type
        ),
        TEST(lambda load: len(load) > 0),
        TEST(lambda load, pid, flower_type:
             load[0][0] == pid and load[0][1] == flower_type),
        TEST(lambda x, px: x < px),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, load, delivered_keys, visited_keys:
             (x + 1, y, load, delivered_keys) not in visited_keys),
        salience=16
    )
    def loaded_move_right_to_pavilion(self, x, y, load, load_count, steps, g, h, f, depth, visited_keys, delivered_keys, pid, px, py, flower_type):
        new_x = x + 1
        new_y = y
        new_key = (new_x, new_y, load, delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(new_x, new_y, px, py)
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"move_right to ({new_x}, {new_y})"

        log_state(
            action=action,
            x=new_x,
            y=new_y,
            load=load,
            load_count=load_count,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=delivered_keys
        )

        self.declare(State(
            robot_x=new_x,
            robot_y=new_y,
            load=load,
            load_count=load_count,
            steps=steps + (action,),
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            visited_keys=visited_keys + (new_key,),
            delivered_keys=delivered_keys
        ))

    @Rule(
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
        Pavilion(
            id=MATCH.pid,
            x=MATCH.px,
            y=MATCH.py,
            flower_type=MATCH.flower_type
        ),
        TEST(lambda load: len(load) > 0),
        TEST(lambda load, pid, flower_type:
             load[0][0] == pid and load[0][1] == flower_type),
        TEST(lambda x, px: x > px),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, load, delivered_keys, visited_keys:
             (x - 1, y, load, delivered_keys) not in visited_keys),
        salience=16
    )
    def loaded_move_left_to_pavilion(self, x, y, load, load_count, steps, g, h, f, depth, visited_keys, delivered_keys, pid, px, py, flower_type):
        new_x = x - 1
        new_y = y
        new_key = (new_x, new_y, load, delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(new_x, new_y, px, py)
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"move_left to ({new_x}, {new_y})"

        log_state(
            action=action,
            x=new_x,
            y=new_y,
            load=load,
            load_count=load_count,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=delivered_keys
        )

        self.declare(State(
            robot_x=new_x,
            robot_y=new_y,
            load=load,
            load_count=load_count,
            steps=steps + (action,),
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            visited_keys=visited_keys + (new_key,),
            delivered_keys=delivered_keys
        ))

    @Rule(
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
        Pavilion(
            id=MATCH.pid,
            x=MATCH.px,
            y=MATCH.py,
            flower_type=MATCH.flower_type
        ),
        TEST(lambda load: len(load) > 0),
        TEST(lambda load, pid, flower_type:
             load[0][0] == pid and load[0][1] == flower_type),
        TEST(lambda y, py: y < py),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, load, delivered_keys, visited_keys:
             (x, y + 1, load, delivered_keys) not in visited_keys),
        salience=16
    )
    def loaded_move_down_to_pavilion(self, x, y, load, load_count, steps, g, h, f, depth, visited_keys, delivered_keys, pid, px, py, flower_type):
        new_x = x
        new_y = y + 1
        new_key = (new_x, new_y, load, delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(new_x, new_y, px, py)
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"move_down to ({new_x}, {new_y})"

        log_state(
            action=action,
            x=new_x,
            y=new_y,
            load=load,
            load_count=load_count,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=delivered_keys
        )

        self.declare(State(
            robot_x=new_x,
            robot_y=new_y,
            load=load,
            load_count=load_count,
            steps=steps + (action,),
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            visited_keys=visited_keys + (new_key,),
            delivered_keys=delivered_keys
        ))

    @Rule(
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
        Pavilion(
            id=MATCH.pid,
            x=MATCH.px,
            y=MATCH.py,
            flower_type=MATCH.flower_type
        ),
        TEST(lambda load: len(load) > 0),
        TEST(lambda load, pid, flower_type:
             load[0][0] == pid and load[0][1] == flower_type),
        TEST(lambda y, py: y > py),
        TEST(lambda depth: depth < MAX_DEPTH),
        TEST(lambda x, y, load, delivered_keys, visited_keys:
             (x, y - 1, load, delivered_keys) not in visited_keys),
        salience=16
    )
    def loaded_move_up_to_pavilion(self, x, y, load, load_count, steps, g, h, f, depth, visited_keys, delivered_keys, pid, px, py, flower_type):
        new_x = x
        new_y = y - 1
        new_key = (new_x, new_y, load, delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(new_x, new_y, px, py)
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"move_up to ({new_x}, {new_y})"

        log_state(
            action=action,
            x=new_x,
            y=new_y,
            load=load,
            load_count=load_count,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=delivered_keys
        )

        self.declare(State(
            robot_x=new_x,
            robot_y=new_y,
            load=load,
            load_count=load_count,
            steps=steps + (action,),
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            visited_keys=visited_keys + (new_key,),
            delivered_keys=delivered_keys
        ))