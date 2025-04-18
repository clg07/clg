document1 = "The quick brown fox jumped over the lazy dog"
document2 = " The lazy dog slept in the sun"

doc1 = "apple mango banana"
doc2 = "apple banana"
doc3 = "apple orange"
term = sorted(set((document1+document2).lower().split(" ")))

for i in term:
    if i in document1 and i in document2:
        print(f"{i} -> Document 1 ({document1.lower().count(i)}),Document 2 ({document2.lower().count(i)})")
    elif i in document1:
        print(f"{i} -> Document 1 ({document1.lower().count(i)})")
    else:
        print(f"{i} -> Document 2 ({document2.lower().count(i)})")

def b_and():
    data = []
    if "apple" in doc1 and "banana" in doc1:
        data.append(1)
    if "apple" in doc2 and "banana" in doc2:
        data.append(2)
    if "apple" in doc3 and "banana" in doc3:
        data.append(3)
    return data
def b_or():
    data = []
    if "apple" in doc1 or "orange" in doc1:
        data.append(1)
    if "apple" in doc2 or "orange" in doc2:
        data.append(2)
    if "apple" in doc3 or "orange" in doc3:
        data.append(3)
    return data
def b_not():
    data = []
    if "orange" not in doc1:
        data.append(1)
    if "orange" not in doc2:
        data.append(2)
    if "orange" not in doc3:
        data.append(3)
    return data
print("Documents containing 'apple' AND 'banana': ",b_and())
print("Documents containing 'apple' OR 'orange': ",b_or())
print("Documents NOT containing 'orange': ",b_not())
