costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for cost in costs:
    total_cost = total_cost + cost

medium_cost = total_cost / 7

print('total cost per week: {} and medium per day: {}'.format(total_cost, medium_cost))