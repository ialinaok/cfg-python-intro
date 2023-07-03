import csv

with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    heights = []

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)
        
shortest_height = max(heights)
print(shortest_height)
