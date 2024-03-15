score = list(map(int, input().split(':')))
team1 = score[0]
team2 = score[1]
if team1 > team2:
    print(1)
elif team1 < team2:
    print(2)
else:
    print(0)
