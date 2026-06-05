import compatibility

from experta import KnowledgeEngine

from rules.directed_movement_rules import DirectedMovementRules
from rules.load_rules import LoadRules
from rules.unload_rules import UnloadRules
from rules.constraint_rules import ConstraintRules
from rules.goal_rules import GoalRules
from rules.print_rules import PrintRules
from rules.maxload_rules import MaxLoadRules


class FlowerRobotEngine(
    MaxLoadRules,
    DirectedMovementRules,
    LoadRules,
    UnloadRules,
    ConstraintRules,
    GoalRules,
    PrintRules,
    KnowledgeEngine
):
    pass