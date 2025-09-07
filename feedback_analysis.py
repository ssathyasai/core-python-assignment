def positive_feedback_percentage(ratings):
    if not ratings:
        return 0
    positive_count = sum(1 for r in ratings if r >= 4)
    return (positive_count / len(ratings)) * 100

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(f"Positive Feedback: {positive_feedback_percentage(ratings)}%")
