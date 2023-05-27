receitasConhecidas = {

    'brownie': {
        'nome': 'brownie',
        'ingredientes': ['trigo', 'chocolate', 'margarina', 'acucar'], 
        'modoDePreparo': 'só mexer tudo e depois assar'
    },

    'doce de leite': {
    'nome': 'doce de leite',
    'ingredientes': ['leite', 'agua', 'margarina', 'acucar'], 
    'modoDePreparo': 'mexa tudo'
    }

}


class Recipes:
    
    def __init__(self, receitasConhecidas : dict) -> None:
        self.receitasConhecidas = receitasConhecidas
        self.possiveisReceitas = []

    def list_recipes(self, recipe:str=None) -> None:
        if recipe:
            if recipe.lower() in self.receitasConhecidas:
                return self.receitasConhecidas[recipe]
            else:
                return "Recipe still unavailable"
        return self.receitasConhecidas


    def find_recipes(self, ingredient):     
        if type(ingredient) == str :
            print("match_one")
            return self.__find_recipes_match_one(ingredient)
        elif type(ingredient) == list:
            print("match_all")
            return self.__find_recipes_match_all(ingredient)
        else:
            pass

    def __find_recipes_match_one(self, ingredient: str) -> list:
        for receita in self.receitasConhecidas.values():
            if ingredient in receita.get('ingredientes'):
                self.possiveisReceitas.append(receita['nome'])
        return self.possiveisReceitas
    
    def __find_recipes_match_all(self, ingredients: str) -> list:
        for recipe in self.receitasConhecidas.values():
            if set(ingredients).issubset(recipe.get("ingredientes")):
                self.possiveisReceitas.append(recipe["nome"])
        return self.possiveisReceitas
        


recipe = Recipes(receitasConhecidas)
#print(recipe.find_recipes(["acucar"]))
#print(type(["acucar"]))

#recipe.find_recipes("acucar")

print(recipe.list_recipes("doce de leite"))