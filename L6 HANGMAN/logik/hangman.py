from repository.state import get_current_state

def guess (word, choice, current_state):
    """
    builds a state based on the choice of the user
    :param word: what to guess
    :param choice: characther
    :return: state as Tuple
    """
    guessed_indexes = []
    current_guessed_indexes = current_state[2]

    found = False

    for idx in range(len(word)):
        if choice == word[idx] and idx not in current_guessed_indexes:
            guessed_indexes.append(idx)
            found = True

    tries = 1 if not found else 0
    guessed = 1 if found else 0

    return current_state[0] + tries, current_state[1] + guessed, current_state[2] + guessed_indexes


def win(states, word):
    if len(get_current_state(states)[2]) == len(word):
        return True

    # if get_current_state(states)[0] > max_tries:
    #     return False
# def guess (word, char, current_state):
#     found_indexes = []
#
#     for idx in range(len(word)):
#         if char == word[idx] and idx not in current_state[2]:
#             found_indexes.append(idx)
#
#     tries = 1 if len(found_indexes) == 0 else 0
#
#     return (current_state[0] + tries,
#             current_state[1] + len(found_indexes),
#             current_state[2] + found_indexes)
#
# def end (word, current_state,max_tries):
#     if current_state[0]< max_tries:
#         if current_state[1] == len(word):
#             return True
#     else:
#         return False