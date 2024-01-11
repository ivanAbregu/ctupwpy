from itertools import permutations

def get_people(arr):
    people = set()
    for x in arr:
        people.update(x)
    people.difference_update({'>','<'})
    return people

def ArrayChallenge(relations):
    result = 0
    people = get_people(relations)
    for perm in permutations(people):
        for rel in relations:
            x, y = (rel[0], rel[2]) if ">" in rel else (rel[2], rel[0])
            if perm.index(x) > perm.index(y):
                break
        else:
            result+=1
    return result
