# import pretty_errors
import random
import numpy as np

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rows = 5
columns = 5

readonly_word_bank = (
    "AMUSEMENT", "TEA", "AUTUMN", "APPLES", "BLACK", "CANDY", "BATS", "TEST", "BOO", "CAT",
    "COSTUMES", "DRACULA", "EERIE", "EXCITEMENT", "FRANKENSTEIN", "FRIGHTEN",
    "GAMES", "GHOSTS", "GOBLIN", "HALLOWEEN", "HARVEST", "HAYRIDE", "MASK",
    "MONSTER", "MUMMY", "NIGHT", "OCTOBER", "ORANGE", "PARTY", "PRANK", "PUMPKINS",
    "SAFE", "SCARE", "SHADOWS", "SKELETON", "SPIDER", "SPOOKY", "TRICKORTREAT", "WITCH"
)
readonly_word_bank.sort(key=lambda s: len(s))

word_bank = []
for word in readonly_word_bank:
    word_bank.append([word, {np.array(0, 1), np.array(1, 0), np.array(1, 1)}])


def print_matrix(matrix):
    """Prints the matrix cleanly."""

    output = ""
    for row in matrix:
        for element in row:
            output += f"{element} "
        output += "\n"
    print(output)


def random_letter():
    """Returns a random letter from the alphabet."""

    return random.sample(alphabet)[0]


def randomized_letter_matrix(word_matrix):
    """returns the input matrix with all empty space replaced by random letters."""

    for row in word_matrix:
        for element in row:
            if word_matrix[row][element] == "":
                # wordMatrix[row][element] = random_letter()  # TODO: reactivate random letters
                word_matrix[row][element] = "."
    return word_matrix


def next_word():
    """returns next word from word_bank."""

    if len(word_bank) == 0:
        return None
    return word_bank[-1][0]

def new_direction(word):
    # TODO: what does this function do?
    if len(word_bank[-1][1]) < 1:
        word_bank.pop()
        return None
    direction = random.sample(word_bank[-1][1], 1)[0]
    word_bank[-1][1].discard(direction)
    return direction


def test_direction(row_index, column_index, word, direction):
    pass


# TODO: change direction variable to strings (horizontal, vertical, diagonal)
def word_check(word, direction, word_matrix):
    checklist = set()
    for row_index in range(rows):
        for column_index in range(columns):  # TODO: stop searching impossible positions (eg: bottom-right corner)

            possible = True

            for letter_index, letter in enumerate(word):

                if direction == np.array(0, 1):
                    if column_index - len(word) < 0:
                        possible = False
                        break

                    next_position = word_matrix[row_index][column_index + letter_index]
                    if next_position != "" and next_position != letter:
                        possible = False

                elif direction == np.array(1, 0):
                    if row_index - len(word) < 0:
                        possible = False
                        break

                    next_position = word_matrix[row_index + letter_index][column_index]
                    if np.all(next_position != "" and next_position != letter):
                        possible = False

                else:
                    if column_index - len(word) < 0 or row_index - len(word) < 0:
                        possible = False
                        break

                    next_position = word_matrix[row_index + letter_index][column_index + letter_index]
                    if next_position != "" and next_position != letter:
                        possible = False

            if possible:
                checklist.add((row_index, column_index))

    if len(checklist) < 1:
        return None
    pos = random.sample(checklist, 1)[0]
    return pos


def word_finder(word_matrix):
    word = next_word()
    if word is None:
        return None
    
    direction = new_direction(word)
    if direction is None:
        return word_finder(word_matrix)
    
    pos = word_check(word, direction, word_matrix)
    if pos is None:
        readonly_word_bank.discard(word)
        return word_finder(word_matrix)
    
    word_bank[-1][1].clear()
    return [word, direction, pos]


def insert_word(word, direction, starting_coordinate, word_matrix):
    position = np.asarray(starting_coordinate)

    for letter in word:
        word_matrix[position] = letter
        position += direction

    return word_matrix


def main():
    print(f"{readonly_word_bank}")
    word_matrix = np.zeros((rows, columns), dtype=str)
    while len(word_bank) > 0:
        info = word_finder(word_matrix)
        if info is None:
            break
        insert_word(info[0], info[1], info[2], word_matrix)

    word_matrix = randomized_letter_matrix(word_matrix)

    print_matrix(word_matrix)
    print(readonly_word_bank)

main()
