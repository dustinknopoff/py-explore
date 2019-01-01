import numpy as np
import json
from matplotlib import pyplot as plt
from os import path
from datetime import datetime, timedelta

consts = {
    1: 2,
    2: 7,
    3: 30,
    4: 365,
    5: 1000
}


def set_questions():
    """
    Writes input text to a file `questions.txt`, separated by a new line.
    This will represent the questions to be asked
    """
    print("Please enter each of your questions separated by a new line, enter just 'q' to finish")
    with open('./questions.txt', 'w') as f:
        while 1:
            question = input()
            if question is 'q':
                break
            else:
                f.write(question)
                f.write("\n")
    with open('./data.json', 'w') as f:
        f.write("{}")


def enter_scores(check):
    """
    For every question in questions.txt, ask for an integer value and add to data.json
    :return: dictionary of questions to list of responses
    """
    if check:
        if (datetime.today() - timedelta(1)).strftime("%d%m%y") != datetime.fromtimestamp(
                path.getmtime('./data.json')).strftime("%d%m%y"):
            print("Whoops, you tried to enter a value twice in one day!")
            exit(1)
    print("Please enter your scores for today")
    with open("./data.json", 'r') as f:
        # Define 10 questions within the triple quotes separated by a new line
        questions = []
        with open('./questions.txt', 'r') as qs:
            questions = qs.read().split('\n')
        kv = json.load(f)
        for line in questions:
            if line is not '':
                answer = int(input(line))
                while answer < 0 or answer > 10:
                    print("Please enter a number between 0-10")
                    answer = int(input(line))
                if line not in kv:
                    kv[line] = [answer]
                else:
                    kv[line].append(answer)
    with open('./data.json', 'w') as f:
        json.dump(kv, f)
    print("Awesome! Thanks for adding your scores today")
    return kv


def show_graph(freq, kv):
    """
    Given a dictionary of questions and frequency, output a matplotlib graph of all questions
    :param freq: Number of data points to show
    :param kv: dictionary of questions to list of answers
    """
    plt.title('Scores')
    lst = []
    ln = 0
    for key in kv.keys():
        plt.subplot(111)
        if freq != 1000:
            ln = len(kv[key][:freq])
            mx = len(kv[key][:freq])
            rng = range(0, len(kv[key][:freq]))
            most = list(reversed(kv[key][:freq]))
        else:
            ln = len(kv[key])
            rng = range(0, len(kv[key]))
            mx = len(kv[key])
            most = list(reversed(kv[key]))
        for i in rng:
            lst.append((datetime.now() - timedelta(days=i)).strftime('%b, %d %Y'))
        x = np.arange(0, mx)
        y = np.array(most)
        plt.plot(x, y, label=key.replace("?", ""))
    plt.legend()
    plt.xticks(range(0, ln), list(reversed(lst)), rotation=45)
    plt.xlabel('Day')

    plt.show()
    should_save = input("Would you like to save this graph?\n1) yes\n2) no\n")
    if should_save is '1':
        plt.savefig('latest.png')


if __name__ == '__main__':
    print("Welcome! This is a program to help keep track of and visualize things you find important"
          " everyday")
    yes = False
    while 1:
        print("Is this your first time?\n1) yes\n2) no")
        is_first = input()
        if int(is_first):
            if int(is_first) == 1:
                yes = True
                set_questions()
            break
        else:
            print("Please enter 1 or 0")
    kv = enter_scores(yes)
    while 1:
        print("How would you like to see this data?\n"
              "1) Past 2 Days\n"
              "2) This Week\n"
              "3) This Month\n"
              "4) This Year\n"
              "5) All Time")
        freq = input()
        if int(freq):
            show_graph(consts[int(freq)], kv)
            break
        else:
            print("Please enter 1 or 0")
