def slices(series, N):
    if N > len(series):
        raise ValueError("The split size is too large!")
    if N < 1:
        raise ValueError("Invalid split size!")

    series   = [int(c) for c in series]
    n_splits = len(series)-N+1

    split = []
    for i in range(n_splits):
        split.append(series[i:N+i])

    return split
