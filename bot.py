import discord
import os
import retrieveSolution
import keywords
import retrieveWords
from selenium import webdriver
import json


os.chmod('/app/chromedriver', 755)

client = discord.Client()

print("you're running the discord bot")

@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.content.startswith('$hello'):
        info = message.content
        info = info.replace("$hello ", "")
        
        # help message
        if "help" in info:
             await message.channel.send("To retrieve solution. make sure you have the word 'solution' in your query. \nTo get words with certain set conditions, use 'words' in your query and separate each condition with ';'. For example, $hello give me words starting with 'a'; and ending with 'e' or $hello I'd like words starting with 'b'; and containing 'e' please.")

        # retrieves solution
        if "solution" in info:
            driver = webdriver.Chrome('/app/chromedriver')
            solution = retrieveSolution.solutionInInfofunc(driver)
            await message.channel.send(solution['solution'])
        
        # case where user requires hints and potential solutions are retrieved
        elif "word" in info:
            
            temp_set = keywords.catchKeywords(info)
            indicative_letters, five_letter_words, key_words = temp_set[0],  temp_set[1], temp_set[2]
            potential_solutions = retrieveWords.retrievePotentialWords(indicative_letters, key_words, five_letter_words)
            await message.channel.send(potential_solutions)
            
        elif (("help" not in info) and ("solution" not in info) and ("word" not in info)):
            await message.channel.send("Invalid hello message.")

client.run(os.getenv("token_bot"))
