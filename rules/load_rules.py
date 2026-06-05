from experta import Rule, MATCH, TEST

from facts.facts import Warehouse, Pavilion, PavilionLoad, ColorLoad, MaxLoad, State


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def load_items_not_delivered(load_items, delivered_keys):
    if len(load_items) == 0:
        return True

    current_key = (load_items[0][0], load_items[0][2])

    if current_key in delivered_keys:
        return False

    return load_items_not_delivered(load_items[1:], delivered_keys)


def describe_load(load_items):
    if len(load_items) == 0:
        return ""

    current = f"{load_items[0][2]} x{load_items[0][3]}"

    if len(load_items) == 1:
        return current

    return current + " + " + describe_load(load_items[1:])


class LoadRules:

    @Rule(
        Warehouse(x=MATCH.wx, y=MATCH.wy),
        MaxLoad(value=MATCH.max_load),

        State(
            robot_x=MATCH.wx,
            robot_y=MATCH.wy,
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

        PavilionLoad(
            pavilion_id=MATCH.pid,
            total=MATCH.total,
            counted_needs=MATCH.counted_needs,
            load_items=MATCH.load_items
        ),

        Pavilion(
            id=MATCH.pid,
            x=MATCH.px,
            y=MATCH.py,
            flower_type=MATCH.flower_type
        ),

        TEST(lambda total: total > 0),
        TEST(lambda total, max_load: total <= max_load),
        TEST(lambda load_items, delivered_keys:
             load_items_not_delivered(load_items, delivered_keys)),

        salience=30
    )
    def load_pavilion_package(
        self,
        wx,
        wy,
        max_load,
        steps,
        g,
        h,
        f,
        depth,
        visited_keys,
        delivered_keys,
        pid,
        total,
        counted_needs,
        load_items,
        px,
        py,
        flower_type
    ):
        new_load = load_items
        new_key = (wx, wy, new_load, delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(wx, wy, px, py)
        new_f = new_g + new_h

        self.declare(
            State(
                robot_x=wx,
                robot_y=wy,
                load=new_load,
                load_count=total,
                steps=steps + (
                    f"load same type pavilion {pid} {flower_type}: {describe_load(load_items)}",
                ),
                g=new_g,
                h=new_h,
                f=new_f,
                depth=depth + 1,
                visited_keys=visited_keys + (new_key,),
                delivered_keys=delivered_keys
            )
        )

    @Rule(
        Warehouse(x=MATCH.wx, y=MATCH.wy),
        MaxLoad(value=MATCH.max_load),

        State(
            robot_x=MATCH.wx,
            robot_y=MATCH.wy,
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

        ColorLoad(
            color=MATCH.color,
            total=MATCH.total,
            counted_needs=MATCH.counted_needs,
            load_items=MATCH.load_items
        ),

        Pavilion(
            id=MATCH.target_pid,
            x=MATCH.px,
            y=MATCH.py,
            flower_type=MATCH.target_flower_type
        ),

        TEST(lambda total: total > 0),
        TEST(lambda total, max_load: total <= max_load),
        TEST(lambda load_items, delivered_keys:
             load_items_not_delivered(load_items, delivered_keys)),
        TEST(lambda load_items, target_pid:
             len(load_items) > 0 and load_items[0][0] == target_pid),

        salience=25
    )
    def load_same_color_package(
        self,
        wx,
        wy,
        max_load,
        steps,
        g,
        h,
        f,
        depth,
        visited_keys,
        delivered_keys,
        color,
        total,
        counted_needs,
        load_items,
        target_pid,
        px,
        py,
        target_flower_type
    ):
        new_load = load_items
        new_key = (wx, wy, new_load, delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(wx, wy, px, py)
        new_f = new_g + new_h

        self.declare(
            State(
                robot_x=wx,
                robot_y=wy,
                load=new_load,
                load_count=total,
                steps=steps + (
                    f"load same color {color}: {describe_load(load_items)}",
                ),
                g=new_g,
                h=new_h,
                f=new_f,
                depth=depth + 1,
                visited_keys=visited_keys + (new_key,),
                delivered_keys=delivered_keys
            )
        )