from experta import Rule, MATCH, TEST, AS, NOT

from facts.facts import Pavilion, Need, PavilionLoad, ColorLoad, MaxLoad


class MaxLoadRules:

    # ==========================================
    # PAVILION LOAD CALCULATION
    # كل احتياجات جناح واحد
    # ==========================================

    @Rule(
        Pavilion(id=MATCH.pid),
        NOT(PavilionLoad(pavilion_id=MATCH.pid)),
        salience=1000
    )
    def initialize_pavilion_load(self, pid):
        self.declare(
            PavilionLoad(
                pavilion_id=pid,
                total=0,
                counted_needs=(),
                load_items=()
            )
        )

    @Rule(
        AS.load_fact << PavilionLoad(
            pavilion_id=MATCH.pid,
            total=MATCH.total,
            counted_needs=MATCH.counted_needs,
            load_items=MATCH.load_items
        ),

        Need(
            pavilion_id=MATCH.pid,
            flower_type=MATCH.flower_type,
            color=MATCH.color,
            quantity=MATCH.quantity
        ),

        TEST(lambda pid, color, counted_needs:
             (pid, color) not in counted_needs),

        salience=990
    )
    def add_need_to_pavilion_load(
        self,
        load_fact,
        pid,
        total,
        counted_needs,
        load_items,
        flower_type,
        color,
        quantity
    ):
        new_total = total + quantity
        new_counted_needs = counted_needs + ((pid, color),)
        new_load_items = load_items + ((pid, flower_type, color, quantity),)

        self.retract(load_fact)

        self.declare(
            PavilionLoad(
                pavilion_id=pid,
                total=new_total,
                counted_needs=new_counted_needs,
                load_items=new_load_items
            )
        )

    # ==========================================
    # COLOR LOAD CALCULATION
    # كل الاحتياجات التي تملك نفس اللون
    # ==========================================

    @Rule(
        Need(color=MATCH.color),
        NOT(ColorLoad(color=MATCH.color)),
        salience=1000
    )
    def initialize_color_load(self, color):
        self.declare(
            ColorLoad(
                color=color,
                total=0,
                counted_needs=(),
                load_items=()
            )
        )

    @Rule(
        AS.color_load_fact << ColorLoad(
            color=MATCH.color,
            total=MATCH.total,
            counted_needs=MATCH.counted_needs,
            load_items=MATCH.load_items
        ),

        Need(
            pavilion_id=MATCH.pid,
            flower_type=MATCH.flower_type,
            color=MATCH.color,
            quantity=MATCH.quantity
        ),

        TEST(lambda pid, color, counted_needs:
             (pid, color) not in counted_needs),

        salience=990
    )
    def add_need_to_color_load(
        self,
        color_load_fact,
        color,
        total,
        counted_needs,
        load_items,
        pid,
        flower_type,
        quantity
    ):
        new_total = total + quantity
        new_counted_needs = counted_needs + ((pid, color),)
        new_load_items = load_items + ((pid, flower_type, color, quantity),)

        self.retract(color_load_fact)

        self.declare(
            ColorLoad(
                color=color,
                total=new_total,
                counted_needs=new_counted_needs,
                load_items=new_load_items
            )
        )

    # ==========================================
    # MAX LOAD UPDATE
    # ==========================================

    @Rule(
        AS.max_fact << MaxLoad(value=MATCH.current_max),

        PavilionLoad(
            pavilion_id=MATCH.pid,
            total=MATCH.total,
            counted_needs=MATCH.counted_needs,
            load_items=MATCH.load_items
        ),

        TEST(lambda total, current_max:
             total > current_max),

        salience=980
    )
    def update_max_load_from_pavilion(
        self,
        max_fact,
        current_max,
        pid,
        total,
        counted_needs,
        load_items
    ):
        self.retract(max_fact)

        self.declare(
            MaxLoad(value=total)
        )