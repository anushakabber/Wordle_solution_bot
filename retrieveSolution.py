import json


def solutionInInfofunc(driver, ):
	url='https://www.nytimes.com/games/wordle/index.html'
	driver.get(url)	
	scriptArray="""return Array.apply(0, new Array(localStorage.length)).map(function (o, i) { return localStorage.getItem(localStorage.key(i)); })""" 
	result = driver.execute_script(scriptArray)
	solution = json.loads(result[0])
	return solution

