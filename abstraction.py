#learning abstraction
#abstraction means to simplify complex code
# or wrap complex code into a box called
# a function
# first we define a function
def speech():
    I_have_a_dream_speech = "When we allow freedom to ring—when we let it ring from every city and every hamlet, from every state and every city, we will be able to speed up that day when all of God’s children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual, “Free at last, Free at last, Great God a-mighty, We are free at last."

    word_find="freedom"

    if word_find in I_have_a_dream_speech:
        print("found")
    else:
        print("not found")

        question=input("did you find the word?")
        print('your response is :', question)


speech()
speech()