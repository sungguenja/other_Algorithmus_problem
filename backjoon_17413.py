word = list(input())
i=0
reverse_word = []
new_word = []
while i<len(word):
    if word[i] == '<':
        while word[i] != '>':
            new_word.append(word[i])
            i+=1
        new_word.append(word[i])
        reverse_word.extend(new_word)
        new_word.clear()
        i+=1
    else:
        while word[i] != ' ':
            new_word.append(word[i])
            i+=1
            if i == len(word):
                new_word.reverse()
                reverse_word.extend(new_word)
                new_word.clear()
                break
            if word[i] == '<':
                new_word.reverse()
                reverse_word.extend(new_word)
                new_word.clear()
                i-=1
                break
        new_word.reverse()
        reverse_word.extend(new_word)
        if i+1 > len(word) or word[i+1] != '<':
            reverse_word.append(' ')
        new_word.clear()
        i+=1
print(''.join(reverse_word))