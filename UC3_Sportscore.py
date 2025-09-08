#SportScore
def get_average_score(data):

    if isinstance(data, dict):
        runs = data["Runs"]
    elif isinstance(data, list):
        runs = [player[2] for player in data]  # Assuming runs is the 3rd element
    else:
        runs = data

    average = sum(runs) / len(runs)
    return round(average, 1)


def count_players_above_age(data, age=30):

    if isinstance(data, dict):
        ages = data["Age"]
    elif isinstance(data, list):
        ages = [player[1] for player in data]  # Assuming age is the 2nd element
    else:
        ages = data

    count = sum(1 for player_age in ages if player_age > age)
    return count


# Main code
if __name__ == "__main__":
    data = {
        "Player": ["Kohli", "Rohit", "Gill", "Dhoni", "Hardik"],
        "Age": [35, 36, 24, 42, 30],
        "Runs": [1200, 980, 750, 1600, 890]
    }

    print("Cricket Score System")
    for i, player in enumerate(data["Player"]):
        print(f"{player}: Age {data['Age'][i]}, Runs {data['Runs'][i]}")
    print()

    # Calculate Avg score
    avg_score = get_average_score(data)
    print(f"Average runs scored by all players: {avg_score}")

    # Countabove age 30
    players_above_30 = count_players_above_age(data, 30)
    print(f"Number of players above age 30: {players_above_30}")

    # Test with different age
    players_above_35 = count_players_above_age(data, 35)
    print(f"Number of players above age 35: {players_above_35}")


def get_average_score_df(df):
    return round(df["Runs"].mean(), 1)

def count_players_above_age_df(df, age=30):
    filtered = df[df["Age"] > age]
    return len([x for x in filtered.data if x])