import pandas as pd
import matplotlib.pyplot as plt


def supported_platforms_pie_chart(data):
    platform_support = {
        "Windows": data["Windows"].fillna(0).astype(int).sum(),
        "Linux": data["Linux"].fillna(0).astype(int).sum(),
        "Mac": data["Mac"].fillna(0).astype(int).sum()
    }

    labels = platform_support.keys()
    sizes = platform_support.values()

    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title("Distribution of games supported in each platform")
    plt.show()


data = pd.read_csv("games.zip")

print(data)

data.drop(
    ["About the game", "Full audio languages", "Header image", "Website", "Support url", "Support email", "Metacritic url", ],
    inplace=True, axis=1)

print(data)

supported_platforms_pie_chart(data)








