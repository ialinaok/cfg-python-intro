# let's convert 'CodeFirstGirls' to separated by hyphens

delimiter = ''

for char in 'CodeFirstGirls':
    delimiter = delimiter + char + '-'

print(delimiter)

result = delimiter.rstrip('-')

print(result)