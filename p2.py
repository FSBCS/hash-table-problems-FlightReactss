def k_most_frequent(lst, k):
    if k == 0:
        return []

    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return [item for item, count in sorted_items[:k]]