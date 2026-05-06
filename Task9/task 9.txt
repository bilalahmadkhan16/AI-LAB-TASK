import math

def minimax(depth, index, isMax, arr, maxDepth):
    
    # Jab last level (leaf node) par pohanch jayein
    if depth == maxDepth:
        return arr[index]

    # Agar maximizer ka turn hai
    if isMax == True:
        left = minimax(depth + 1, index * 2, False, arr, maxDepth)
        right = minimax(depth + 1, index * 2 + 1, False, arr, maxDepth)
        
        if left > right:
            return left
        else:
            return right

    # Agar minimizer ka turn hai
    else:
        left = minimax(depth + 1, index * 2, True, arr, maxDepth)
        right = minimax(depth + 1, index * 2 + 1, True, arr, maxDepth)
        
        if left < right:
            return left
        else:
            return right


# Main program
values = [3, 5, 2, 9, 3, 5, 2, 9]

# Tree ki depth nikalna
depth = int(math.log2(len(values)))

result = minimax(0, 0, True, values, depth)

print("Optimal value is:", result)