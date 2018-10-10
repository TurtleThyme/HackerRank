def plusMinus(arr):
    zeros = 0
    abovezeros = 0
    belowzeros = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        elif arr[i] > 0:
            abovezeros += 1
        else:
            belowzeros += 1
    print(abovezeros/len(arr))
    print(belowzeros/len(arr))
    print(zeros/len(arr))