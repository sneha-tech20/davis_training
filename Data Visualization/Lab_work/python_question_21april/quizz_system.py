def quiz(file):
    score = 0

    with open(file, 'r') as f:
        for line in f:
            q, ans = line.strip().split(',')

            user = input(q + " ")

            if user.lower() == ans.lower():
                score += 1

    print("Score:", score)