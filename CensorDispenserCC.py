# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

def censor_word(input_text, censor) :
    censored_item = "" 
    for x in range(0, len(censor)) : 
        if censor[x] == " ": 
            censored_item = censored_item + " "
        else : 
            censored_item = censored_item + "-"
    return input_text.replace(censor, censored_item)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_proprietary_terms(input_text, censored_list) : 
    for word in censored_list : 
        censored_word = ""
        for x in range(0,len(word)) : 
            if word[x] == " " : 
                censored_word = censored_word + " "
            else : 
                censored_word = censored_word + "-"
        input_text = input_text. replace(word, censored_word)
    return input_text

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_negative_word(input_text, censored_list, negative_words) : 
    input_text_words = [] 
    # Cleans up the words and puts it into a new array
    for x in input_text.split(" ") : 
        x1 = x.split("\n")
        for word in x1:
            input_text_words.append(word)
    #  Censor : goes through the new array word for word
    for i in range(0, len(input_text_words)) : 
        # Checks if the word is in the censor list and replaces it with a string of equal length if it exists
        if (input_text_words[i] in censored_list) == True: 
            word_clean = input_text_words[i]
   
            censored_word = ""
            for x in range(0, len(word_clean)) : 
                censored_word = censored_word + "-"
            input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
        # initiates a variable to count the amount of times a word appears" 
        count = 0
        for i in range(0, len(input_text_words)) : 
            # checks if the word is in the negative list 
            if (input_text_words[i] in negative_words) == True : 
                count += 1 
                # Only censors if the word appears more than once in the text
                if count > 2 : 
                    word_clean = input_text_words[i]
                    #strips any punctuation off of the word
                    for x in punctuation : 
                        word_clean = word_clean.strip(x)
                    censored_word = ""
                    for x in range(0, len(word_clean)) : 
                        censored_word = censored_word + "-"
                    input_text_words[i] = input_text_words[i].replace(word_clean,censored_word)
    return " ".join(input_text_words)
    
def censor_negative_word_two(input_text, censored_list, negative_words)  :  
   email_to_censor = censor_proprietary_terms(input_text, censored_list)
   negative_word_count = 0
   for word in negative_words :
      word.lower()
      if email_to_censor.find(word) >= 0 : 
         negative_word_count += 1
         if negative_word_count > 2 : 
           email_to_censor = email_to_censor.replace(word, "------")
   return email_to_censor

def censor_everything(input_text, censored_list) : 
    input_text_words = [] 
    for x in input_text.split(" ") : 
        x1 = x.split("\n") 
        for word in x1: 
            input_text_words.append(word)
    for i in range(0, len(input_text_words)) : 
        checked_word = input_text_words[i].lower() 
        for x in punctuation : 
            checked_word = checked_word.strip(x) 
        if checked_word in censored_list : 

            #Censoring the Targeted word
            word_clean = input_text_words[i]
            censored_word = ""
            for x in punctuation : 
                word_clean = word_clean.strip(x)
            for x in range(0, len(word_clean)) : 
                censored_word = censored_word + "-"
            input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)

            # Censoring the word before
            word_before = input_text_words[i-1]
            for x in punctuation : 
                word_before = word_before.strip(x)
            censored_word_before = ""
            for x in range(0, len(word_before)) : 
                censored_word_before = censored_word_before + "-"
            input_text_words[i-1] = input_text_words[i-1].replace(word_before, censored_word_before)

            # Censoring the word After
            word_before = input_text_words[i+1]
            for x in punctuation : 
                word_before = word_before.strip(x)
            censored_word_before = ""
            for x in range(0, len(word_before)) : 
                censored_word_before = censored_word_before + "-"
            input_text_words[i+1] = input_text_words[i+1].replace(word_before, censored_word_before)
    return " ".join(input_text_words)

#print("What would you like to remove Mr.Cloudy?")
##key_words = input()
#print(censor_word(email_one,"learning algorithm"))
#print(censor_proprietary_terms(proprietary_terms, email_two))
#print(censor_negative_word_two(email_three, proprietary_terms, negative_words))
print(censor_everything(email_four, (negative_words + proprietary_terms)))