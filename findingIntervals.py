def sort_key(interval):
    return interval[0]


def merge_intervals(intervals):
    # Sort intervals by start time using the sort_key function
    intervals.sort(key=sort_key)

    merged = []

    for interval in intervals:
        # If merged is empty or there is no overlap with the last interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge intervals by updating the end of the last interval
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Test the function
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]




# def merge_intervals(intervals):
#     # Sort intervals by start time
#     intervals.sort(key=lambda x: x[0])
#
#     merged = []
#
#     for interval in intervals:
#         # If merged is empty or there is no overlap with the last interval
#         if not merged or merged[-1][1] < interval[0]:
#             merged.append(interval)
#         else:
#             # Merge intervals by updating the end of the last interval
#             merged[-1][1] = max(merged[-1][1], interval[1])
#
#     return merged
#
#
# # Test the function
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# print(merge_intervals(intervals))  # Output: [[1,6], [8,10], [15,18]]