class ICV:
    def __init__(self, nr_valves):
        self.nr_valves = nr_valves


    def binary(self, *operational_conditions):
        from .device_binary import device_binary
        return [device_binary(*operational_conditions)]*self.nr_valves
