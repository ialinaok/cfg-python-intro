scores = [10, 33, 23, 19, 43, 8, 0]

print('Number of scores {}'.format(len(scores)))
print('Highest score {}'.format(max(scores)))
print('Lowest score {}'.format(min(scores)))

sorted_scores = sorted(scores)
desc_scores = list(reversed(sorted_scores))
print('All scores {}'.format(desc_scores))