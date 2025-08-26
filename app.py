import re
from flask import Flask, render_template, request

app = Flask(__name__)

DICTIONARY_MORSE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',   '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',  "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.',  '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

DICTIONARY_REVERSE = {value: key for key, value in DICTIONARY_MORSE.items()}  # All values become keys to invert the dictionary


def is_valid_input(input_data):
    pattern = r'^[A-Za-z0-9 .,?\'!/\(\)&:;=+\-_"$@]+$'
    return bool(re.search(pattern, input_data))

def normalize_morse_input(input_data):
    return input_data.replace('/', ' / ').split()  # Normalize user input for Morse code by converting '/',' / ', or ' /' to ' / '

def is_morse(input_data):
    pattern = r'^[. \-/]+$'
    if not re.search(pattern, input_data):
        return False
    code = normalize_morse_input(input_data)
    if all(morse_units in DICTIONARY_REVERSE for morse_units in code):
        return True
    raise ValueError("Error: Character not found in Morse dictionary:")

def morse_to_text(input_code):
    split_code = normalize_morse_input(input_code)
    converted_text = ''
    for code in split_code:
        converted_text += DICTIONARY_REVERSE[code]
    return converted_text

def text_to_morse(text):
    text = text.upper()
    morse_result = ''
    for char in text:
        morse_result += DICTIONARY_MORSE[char] + ' '
    return morse_result


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        if is_valid_input(user_input):
            try:
                if is_morse(user_input):
                    result = morse_to_text(user_input)
                else:
                    result = text_to_morse(user_input)
            except (ValueError, KeyError):
                error = 'Error: Character not found in Morse dictionary:'
        else:
            error = "Error: Invalid input. Please enter valid text or Morse code (no special characters like ñ, ü, etc)."
    return render_template('index.html', result=result, error=error)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)