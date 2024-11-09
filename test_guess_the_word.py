# Jake Gapusan
# CIS 256 Fall 2024
# EX 4

from guess_the_word import choose_word, show_word

def test_choose_word():
    word = choose_word()
    assert word in ["gaming", "coding", "testing", "homework", "habits"]

def test_show_word():
    word = "coding"
    guesses = {"c", "o", "d"}
    assert show_word(word, guesses) == "c o d _ _ _"

    guesses = {"c", "o", "d", "i", "n", "g"}
    assert show_word(word, guesses) == "c o d i n g"