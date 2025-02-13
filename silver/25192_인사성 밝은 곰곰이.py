n = int(input())
say_hi_people = set()
count = 0
for _ in range(n):
    s = input()
    
    if s == "ENTER":
        say_hi_people = set()
    else:
        if s not in say_hi_people:
            say_hi_people.add(s)
            count += 1
print(count)