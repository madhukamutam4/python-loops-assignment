import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 5x4 array with values between 50 and 100 (inclusive)
scores = np.random.randint(50, 101, size=(5, 4))

print("Scores Array:\n", scores)

# Score of the 3rd student in the 2nd subject
print("\nScore of 3rd student in 2nd subject:",
      scores[2, 1])

# All scores of the last 2 students
print("\nAll scores of the last 2 students:\n",
      scores[-2:, :])

#  Scores of first 3 students in subjects 2 and 3 only
print("\nScores of first 3 students in subjects 2 and 3:\n",
      scores[:3, 1:3])
# Column-wise mean (average per subject), rounded to 2 decimals
column_mean = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise Mean (per subject):\n", column_mean)

# Add curve using broadcasting
curve = np.array([5, 3, 7, 2])

curved_scores = scores + curve

# Ensure no score exceeds 100
curved_scores = np.clip(curved_scores, None, 100)

print("\nCurved Scores (max capped at 100):\n", curved_scores)

# Row-wise max (best subject score per student)
row_max = curved_scores.max(axis=1)
print("\nBest Subject Score per Student:\n", row_max)

# Min-Max Normalization per row
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)

print("\nNormalized Scores (0–1 per student):\n", normalized)

# Find index of single highest value in normalized array
flat_index = np.argmax(normalized)
row_index, col_index = np.unravel_index(flat_index, normalized.shape)

print("\nHighest normalized value location:")
print("Student index:", row_index)
print("Subject index:", col_index)

# Extract all scores strictly above 90
above_90 = curved_scores[curved_scores > 90]

print("\nScores strictly above 90:\n", above_90)