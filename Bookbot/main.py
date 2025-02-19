import sys

def count_words(text: str):
    return len(text.split())

def count_characters(text: str):
    lowercase_text = text.lower()
    characters = list(lowercase_text)
    result = {}

    for char_item in characters:
        if char_item in result:
            result[char_item] += 1
        else:
            result[char_item] = 1
    return result

def report_characters(char_count):
    print("--- BEGIN REPORT ---")
    for item in char_count:
        if item in (' ', '.', '#'):
            continue
        print(f'The \'{item}\' character was found {char_count[item]} times')
    print("--- END REPORT ---")

def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        # print(contents, end="\n\n")

        word_count = count_words(contents)
        print(f'This text contains {word_count} words', end="\n\n")

        char_count = count_characters(contents)
        # print(f'This text has the following character frequency:\n {char_count}')
        report_characters(char_count)

if __name__ == '__main__':
    sys.exit(main())