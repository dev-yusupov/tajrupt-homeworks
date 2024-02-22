import itertools

def main(list):
    permutations = itertools.permutations(list)

    for perm in permutations:
        print(perm)

print(main([1, 3, 4, 2, 5cls
            ]))