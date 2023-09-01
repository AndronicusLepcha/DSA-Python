def conquer(arr, si, mid, ei):
    new_arr = []
    idx1 = si
    idx2 = mid + 1

    while idx1 <= mid and idx2 <= ei:
        if arr[idx1] >= arr[idx2]:
            new_arr.append(arr[idx2])
            idx2 = idx2 + 1
        else:
            new_arr.append(arr[idx1])
            idx1 = idx1 + 1

    while idx1 <= mid:
        new_arr.append(arr[idx1])
        idx1 = idx1 + 1
    
    while idx2 <= ei:
        new_arr.append(arr[idx2])
        idx2 = idx2 + 1

    return new_arr

def divide(arr, si, ei):
    if si >= ei:
        return arr[si:ei + 1]  # Return a single-element or empty array
    mid = (si + ei) // 2
    left_half = divide(arr, si, mid)
    right_half = divide(arr, mid + 1, ei)
    return conquer(left_half + right_half, 0, len(left_half) - 1, len(left_half) + len(right_half) - 1)

arr = [12, 54, 76, 77, 11, 6, 7]
si = 0
ei = len(arr) - 1
sorted_arr = divide(arr, si, ei)
print(sorted_arr)
