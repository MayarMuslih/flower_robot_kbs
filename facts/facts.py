from experta import Fact


class Grid(Fact):
    """
    Grid(width, height)
    Represents the exhibition grid size.
    """
    pass


class Warehouse(Fact):
    """
    Warehouse(x, y)
    Represents the warehouse position.
    """
    pass


class Pavilion(Fact):
    """
    Pavilion(id, x, y, flower_type)
    Represents one pavilion.
    """
    pass


class Need(Fact):
    """
    Need(pavilion_id, flower_type, color, quantity)
    Represents one color requirement for one pavilion.
    """
    pass


class MaxLoad(Fact):
    """
    MaxLoad(value)
    Represents the maximum robot capacity.
    """
    pass


class State(Fact):
    """
    One complete search state.

    Fields:
    - robot_x
    - robot_y
    - load
    - load_count
    - steps
    - g
    - h
    - f
    - depth
    - visited_keys
    - delivered_keys
    """
    pass


class NeedTotal(Fact):
    """
    NeedTotal(value)
    Represents the number of required Need facts.
    Used to check if all needs were delivered.
    """
    pass

class PavilionLoad(Fact):
    """
    PavilionLoad(pavilion_id, total, counted_needs)
    Represents the calculated total number of bouquets needed by one pavilion.
    """
    pass

class ColorLoad(Fact):
    """
    ColorLoad(color, total, counted_needs, load_items)
    Represents a package of needs with the same color from different flower types.
    """
    pass