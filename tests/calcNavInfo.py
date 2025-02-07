print("Show informations about the current navigation's group")
# length = int(input('Number of values (total): '))
limit = int(input('Limit of values per view: '))
index = int(input('Index of current group: '))
print('calculating...')

def getNavigationInfo(length:int, limit:int, index:int) -> tuple[int, int, int, int, int]:
    """
    calcula os valores inicial, final e número de intervalos a partir das informações de length, limit e index.
    Realiza o tratamento de limit e index de acordo com length
    
    retorna start, end, limit, index, num_intervals
    """

    if not (0 < limit < length):
        limit = length

    num_intervals = (length // limit) + (length % limit != 0)

    if length == 0:
        return 0, 0, 0, num_intervals
    
    if index >= num_intervals:
        index = num_intervals - 1

    start = index * limit + 1 # just works if length is bigger than one
    end = (index + 1) * limit if (index + 1 < num_intervals) else length

    return start, end, limit, index, num_intervals

values = [1,2,3, 4,5,6, 7,8]
length = len(values)
start, end, limit, index, num_intervals = getNavigationInfo(length, limit, index)

print(
    '',
    f'Values: {values[start-1:end]}',
    f'Number of values: {length}',
    f'Number of intervals (with limit {limit}): {num_intervals}',
    f'Interval: ' + (str(index+1) if length else "it hasn't intervals"),
    f'Start: {start}',
    f'End: {end}',
    sep='\n'
)