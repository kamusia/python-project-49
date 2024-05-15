from brain_games.cli import greeting, get_answer

max_score = 3


def game_run(game):
    name = greeting()
    print(game.rules)

    score = 0

    while score < max_score:

        question, correct = game.run_game()

        answer = get_answer(question)

        if answer != correct:
            print(f"{answer} is wrong answer ;(.Correct answer was {correct}.")
            print(f"Let's try again, {name}!")
            break
        print("Correct!")
        score += 1
    if score == 3:
        print(f"Congratulations, {name}!")