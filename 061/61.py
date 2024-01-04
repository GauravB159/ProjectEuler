from pelib.basic import timed

@timed
def process():
    series = { 3: [], 4: [], 5: [], 6: [], 7: [], 8: [] }
    for i in range(200):
        series[3].append(int(i * (i + 1) / 2))
        series[4].append(int(i * i))
        series[5].append(int(i * (3 * i - 1) / 2))
        series[6].append(int(i * (2 * i - 1)))
        series[7].append(int(i * (5 * i - 3) / 2))
        series[8].append(int(i * (3 * i - 2)))
    
    for serie in series:
        series[serie] = [x for x in series[serie] if len(str(x)) == 4]
    
    mappedSeries = { 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {} }
    for serie in series:
        for term in series[serie]:
            prefix = str(term)[:2]
            suffix = str(term)[2:]
            if prefix not in mappedSeries[serie]:
                mappedSeries[serie][prefix] = []
            mappedSeries[serie][prefix].append(suffix)


    def recurse(level, term, remaining_levels, visited):
        if term == '81' and not visited:
            pass
        if not remaining_levels:
            return
        if term not in mappedSeries[level]:
            return
        remaining_levels = remaining_levels.copy()
        remaining_levels.remove(level)
        for next_term in mappedSeries[level][term]:
            if not remaining_levels and next_term == visited[0][:2]:
                result = [*visited, f"{term}{next_term}"]
                print(sum([int(x) for x in result]))
                return
            for next_level in remaining_levels:
                if next_term not in mappedSeries[next_level]:
                    continue
                recurse(next_level, next_term, remaining_levels, [*visited, f"{term}{next_term}"])

    for serie in mappedSeries[3]:
        recurse(3, serie, set([3, 4, 5, 6, 7, 8]), [])

process()