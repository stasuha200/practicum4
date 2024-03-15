score = list(map(int, input().split()))
kirill = score[0]
arina = score[1]
sergei = score[2]
if kirill >= arina and kirill >= sergei:
    print(kirill)
elif kirill <= arina and arina >= sergei:
    print(arina)
elif kirill <= sergei and arina <= sergei:
    print(sergei)
