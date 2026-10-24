
print("=" * 5, "TEXT ANALYZER", "=" * 5)

text = input("Enter a paragraph: ")

# Remove basic punctuation and make letters lowercase
clean_text = text.lower()

for mark in ".,!?;:":
    clean_text = clean_text.replace(mark, "")

words = clean_text.split()


def count_words():
    return len(words)


def count_characters():
    count = 0

    for char in text:
        if char != " ":
            count += 1

    return count


def count_vowels_consonants():
    vowels = 0
    consonants = 0

    for char in clean_text:
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


def longest_word():
    if len(words) == 0:
        return "No words found"

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def count_appearances():
    appearances = {}

    for word in words:
        if word in appearances:
            appearances[word] += 1
        else:
            appearances[word] = 1

    return appearances


def count_repeated_words():
    appearances = count_appearances()
    repeated = []

    for word in appearances:
        if appearances[word] > 1:
            repeated.append(word)

    return repeated


def five_most_frequent():
    appearances = count_appearances()
    frequent = []

    for word in appearances:
        frequent.append([word, appearances[word]])

    # Sort from highest frequency to lowest
    for i in range(len(frequent)):
        for j in range(i + 1, len(frequent)):
            if frequent[j][1] > frequent[i][1]:
                frequent[i], frequent[j] = frequent[j], frequent[i]

    return frequent[:5]


# Display results
vowels, consonants = count_vowels_consonants()

print("\n===== TEXT STATISTICS =====")
print("Words:", count_words())
print("Characters excluding spaces:", count_characters())
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Longest word:", longest_word())

print("\nWord appearances:")
print(count_appearances())

print("\nRepeated words:")
print(count_repeated_words())

print("\nFive most frequent words:")
for item in five_most_frequent():
    print(item[0], ":", item[1])
