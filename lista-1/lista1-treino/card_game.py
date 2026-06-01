def solve(a1, a2, b1, b2):
    sunnet = [a1,a2]
    slavic = [b1,b2]
    
    g_w = 0
    for i in range(len(sunnet)):
        for j in range(len(slavic)):
            s_w = 0
            b_w = 0
            a1 = sunnet[i]
            a2 = sunnet[1 - i]
            b1 = slavic[j]
            b2 = slavic[1 - j]

            if a1 > b1:
                s_w += 1
            elif b1 > a1:
                b_w += 1
    
            if a2 > b2:
                s_w += 1  
            elif b2 > a2:
                b_w += 1

            if s_w > b_w:
                g_w += 1


    return g_w
 

def main():
    rounds = int(input())
    sol = []

    for _ in range(rounds):
        a1, a2, b1, b2 = map(int, input().split())
        sol.append(solve(a1, a2, b1, b2))

    for s in sol:
        print(s)

if __name__ == "__main__":
    main()