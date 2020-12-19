def cyclotomic_set(base, power, *args, **kwargs):
    mod_val = base ** power - 1

    seen = []
    k_values = args if len(args) > 0 else list(range(1, mod_val))
    sets = dict()
    for k in k_values:
        if k not in seen:
            val = k
            k_set = []
            while val not in k_set:
                seen.append(val)
                k_set.append(val)
                val = val * base % mod_val
            sets[k] = k_set

    print(sets)
    return sets
