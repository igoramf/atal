def getPos(s):
    return s.count("+") - s.count("-")

def getUnk(s):
    return s.count("?")

def calc_prob(poss, total):
    count = 0
    for p in poss:
        if getPos(p) == total:
            count += 1
    
    return count / len(poss)

def solve(s1, s2):
    s1_pos = getPos(s1)

    s2_unk = getUnk(s2)
    s2_cleaned = s2.replace("?", "")

    poss = []

    def backtrack(unk_total, unk_idx, path, s):
        if unk_total == unk_idx:
            s_copy = s
            s_copy += "".join(path[:])
            poss.append(s_copy)
            return

        path.append("+")
        backtrack(unk_total, unk_idx + 1, path, s)
        path.pop()

        path.append("-")
        backtrack(unk_total, unk_idx + 1, path, s)
        path.pop()

    backtrack(s2_unk, 0, [], s2_cleaned)

    return calc_prob(poss, s1_pos)

def main():
    s1 = input()
    s2 = input()

    print(f"{solve(s1, s2):.12f}")


if __name__ == "__main__":
    main()