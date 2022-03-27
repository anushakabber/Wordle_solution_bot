import discord
import os
from selenium import webdriver
import json

client = discord.Client()

print("you're running the discord bot")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    
    if message.content.startswith('$hello'):
        info = message.content
        info = info.replace("$hello ", "")
        if "help" in info:
             await message.channel.send("To retrieve solution. make sure you have the word 'solution' in your query. \nTo get words with certain set conditions, use 'words' in your query and separate each condition with ';'. For example, $hello give me words starting with 'a'; and ending with 'e' or $hello I'd like words starting with 'b'; and containing 'e' please.")

        if "solution" in info:
            driver = webdriver.Chrome('/Users/anushakabber/Downloads/chromedriver')
            url='https://www.nytimes.com/games/wordle/index.html'
            driver.get(url)	
            scriptArray="""return Array.apply(0, new Array(localStorage.length)).map(function (o, i) { return localStorage.getItem(localStorage.key(i)); }
                            )""" 
            result = driver.execute_script(scriptArray)
            solution = json.loads(result[0])
            await message.channel.send(solution['solution'])
        elif "words" in info:
            import nltk
            from nltk.corpus import words
            import re
            nltk.download('punkt')
            nltk.download('words')

            sentence = info
            word_list = words.words()
            five_letter_words = [i for i in word_list if len(i)==5]
            key_words = {"containing":1, "not containing":-1, "having":1, "starting with":3, "beginning with":3, "ending with":4, "first":5, "second":6, "third":7, "fourth":8, "fifth":9, "not having":-1, "not containing":-1, "not starting":-3, "not ending":-4, "not beginning":-3}

            main = {}
            for i in key_words.keys():
                value = []
                if i in sentence:
                    k = sentence.index(i)
                    if key_words[i] in [1, -1, 3, 4, -4, -3]:
                        temp = ""
                        for m in range(k+len(i),len(sentence)):
                            if sentence[m]== ';':
                                break
                            temp += sentence[m]
                        temp = temp.split(" ")
                        for h in temp:
                            if '\'' in h:
                                value.append(h)
                    else:
                        hold = 0
                        for m in range(0, k):
                            if sentence[m] == ';':
                                hold = m
                        temp = sentence[hold+1:k]
                        temp = temp.split(" ")
                        for h in temp:
                            if '\'' in h:
                                value.append(h)
                    main[i] = value

            main_list = five_letter_words.copy()
            for i in main.keys():
                temp = ""
                for j in main[i]:
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
            await message.channel.send(final)


client.run(os.getenv("token_bot"))
