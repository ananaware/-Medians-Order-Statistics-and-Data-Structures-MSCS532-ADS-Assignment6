import random


# ------------------------------
# RANDOMIZED QUICKSELECT
# ------------------------------
def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return randomized_quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return randomized_quickselect(highs, k - len(lows) - len(pivots))


# ------------------------------
# MEDIAN OF MEDIANS (DETERMINISTIC)
# ------------------------------
def deterministic_select(arr, k):

    if len(arr) <= 5:
        return sorted(arr)[k]

    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group)//2] for group in groups]

    pivot = deterministic_select(medians, len(medians)//2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return deterministic_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))


# ------------------------------
# TEST CODE
# ------------------------------
if __name__ == "__main__":

    data = list(map(int, input("Enter numbers separated by space: ").split()))
    k = int(input("Enter k (0-based index): "))

    print("Array:", data)
    print("k =", k)

    print("Randomized Quickselect result:", randomized_quickselect(data, k))
    print("Deterministic Select result:", deterministic_select(data, k))