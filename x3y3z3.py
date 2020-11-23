def generate(n):
    d = {i:set({}) for i in range(101)}
    for x in range(n+1):
        for y in range(x,n+1):
            for z in range(int(1.5*(n+1))):
                v = x**3 + y**3 - z**3
                if v <= 100 and v > 0:
                    d[v].add(tuple(sorted((x,y,-z))))
                if v < 0  and v >= -100:
                    d[-v].add(tuple(sorted((-x,-y,z))))
    for x in range(6):
        for y in range(6):
            for z in range(6):
                v = x**3 + y**3 + z**3
                if v <= 100:
                    d[v].add(tuple(sorted((x,y,z))))
    return {k: v for k, v in d.items() if v != set({})}

def unreachable(n):
    d = generate(n)
    return set(range(101)) - set(d.keys())
