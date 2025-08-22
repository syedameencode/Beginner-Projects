# Cal.py
def calculate_love_score(name1, name2):
    name = (name1 + name2).upper()
    count_true = 0
    count_love = 0
    for i in name:
        if i in ("T", "R", "U", "E"):
            count_true += 1
        if i in ("L", "O", "V", "E"):
            count_love += 1
    print(f"TRUE count: {count_true}")
    print(f"LOVE count: {count_love}")
    score = str(count_true) + str(count_love)
    print(f"Your love score is: {score}")

calculate_love_score("", "")