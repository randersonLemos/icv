import pathlib


class ICV:
    def __init__(self, nr_valves):
        self.nr_valves = nr_valves
        self.valve = None

    def binary(self, *operational_conditions):
        from .valve_binary import Valve_Binary
        self.valve = Valve_Binary(*operational_conditions)
        return [self.valve.operational_rule()]*self.nr_valves

    def incremental(self, operational_conditions, actions, conditionals):
        from .valve_incremental import Valve_Incremental
        self.valve = Valve_Incremental(operational_conditions, actions, conditionals)
        return [self.valve.operational_rule()]*self.nr_valves

    def repr(self):
        return self.valve.repr()

    def write(self, path_to_inf):
        path = pathlib.Path(path_to_inf)
        with path.open('w') as handle:
            handle.write(self.repr())

