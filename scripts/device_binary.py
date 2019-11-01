from dictionary.scripts.dictionary import Keywords as kw


def device_binary(*operational_conditions):
    outer = []
    for conditions in operational_conditions:
        iter_conditions = iter(conditions)
        inner = []
        while True:
            qty = next(iter_conditions)
            val = next(iter_conditions)
            stg = '{} __LAYER__ {} > {}'.format(kw.on_ctrllump(), qty, val)
            inner.append(stg)
            try:
                conditional = next(iter_conditions)
                inner.append(conditional)
            except StopIteration:
                inner.append(0.0)
                outer.append(tuple(inner))
                break
    return outer
