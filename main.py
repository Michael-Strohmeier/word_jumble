import random

if __name__ == "__main__":
    words = ["word", "banana", "cat", "dog"]

    score = 0
    for word in words:
        answer = word
        shuffled_word = "".join(random.sample(word, len(word)))

        while answer == shuffled_word:
            shuffled_word = "".join(random.sample(word, len(word)))

        question_points = 5
        hint_available = True
        user_guess = ""

        print(f"\nSolve the jumble: {shuffled_word}\n")

        while user_guess != answer:
            user_guess = input("Enter guess (h to get a hint): ")

            if user_guess == "h" and hint_available:
                hint_available = False

                # score decay for asking for hint
                question_points *= 0.5

                hint = list("_" * len(answer))

                n = random.randint(0, len(answer) - 1)
                hint[n] = list(answer)[n]
                hint = "".join(hint)

                print(f"Hint: {hint}")

        score += question_points
        print(f"\nCurrent Score: {score}\n")
