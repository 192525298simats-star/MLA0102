import math

def alphabeta(depth, nodeIndex, isMax, scores, height, alpha, beta):

    # Leaf node
    if depth == height:
        return scores[nodeIndex]

    if isMax:
        best = -math.inf

        for i in range(2):
            value = alphabeta(depth + 1,
                              nodeIndex * 2 + i,
                              False,
                              scores,
                              height,
                              alpha,
                              beta)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alphabeta(depth + 1,
                              nodeIndex * 2 + i,
                              True,
                              scores,
                              height,
                              alpha,
                              beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


scores = [3, 5, 2, 9, 12, 5, 23, 23]
height = 3

result = alphabeta(0, 0, True, scores, height, -math.inf, math.inf)

print("The optimal value is:", result)
