def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError("Length can't be more than series length or length needs to be greater than 0")
    
    return [series[i: i+length] for i in range(0, len(series) - length + 1)]
