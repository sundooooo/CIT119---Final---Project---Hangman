import random
import requests
from bs4 import BeautifulSoup

def words():
    response = requests.get("https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt")
    soup = BeautifulSoup(response.text, "html.parser")
    word_list = [word for word in response.text.splitlines() if len(word) > 4]
    answer = random.choice(word_list)
    return answer

def hangman(guesses):
    hangman_stage = {
                  0: ("         ------------",
                       "        |          |",
                       "        |          ",
                       "        |          ",
                       "        |          ",
                      "     -------------------------"),
                  1: ("         ------------",
                       "        |          |",
                       "        |          o ",
                       "        |          ",
                       "        |          ",
                      "     -------------------------"),
                  2: ("         ------------",
                       "        |          |",
                       "        |          o ",
                       "        |          |",
                       "        |          ",
                      "     -------------------------"),
                  3: ("         ------------",
                       "        |          |",
                       "        |          o ",
                       "        |         /|",
                       "        |          ",
                      "     -------------------------"),
                  4: ("         ------------",
                       "        |          |",
                       "        |          o ",
                       "        |         /|\\",
                       "        |          ",
                      "     -------------------------"),
                  5: ("         ------------",
                       "        |          |",
                       "        |          o ",
                       "        |         /|\\",
                       "        |         / ",
                      "     -------------------------"),
                  6: ("         ------------",
                       "        |          |",
                       "        |          o ",
                       "        |         /|\\",
                       "        |         / \\",
                      "     -------------------------")}
    for line in hangman_stage[guesses]:
        print(line)
def game(answer):
    wrong_guesses = 0
    guess_list = []
    hangman(wrong_guesses)
    hint = ["_"] * len(answer)
    print(" ".join(hint))
    while wrong_guesses < 6 and "_" in hint:
        guess = input("enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("enter a valid letter")
            continue
        if guess in guess_list:
            print("you already guessed that")
            continue
        guess_list.append(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    hangman(wrong_guesses)
                    print(" ".join(hint))
        else:
            wrong_guesses += 1
            hangman(wrong_guesses)
            print(" ".join(hint))
        if "_" not in hint:
            print(f"you win!!!!!!!!!!")
            return True
        elif wrong_guesses == 6:
            print(f"game over! the word was: {answer}")
            return False

def main():
    wins = 0
    losses = 0

    while True:
        answer = words()
        won = game(answer)
        games = wins + losses + 1

        if won:
            wins += 1
        else:
            losses += 1

        games = wins + losses
        win_pct = (wins / games) * 100
        print("                         ")
        print("*************************")
        print("*       STATISTICS      *")
        print(f"*  Wins:           {wins:<4} *")
        print(f"*  Losses:         {losses:<4} *")
        print(f"*  Games:          {games:<4} *")
        print(f"*  Win %:          {win_pct:<4.1f} *")
        print("*************************")

        play_again = input("\nplay again? (y/n): ").lower()
        if play_again != "y":
            print("thanks for playing!")
            break

main()