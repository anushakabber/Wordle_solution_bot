

def retrievePotentialWords(indicative_letters, key_words, five_letter_words):

        main_list = five_letter_words.copy()
        for i in indicative_letters.keys():
            temp = ""
            for j in indicative_letters[i]:
                temp += j
            temp = re.sub('\W+','', temp )
            if key_words[i] == 1:
                for letter in temp:
                    main_list = [x for x in main_list if re.findall("["+re.escape(letter)+"]", x) ]
            if key_words[i] == -1:
                for letter in temp:
                    main_list = [x for x in main_list if (re.findall("[^"+re.escape(letter)+"]"),x) ]
            if key_words[i]== 3:
                main_list = [x for x in main_list if re.findall("\A"+re.escape(temp),x)]
            if key_words[i]== 5:
                main_list = [x for x in main_list if re.findall(re.escape(temp)+"....",x)]
            if key_words[i]== 6:
                main_list = [x for x in main_list if re.findall("."+re.escape(temp)+"...",x)]
            if key_words[i]== 7:
                main_list = [x for x in main_list if re.findall(".."+re.escape(temp)+"..",x)]
            if key_words[i]== 8:
                main_list = [x for x in main_list if re.findall("..."+re.escape(temp)+".",x)]
            if ((key_words[i]== 9) or (key_words[i]== 4)) :
                main_list = [x for x in main_list if re.findall("...."+re.escape(temp),x)]
        if (len(main_list)>1500):
            final = "Here are some words that match the description: \n"+main_list[0]+"\n"+main_list[1]+"\n"+main_list[2]+"..."+"\n There are too many words that match the description, please continue to narrow your search."
        elif (len(main_list)==0):
            final = "No words match that description. Please try again."
        else:
            final = "These are your words:"+"\n"
            for word in main_list:
                final += (word + "\n")
        return final 
