# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_word(text, word) : 
    word = word.lower() 
    index = text.find(word)
    if index <= 0 :
        return print("The word was not found in the text")
    else :
        censored_email_fractured = text.split(word)
        censored_email = "------".join(censored_email_fractured)
        return censored_email

def censor_proprietary_terms(term_list, text) : 
    email_to_censor = text.lower()
    for term in term_list : 
        term.lower()
        email_to_censor = email_to_censor.replace(term, "------")
    return email_to_censor

def censor_negative_word(term_list, negative_word_list, text) : 
    email_to_censor = censor_proprietary_terms(term_list, text)
    negative_word_count = 0
    print(email_to_censor)
    print("--------------------------------------")
    for word in negative_word_list :
       word.lower()
       if email_to_censor.find(word) >= 0 : 
          negative_word_count += 1
          if negative_word_count > 2 : 
            email_to_censor = email_to_censor.replace(word, "------")
    return email_to_censor

def censor_everything(term_list, negative_word_list, text) : 
    email_to_censor = text.lower()
    all_terms = term_list + negative_word_list
    print(all_terms)
    print(email_to_censor)
    email_to_censor_lines = email_to_censor.split(".")
    partially_censored_email = []
    for line in email_to_censor_lines : 
        email_to_censor_words = line.split()
        for word in email_to_censor_words :
            censored_next_word = False
            censored_word = False
            sanatized_word = word.strip(",").strip("(").strip(")")
            for term in all_terms : 
                if sanatized_word == term :
                    censored_word = True
                    break
            if censored_word : 
                partially_censored_email[-1] = "-" * len(partially_censored_email[-1])
                partially_censored_email.append("-" * len(word))
                partially_censored_email.append("-" * len(word))
                censored_next_word = True
            else :
                if censored_next_word : 
                   break
                partially_censored_email.append(word)
    return " ".join(partially_censored_email)

#print("What would you like to remove Mr.Cloudy?")
#key_words = input()
#print(censor_word(email_one, key_words))
#print(censor_proprietary_terms(proprietary_terms, email_two))
#print(censor_negative_word(proprietary_terms, negative_words, email_three))
print(censor_everything(proprietary_terms, negative_words, email_three))