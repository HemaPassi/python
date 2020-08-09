original = input('Enter sentence to play : ').strip().lower()
words = original.split()

new_words = []
vowels = 'aeiou'

for word in words:
    if word[0] in vowels:
        new_word = word+'yay'
        new_words.append(new_word)
        print(new_words)
    else:
        vowel_pos =0;
        for letter in word:
            if letter not in vowels:
                vowel_pos = vowel_pos+1
            else:
                break
        const = word[:vowel_pos]
        the_Rest = word[vowel_pos:]
        new_word = the_Rest+const +'ay'
        new_words.append(new_word)
        output = " ".join(new_words)
        print(output )

