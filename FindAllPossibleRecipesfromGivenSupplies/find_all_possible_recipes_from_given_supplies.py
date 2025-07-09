class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        available_ingredients = set(supplies)
        
        recipes_data = []
        for i in range(len(recipes)):
            recipes_data.append((recipes[i], ingredients[i]))
            
        creatable_recipes = []
        
        while True:
            new_recipe_created_in_this_iteration = False
            next_recipes_to_check = []
            
            for recipe_name, required_ingredients in recipes_data:
                can_make_recipe = True
                for ingredient in required_ingredients:
                    if ingredient not in available_ingredients:
                        can_make_recipe = False
                        break
                
                if can_make_recipe:
                    creatable_recipes.append(recipe_name)
                    available_ingredients.add(recipe_name)
                    new_recipe_created_in_this_iteration = True
                else:
                    next_recipes_to_check.append((recipe_name, required_ingredients))
            
            if not new_recipe_created_in_this_iteration:
                break
            
            recipes_data = next_recipes_to_check
            
            if not recipes_data:
                break
                
        return creatable_recipes