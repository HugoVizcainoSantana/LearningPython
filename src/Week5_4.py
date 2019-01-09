import random


def launch():
    return random.choice(["C", "X"])


def match_sequence(seq):
    history = launch()
    while seq not in history:
        history += launch()
    print(history)
    print("Played " + str(len(history)) + " times")


def match_sequence_compete(seq1, seq2):
    print("\n\nCompeting!")
    history = ""
    winner = None
    ret = None
    while winner is None:
        history += launch()
        if seq1 in history:
            winner = seq1
            ret = 0
        if seq2 in history:
            winner = seq2
            ret = 1

    print("History\n\t" + history)
    print("Winner\n\t" + winner)
    print("Played " + str(len(history)) + " times")

    return ret


def match_tournament(seq1, seq2, rounds=10):
    print("\n\n\nTournament!")
    wins = [0, 0]
    for i in range(rounds):
        wins[match_sequence_compete(seq1, seq2)] += 1
    return list(zip([seq1, seq2], wins))


match_sequence("CCX")

match_sequence_compete("CCX", "XXX")

print(match_tournament("CXCX", "CCCC"))
