def getR():
    while True:
        try:
            s_size = input("How many tuples are in your relation: ")
            size = int(s_size)
            if size  <= 0:
                raise ValueError("Size must be positive")
            break
        except ValueError:
            print("Number of tuples must be positive")
    R = []
    for count in range(size):
        while True:
            try:
                temp = input(f"Provide relation {count + 1} in form 'a,b' (no parentheses, spaces optional): ")
                to_add = tuple(map(int, temp.split(',')))
                if len(to_add) != 2:
                    raise ValueError("Please provide exactly two integers")
                R.append(to_add)
                break
            except ValueError:
                print("Invalid format. Relation must be in form 'a,b' with two integers")
    return R

"""
Consider:
{(1, 3), (1, 4), (2, 1), (3, 2)}
"""


def calculateTransitiveClosure(R):
    ret = set(R)
    new_el = True
    while new_el:
        new_el = False
        for i in ret.copy():
            for j in ret.copy():
               if i[1] == j[0]:
                   if (i[0], j[1]) not in ret:
                       temp = (i[0], j[1])
                       ret.add(temp)
                       new_el = True
    return ret



if __name__ == "__main__":
    run = True
    print("Welcome! This program can calculate the transitive closure of a given set relation. Enjoy!")
    print("")
    while run:
        R = getR()
        res = calculateTransitiveClosure(R)
        print(f"Transitive closure; contains {len(res)} relations: {res}")
        r_check = input("Press 'r' to run again, or any other key to exit: ")
        if r_check.lower() == "r":
            continue
        else:
            run = False
