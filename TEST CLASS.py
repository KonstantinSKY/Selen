def check(a):
    print(a)
    for i in a:
        if i == "12:00:00" or "00:00:00":
            print(len(i))


check(["12:00:00", "23:59:59", "00:00:00"])
