import itertools

def leetspeak(word):
    return word.replace('a', '@').replace('e', '3').replace('s', '$').replace('o', '0')

def generate_wordlist(keywords):
    variations = set()
    for word in keywords:
        word = word.lower()
        for year in range(1990, 2030):
            variations.update([
                word,
                word + str(year),
                leetspeak(word),
                leetspeak(word) + str(year),
                word.capitalize(),
            ])
    return list(variations)

def export_wordlist(words, filename='output/custom_wordlist.txt'):
    with open(filename, 'w') as f:
        for word in words:
            f.write(f"{word}\n")