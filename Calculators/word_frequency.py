text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

ignored_words = ["the", "they", "their", "them", "it", "its", "and", "then", "a", "an", "of", "to"]
punctuation = "`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/?\n\t"

def format(punctuation, text):
    text = text.lower()
    for char in punctuation:
        text = text.replace(char, '')
    
    return text

def repetitionFinder(text):
    found = []
    repetitions = []

    text = format(punctuation, text)
    wordList = text.split(" ")

    for word in wordList:
        if word in ignored_words or word in found:
            continue

        count = wordList.count(word)
        found.append(word)

        if count > 1:
            repetitions.append((count, word))
            print(f"{word}: {count}")
    
    return repetitions


repetitionFinder(text)
