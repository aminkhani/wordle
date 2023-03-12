"""Run The Wordle Game.

:DATA_FILE_PATH: Set your dataset as a text file
:word_len: Number of letters, defualt = 5
:limit: Number of words, defualt = 100000, don't change
"""

from wordle import Wordle

DATA_FILE_PATH = 'src/data/data.txt'
word_len = 5
limit = 10000

print(f"\n\t*** Welcom To Wordle Game ***\n\t1. Set number of letters\n\t2. Set number of words\n\n\tNotice:\n\t  * Green Color: The letter and the place is ok\n\t  * Red Color: Make a mistake(ERROR)\n\t  * Yellow Color: The letter is ok but the place in not ok\n\t  * No Color: The letter and place not ok\n\t  * You car try: 6 times\n\n")


word_len = int(input("\tEnter a number for number of letters (minimum: 2): "))

wordle = Wordle(DATA_FILE_PATH, word_len)
wordle.run()
