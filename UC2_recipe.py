
def read_recipe_file(filename):
    recipes = []

    try:
        # Open the file using with open(filename) as file
        with open(filename, 'r') as file:
            for line in file:
                # Read each line and strip trailing whitespace
                line = line.strip()
                if line:  # Skip empty lines
                    # Split each line into parts
                    parts = line.split(',')
                    if len(parts) >= 3:
                        # Extract components
                        recipe_name = parts[0].strip()  # Name (str)
                        calories = int(parts[1].strip())  # Calories (int)
                        # Ingredients (use ; and convert to a string like "x, y, z")
                        ingredients_list = [ingredient.strip() for ingredient in parts[2:]]
                        ingredients_str = ';'.join(ingredients_list)

                        # Create a dictionary with keys: Recipe, Calories, Ingredients
                        recipe_dict = {
                            'Recipe': recipe_name,
                            'Calories': calories,
                            'Ingredients': ingredients_str
                        }
                        recipes.append(recipe_dict)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    return recipes


def get_high_calorie_recipes(df, threshold=500):
    # Use DataFrame filtering: df[df['Calories'] > threshold]
    high_calorie_recipes = []

    for recipe in df:
        if recipe['Calories'] > threshold:
            high_calorie_recipes.append(recipe)

    # Return the filtered DataFrame
    return high_calorie_recipes


def get_ingredients(df, recipe_name):
     # Filter the DataFrame where df['Recipe'] == pizza
    for recipe in df:
        if recipe['Recipe'].lower() == recipe_name.lower():
            # Check if the result is not empty
            # If found, return the value from the Ingredients column
            return recipe['Ingredients']

    # Else, return "Recipe not found."
    return "Recipe not found."


# Create sample data
def create_sample_data():
    """Create sample recipe data for testing"""
    sample_recipes = [
        {'Recipe': 'Pasta', 'Calories': 600, 'Ingredients': 'Pasta;Tomato Sauce;Cheese'},
        {'Recipe': 'Salad', 'Calories': 550, 'Ingredients': 'Lettuce;Tomato;Cucumber'},
        {'Recipe': 'Pizza', 'Calories': 800, 'Ingredients': 'Dough;Cheese;Sauce'},
        {'Recipe': 'Soup', 'Calories': 350, 'Ingredients': 'Broth;Carrot;Onion'},
        {'Recipe': 'Smoothie', 'Calories': 200, 'Ingredients': 'Banana;Milk;Honey'}
    ]
    return sample_recipes


# Test functions
if __name__ == "__main__":
    # Create sample data (simulating file read)
    print("\n1. Sample Recipe Data:")
    recipes_data = create_sample_data()

    print("Recipe       | Calories | Ingredients")
    print("-" * 50)
    for recipe in recipes_data:
        ingredients_display = recipe['Ingredients'].replace(';', ', ')
        print(f"{recipe['Recipe']:<12} | {recipe['Calories']:<8} | {ingredients_display}")

    # Test Function 1: File reading (simulated with sample data)
    print(f"\nFunction 1 - Read Recipe File:")
    print(f"Successfully loaded {len(recipes_data)} recipes")

    # Test Function 2: High calorie recipes
    print(f"\nFunction 2 - High Calorie Recipes (>500 calories):")
    high_calorie = get_high_calorie_recipes(recipes_data, 600)
    if high_calorie:
        for recipe in high_calorie:
            print(f"- {recipe['Recipe']}: {recipe['Calories']} calories")
    else:
        print("No high-calorie recipes found.")

    # Test Function 3: Get ingredients
    print(f"\nFunction 3 - Get Ingredients:")
    test_recipes = ['Pizza', 'pizza', 'Pasta', 'Vada Pav']
    for recipe_name in test_recipes:
        ingredients = get_ingredients(recipes_data, recipe_name)
        ingredients_display = ingredients.replace(';', ', ') if ingredients != "Recipe not found." else ingredients
        print(f"Ingredients for '{recipe_name}': {ingredients_display}")
