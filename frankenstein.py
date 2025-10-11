def min_orbs_to_brew(potion, recipes, memo):
    if potion in memo:
        return memo[potion]
    
    if potion not in recipes:
        # It's a base item, no orbs needed
        memo[potion] = 0
        return 0

    min_orbs = float('inf')
    for ingredients in recipes[potion]:
        cost = len(ingredients) - 1  # Orbs for combining
        for ing in ingredients:
            cost += min_orbs_to_brew(ing, recipes, memo)
        min_orbs = min(min_orbs, cost)
    
    memo[potion] = min_orbs
    return min_orbs

# Input parsing
n = int(input())
recipes = {}
for _ in range(n):
    line = input()
    potion, ing_str = line.split('=')
    ingredients = ing_str.split('+')
    recipes.setdefault(potion, []).append(ingredients)

target_potion = input()
memo = {}
print(min_orbs_to_brew(target_potion, recipes, memo))
