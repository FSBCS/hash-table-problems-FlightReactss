def count_subarrays_with_sum(arr, target_sum):
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}

    for num in arr:
        current_sum += num
        if (current_sum - target_sum) in prefix_sums:
            count += prefix_sums[current_sum - target_sum]
        if current_sum in prefix_sums:
            prefix_sums[current_sum] += 1
        else:
            prefix_sums[current_sum] = 1

    return count