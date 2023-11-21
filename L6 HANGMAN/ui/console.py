from logik.hangman import guess, win
from repository.state import get_current_state, set_initial_state
from repository.state import add_state


def hide_word(word, guesses):
    new_word = ''

    for idx in range(len(word)):
        if idx in guesses:
            new_word += word[idx]
        else:
            new_word += '_'

    return new_word


def state(states, word, max_tries):
    current_state = get_current_state(states)
    """
    max_tries: 10
    guessed: 3
    tries_left: 2
    M_A_S____
    """

    return f'max_tries:\t{max_tries}\nguessed:\t{current_state[1]}\ntries_left:\t\
    {max_tries - current_state[0]}\n{hide_word(word, current_state[2])}'


def run(word, states, max_tries):
    set_initial_state(states, word)

    print(state(states, word, max_tries))

    while True:
        choice = input('choice= ')

        new_state = guess(word, choice, get_current_state(states))
        add_state(states, new_state)

        if get_current_state(states)[0] > max_tries:
            print('You Lost')
            break

        if win(states, word):
            print('OK')
            break

        print(state(states, word, max_tries))

