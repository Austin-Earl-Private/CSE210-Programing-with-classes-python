class Guesser:

    def __init__(self, word):
        self._word = word
        self._wrong_guesses = 0
        self._correct_letters = []
        # print("DEBUG: WORD IS " + self._word)

    def guess_letter(self, letter):
        for char in self._word:
            if char == letter:
                self._correct_letters.append(letter)
                return True
        self._wrong_guesses += 1
        return False

    def get_wrong_guesses(self):
        return self._wrong_guesses

    def checkForFullWord(self):
        for char in self._word:
            if char not in self._correct_letters:
                return False
        return True

    def show_correct_letters(self):
        output = ""
        for char in self._word:
            if char in self._correct_letters:
                output += char + ' '
            else:
                output += '_ '
        print(output + '\n')
