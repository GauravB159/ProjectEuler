from pelib.basic import timed, getPrimes
import time

@timed
def process(n):
    limit = 100_000_000
    all_primes = getPrimes(limit)
    primes = {x: True for x in all_primes}
    all_primes = [x for x in all_primes if x < 10000]
    sets = {}
    for i in all_primes:
        str_i = str(i)
        for j in all_primes:
            check_one = int(str_i + str(j))
            check_two = int(str(j) + str_i)
            if check_one in primes and check_two in primes:
                if i not in sets:
                    sets[i] = set()
                if j not in sets:
                    sets[j] = set()
                sets[i].add(j)
                sets[j].add(i)

    lens = sorted(
        [(len(sets[k]), k) for k in sets if len(sets[k]) >= n - 1], reverse=True
    )
    for len_ in lens:
        for item in sets[len_[1]]:
            intersection = sets[len_[1]].intersection(sets[item])
            for k in intersection:
                inner_intersection = intersection.intersection(sets[k])
                for j in inner_intersection:
                    inner_inner_intersection = inner_intersection.intersection(sets[j])
                    if len(inner_inner_intersection):
                        print(
                            f"The numbers are: {len_[1]}, {item}, {k}, {j}, {list(inner_inner_intersection)[0]}"
                        )
                        return (
                            len_[1] + item + k + j + list(inner_inner_intersection)[0]
                        )


process(5)
