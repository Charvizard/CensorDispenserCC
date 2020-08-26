# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_word(text, word) : 
    word = word.lower() 
    index = text.find(word)
    if index <= 0 :
        return print("The word was not found in the text")
    else :
        censored_email_fractured = text.split(word)
        censored_email = "------".join(censored_email_fractured)
        return censored_email

print("What would you like to remove Mr.Cloudy?")
key_words = input()
print(censor_word(email_one, key_words))