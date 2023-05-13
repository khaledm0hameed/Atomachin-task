color_codes = {
    'red': '\033[91m',
    'green': '\033[92m',
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'reset': '\033[0m'
}

def color_text(text, color):
    color_code = color_codes.get(color.lower())
    if color_code:
        return f"{color_code}{text}{color_codes['reset']}"
    else:
        return text
    



print(color_text("Hello, world!", "blue"))