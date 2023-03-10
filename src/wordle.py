import random

from utils import print_error, print_regular, print_success, print_warning

random.seed(42)


class Wordle:
    """Wordle Game
    """

    def __init__(self, file_path: str, word_len: int = 5, limit: str = 10000):
        """Constructor
        """
        self.word_len = word_len
        self.words = self.generate_word_frequency(file_path, word_len, limit)



    def generate_word_frequency(self, file_path: str, word_len: int, limit: int):
        """Generate Word Frequency

        :param file_path: text file that have many words.
        :param word_len: set the letter of words, defaults to 5.
        :param limit: number of words to chose, defaults to 1000.
        :return: list of words with {word_len} letter.
        """

        # Build Data
        words_freq = []
        with open(file_path) as f:
            for line in f:
                word, frequency = line.split(', ')
                words_freq.append((word, int(frequency)))

        # Sort Data
        words_freq = sorted(words_freq, key=lambda w_freq: w_freq[1], reverse=True)

        # Limit Data
        words_freq = words_freq[:limit]

        # Drop Frequency Data
        words = [w_freq[0] for w_freq in words_freq]

        # {word_len} letters words
        words = [w for w in words if len(w) == word_len]
        # Secend way: words = list(filter(lambda w: len(w) == word_len, words))

        return words

    def run(self):
        # Random Word
        selected_word = random.choice(self.words)
        selected_word = selected_word.upper()

        # Start Game
        num_try = 0
        success = True

        while True:
            guess_word = input(f'\n{num_try + 1} >> Enter a {self.word_len} letter word (or q to exit): ')
            guess_word = guess_word.upper()

            if guess_word == 'Q':
                print_warning(f"\n\t*** The word is: {selected_word} ***\n\n")
                break

            if len(guess_word) != 5:
                msg = (f'\t*** Enter a {self.word_len} letter word ***\n\t*** You enter a {len(guess_word)} letter! ***')
                print_error(msg)
                continue

            if guess_word.lower() not in self.words:
                print_warning(f"\t*** Word {guess_word} is not valid ***")
                continue

            for w_letter, g_letter in zip(selected_word, guess_word):
                if w_letter == g_letter:
                    print_success(f"\t {g_letter} ", end='')
                elif g_letter in selected_word:
                    print_warning(f"\t {g_letter} ", end='')
                else:
                    print_regular(f"\t {g_letter} ", end='')


            if guess_word == selected_word:
                print_success(f"\n\t*** Congajulation ***\n")
                print('\n')
                success = True
                break

            print('\n')
            num_try += 1
            if num_try > 5:
                break

            if not success:
                print_error(f"\n\t*** You didn't guess ***\n\t*** The word is: {selected_word} ***\n\n")


