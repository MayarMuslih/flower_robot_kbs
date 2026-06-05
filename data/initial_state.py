from facts.facts import Grid, Warehouse, Pavilion, Need, NeedTotal, MaxLoad, State


initial_facts = [
    Grid(width=5, height=5),

    Warehouse(x=3, y=2),

    MaxLoad(value=0),
    NeedTotal(value=9),

    Pavilion(id=1, x=2, y=4, flower_type="rose"),
    Need(pavilion_id=1, flower_type="rose", color="red", quantity=2),
    Need(pavilion_id=1, flower_type="rose", color="pink", quantity=1),
    Need(pavilion_id=1, flower_type="rose", color="white", quantity=1),

    Pavilion(id=2, x=4, y=3, flower_type="tulip"),
    Need(pavilion_id=2, flower_type="tulip", color="red", quantity=3),
    Need(pavilion_id=2, flower_type="tulip", color="yellow", quantity=1),

    Pavilion(id=3, x=4, y=5, flower_type="orchid"),
    Need(pavilion_id=3, flower_type="orchid", color="purple", quantity=2),
    Need(pavilion_id=3, flower_type="orchid", color="pink", quantity=1),

    Pavilion(id=4, x=5, y=2, flower_type="goliat_rose"),
    Need(pavilion_id=4, flower_type="goliat_rose", color="gold", quantity=2),
    Need(pavilion_id=4, flower_type="goliat_rose", color="light_pink", quantity=2),

    State(
        robot_x=3,
        robot_y=1,
        load=(),
        load_count=0,
        steps=(),
        g=0,
        h=0,
        f=0,
        depth=0,
        visited_keys=((3, 1, (), ()),),
        delivered_keys=()
    )
]