def sac(val):
    pieces = [x.strip() for x in val.split('/')]
    rjoin = '/'.join(pieces)
    return val

# route.apply(sac)