import json
import random
import timeit


def runtest():
    questions = None
    with open("questions.json", mode="r", encoding="utf-8") as f:
        questions = json.load(f)

    random.shuffle(questions)
    right = 0
    wrong = 0
    skipped = 0
    mode = (
        input(
            "Please select mode: 'exam' (exam simulation, u have 55 qns in 45 min), 'hard' (33 qns), 'survivor' (110+ qns) >>> "
        )
        .lower()
        .strip()
    )
    if mode == "exam":
        questions = questions[:55]
    elif mode == "hard":
        questions = questions[:33]
    elif mode == "survivor":
        resure = (
            input(
                "\n\tWARNING!!!\n \nYou are about to start the test in survivor mode! \nIn this mode every skipped qn is -1 point!\n \n\tAre  you sure?? \n \ntype 'YES' (yes, bring it on!!) or 'NO' (no, I want my Mommy!)>>> "
            )
            .lower()
            .strip()
        )
        if resure == "yes":
            pass
        else:
            return "\n\tMommy is here, try again\n"
        print("\n\tMay the knowledge be with you...\n")
    else:
        return "Smth is wrong! Try again"

    print(
        "\n   Answer the qns with 't' (true), 'f' (false), or press Enter to skip. You can terminate the attempt by answering 'e' (exit)\n"
    )
    counter = 0
    start = timeit.default_timer()

    for qn, ans in questions:
        answer = None
        while answer not in ["t", "f", "e", ""]:
            answer = input(f"{counter+1}) {qn} >>> ").lower().strip()
            if answer == "true":
                answer = "t"
            elif answer == "false":
                answer = "f"
            elif answer == "exit":
                answer = "e"

        if answer == "e":
            print("\n\tExiting...\n")
            break
        elif answer == ans:
            right += 1
            print("\n\tCorrect!\n")
        elif answer == "":
            skipped += 1
            print(f"\n\tSkipped! The correct answer is {ans}\n")
        else:
            wrong += 1
            print("\n\tIncorrect!\n")
        counter += 1

    stop = timeit.default_timer()
    score = (right - wrong - skipped) if mode == "survivor" else (right - wrong)
    return f"""
_____________________
RESULTS

Your score is: {score} point(s).
\tGrade: '{score * 31 / counter:.2f}'
\tRight ones {right}. Wrong ones {wrong}. Skipped ones {skipped}. Overall qns {counter}.
\tTIME: {(stop - start) / 60:.2f} minutes. Avrg time per qn: {(stop - start) / counter:.2f} sec.
\tMode: '{mode}'"""


print(runtest())
