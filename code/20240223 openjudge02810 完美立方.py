N = int(input())
list = []
for a in range(2, N + 1) :
    for b in range(2, a) :
        for c in range(b, a) :
            for d in range(c, a) :
                if a*a*a == b*b*b + c*c*c + d*d*d:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")