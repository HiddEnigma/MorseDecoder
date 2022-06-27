MORSE_CODE_DICTIONARY = {
    "a": ".- ",
    "b": "-... ",
    "c": "-.-. ",
    "d": "-.. ",
    "e": ". ",
    "f": "..-. ",
    "g": "--. ",
    "h": ".... ",
    "i": ".. ",
    "j": ".--- ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": "-- ",
    "n": "-. ",
    "o": "--- ",
    "p": ".--. ",
    "q": "--.- ",
    "r": ".-. ",
    "s": "... ",
    "t": "- ",
    "u": "..- ",
    "v": "...- ",
    "w": ".-- ",
    "x": "-..- ",
    "y": "-.-- ",
    "z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    ".": ".-.-.- ",
    ",": "--..-- ",
    "?": "..--.. ",
    "!": "..--. ",
    ":": "---... ",
    '"': ".-..-. ",
    "'": ".----. ",
    "=": "-...- ",
    " ": "/ "
}


def translate(text):
    for character in text:
        character = character.lower()

        translated.append(MORSE_CODE_DICTIONARY[character])


translated = []
print("This is a Text-To-Morse Code translator. Please insert the string you want to translate.")
string = input("Text: ")

translate(string)

print(f"Morse Code: {''.join(translated)}")


