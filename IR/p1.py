document1 = "The quick brown fox jumped over the lazy dog"
document2 = " The lazy dog slept in the sun"


term = sorted(set((document1+document2).lower().split(" ")))

for i in term:
    if i in document1 and i in document2:
        print(f"{i} -> Document 1 ({document1.lower().count(i)}),Document 2 ({document2.lower().count(i)})")
    elif i in document1:
        print(f"{i} -> Document 1 ({document1.lower().count(i)})")
    else:
        print(f"{i} -> Document 2 ({document2.lower().count(i)})")

