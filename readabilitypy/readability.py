sentence = input("Text: ")
letters = 0
word = 0
sentences = 0
for letter in sentence:
    if letter == " ":
        word = word + 1
    elif letter == "." or letter == "!" or letter == "?":
        sentences = sentences + 1
    else:
        letters = letters + 1
        if letter == "." or letter =="!" or letter == "?" or letter == "," or letter == " ":
            letters = letters - 1

print("letter: "+ str(letters))
print("words: "+ str(word))
print("sentences: "+ str(sentences))
L = (letters / (word + 1)) * 100
S = (sentences / (word + 1)) * 100
index = (0.0588 * L) - (0.296 * S) - 15.8
grade = round(index)

if grade < 1:
    print("Before Grade 1");
elif grade > 16:
    print("Grade 16+")
else:
    print("Grade " + str(grade))