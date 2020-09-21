from pokeapi import *
from flask import *
import json

app = Flask(__name__)
data = dict()



@app.route('/')
def home():
    return render_template('main.html')

@app.route('/pokedex',methods =['POST','GET'])
def pokedex():
    if request.method == 'POST': 
        sno = int(request.form['sno'])
    else :
        sno = 1
    results = pokes
    if(sno <1):
        return "Enter a valid Value"
    if(sno > 13):
        return "Under Progress"
    
    data = {
    "id" : str(results[sno]['id']),
    "name" : str(results[sno]['name']),
    "type1" : str(results[sno]['type1']),
    "type2" : str(results[sno]['type2']),
    "ability1" : str(results[sno]['ability1']),
    "ability2" : str(results[sno]['ability2']),
    "Hiddenability" : str(results[sno]['Hiddenability']),
    "HP" : str(results[sno]['HP']),
    "Attack" : str(results[sno]['Attack']),
    "Defense" : str(results[sno]['Defense']),
    "SpecialAttack" : str(results[sno]['SpecialAttack']),
    "SpecialDefense" : str(results[sno]['SpecialDefense']),
    "Speed" : str(results[sno]['Speed']),
    "TotalStats" : str(results[sno]['TotalStats']),
    "EvolutionMethod" : str(results[sno]['EvolutionMethod']),
    "EvolutionName" : str(results[sno]['EvolutionName'])
    }
    return render_template('pokedex.html', data = data)



if __name__ == '__main__': 
    app.run(debug = True) 


