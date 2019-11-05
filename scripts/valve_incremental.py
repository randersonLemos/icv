from dictionary.scripts.dictionary import Keywords as kw


class Valve_Incremental:
    def __init__(self, operational_conditions, actions, conditionals):
        self.operational_conditions = list(operational_conditions)
        self.conditionals = list(conditionals)
        self.actions = list(actions)

    def operational_rule(self):
        operational_conditions = {}
        for operational in self.operational_conditions:
            lst = []
            lst += list(zip(operational[1:-1],operational[2:]))
            operational_conditions[operational[0]] = lst[::-1]

        outer = []
        actions = self.actions[::-1]
        while self._has_element(operational_conditions):
            inner = []
            stg = ''
            conditionals = self.conditionals[::-1]
            for key in operational_conditions:
                interval = operational_conditions[key].pop()
                stg = '{{{} __LAYER__ {} > {} AND {} __LAYER__ {} < {}}}'.format(kw.on_ctrllump(), key,
                        interval[0], kw.on_ctrllump(), key, interval[1])
                inner.append(stg)
                try:
                    inner.append(conditionals.pop())
                except IndexError:
                    inner.append(actions.pop())
                    outer.append(tuple(inner))
        return outer

    def _has_element(self, dic):
        if list(dic.values())[0]:
            return True
        else:
            return False


    def repr(self):
        outer = '###BINARY VALVE###\n'
        #for conditions in self.oc:
        #    iter_conditions = iter(conditions)
        #    inner = 'Trigger\n'
        #    while True:
        #        inner += '  with {} at {}\n'.format(
        #                  next(iter_conditions)
        #                , next(iter_conditions)
        #                )
        #        try:
        #            inner += '  {}\n'.format(next(iter_conditions))
        #        except StopIteration:
        #            outer += inner
        #            outer += '  do 0.0\n'
        #            break
        return outer
