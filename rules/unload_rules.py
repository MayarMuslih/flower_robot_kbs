from experta import Rule, MATCH, TEST

from facts.facts import Pavilion, State
from utils.search_logger import log_state


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def load_has_item_for_pavilion(load, pid, flower_type):
    if len(load) == 0:
        return False

    if load[0][0] == pid and load[0][1] == flower_type:
        return True

    return load_has_item_for_pavilion(load[1:], pid, flower_type)


def split_load_for_pavilion(load, pid, flower_type):
    if len(load) == 0:
        return (), ()

    current = load[0]
    delivered_rest, remaining_rest = split_load_for_pavilion(load[1:], pid, flower_type)

    if current[0] == pid and current[1] == flower_type:
        return (current,) + delivered_rest, remaining_rest

    return delivered_rest, (current,) + remaining_rest


def keys_from_load(load):
    if len(load) == 0:
        return ()

    return ((load[0][0], load[0][2]),) + keys_from_load(load[1:])


def count_load(load):
    if len(load) == 0:
        return 0

    return load[0][3] + count_load(load[1:])


def describe_load(load):
    if len(load) == 0:
        return ""

    current = f"{load[0][2]} x{load[0][3]}"

    if len(load) == 1:
        return current

    return current + " + " + describe_load(load[1:])


def first_load_pid(load):
    if len(load) == 0:
        return None

    return load[0][0]


def first_load_flower_type(load):
    if len(load) == 0:
        return None

    return load[0][1]


class UnloadRules:

    # ==========================================
    # UNLOAD AND ROBOT BECOMES EMPTY
    # ==========================================

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
            x=MATCH.x,
            y=MATCH.y,
            flower_type=MATCH.flower_type
        ),

        TEST(lambda load:
             len(load) > 0),

        TEST(lambda load, pid, flower_type:
             load_has_item_for_pavilion(load, pid, flower_type)),

        TEST(lambda load, pid, flower_type:
             len(split_load_for_pavilion(load, pid, flower_type)[1]) == 0),

        salience=40
    )
    def unload_matching_part_empty_after(
        self,
        x,
        y,
        load,
        load_count,
        steps,
        g,
        h,
        f,
        depth,
        visited_keys,
        delivered_keys,
        pid,
        flower_type
    ):
        delivered_part, remaining_load = split_load_for_pavilion(load, pid, flower_type)

        delivered_now = keys_from_load(delivered_part)
        new_delivered_keys = delivered_keys + delivered_now

        new_load_count = 0
        new_key = (x, y, remaining_load, new_delivered_keys)

        new_g = g + 1
        new_h = 0
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"unload pavilion {pid} {flower_type}: {describe_load(delivered_part)}"

        log_state(
            action=action,
            x=x,
            y=y,
            load=remaining_load,
            load_count=new_load_count,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=new_delivered_keys
        )

        self.declare(
            State(
                robot_x=x,
                robot_y=y,
                load=remaining_load,
                load_count=new_load_count,
                steps=steps + (action,),
                g=new_g,
                h=new_h,
                f=new_f,
                depth=new_depth,
                visited_keys=visited_keys + (new_key,),
                delivered_keys=new_delivered_keys
            )
        )

    # ==========================================
    # UNLOAD AND ROBOT STILL HAS REMAINING LOAD
    # ==========================================

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
            x=MATCH.x,
            y=MATCH.y,
            flower_type=MATCH.flower_type
        ),

        TEST(lambda load:
             len(load) > 0),

        TEST(lambda load, pid, flower_type:
             load_has_item_for_pavilion(load, pid, flower_type)),

        TEST(lambda load, pid, flower_type:
             len(split_load_for_pavilion(load, pid, flower_type)[1]) > 0),

        Pavilion(
            id=MATCH.next_pid,
            x=MATCH.next_x,
            y=MATCH.next_y,
            flower_type=MATCH.next_flower_type
        ),

        TEST(lambda load, pid, flower_type, next_pid, next_flower_type:
             len(split_load_for_pavilion(load, pid, flower_type)[1]) > 0
             and
             first_load_pid(split_load_for_pavilion(load, pid, flower_type)[1]) == next_pid
             and
             first_load_flower_type(split_load_for_pavilion(load, pid, flower_type)[1]) == next_flower_type),

        salience=40
    )
    def unload_matching_part_with_remaining(
        self,
        x,
        y,
        load,
        load_count,
        steps,
        g,
        h,
        f,
        depth,
        visited_keys,
        delivered_keys,
        pid,
        flower_type,
        next_pid,
        next_x,
        next_y,
        next_flower_type
    ):
        delivered_part, remaining_load = split_load_for_pavilion(load, pid, flower_type)

        delivered_now = keys_from_load(delivered_part)
        new_delivered_keys = delivered_keys + delivered_now

        new_load_count = count_load(remaining_load)
        new_key = (x, y, remaining_load, new_delivered_keys)

        new_g = g + 1
        new_h = manhattan_distance(x, y, next_x, next_y)
        new_f = new_g + new_h
        new_depth = depth + 1

        action = f"unload pavilion {pid} {flower_type}: {describe_load(delivered_part)}"

        log_state(
            action=action,
            x=x,
            y=y,
            load=remaining_load,
            load_count=new_load_count,
            g=new_g,
            h=new_h,
            f=new_f,
            depth=new_depth,
            delivered_keys=new_delivered_keys
        )

        self.declare(
            State(
                robot_x=x,
                robot_y=y,
                load=remaining_load,
                load_count=new_load_count,
                steps=steps + (action,),
                g=new_g,
                h=new_h,
                f=new_f,
                depth=new_depth,
                visited_keys=visited_keys + (new_key,),
                delivered_keys=new_delivered_keys
            )
        )