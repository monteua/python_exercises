names = ["Michele", "Robin", "Sara", "Michele"]

sets_dup = set()
list_dup = list()

def list_duplicates():
    for name in names:
        if name not in list_dup:
            list_dup.append(name)


def sets_duplicates():
    #sets_dup.add(names)
    #sets_dup = set(names)
    for name in names:
        sets_dup.add(name)

list_duplicates()
print list_dup

sets_duplicates()
print sets_dup