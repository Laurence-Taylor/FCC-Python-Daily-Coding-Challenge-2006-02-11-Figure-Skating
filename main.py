def compute_score(judge_scores, *penalties):
    # Find maximum score and removed from the array
    max_score = max(judge_scores)
    judge_scores.remove(max_score)
    # Find minimum score and removed from the array
    min_score = min(judge_scores)
    judge_scores.remove(min_score)
    # Calculate score without penalties
    sum_score = sum(judge_scores)
    # Apply penalties
    if penalties:
        # Sum all possible penalties
        total_penalties = sum(penalties)
        # Apply penalties
        sum_score -= total_penalties
    return sum_score

if __name__ == '__main__':
    print(compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1))
    print()
    print(compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))