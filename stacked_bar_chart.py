import pandas as pd
import matplotlib.pyplot as plt

def MedailleVerdelingPerLandEnContinent(df):
    teams = df['Team/NOC']
    gold_medals = df['Gold Medal']
    silver_medals = df['Silver Medal']
    bronze_medals = df['Bronze Medal']
    continents = df['Continent']

    data = pd.DataFrame({
        'Team': teams,
        'Gold': gold_medals,
        'Silver': silver_medals,
        'Bronze': bronze_medals,
        'Continent': continents
    })

    fig, ax = plt.subplots()

    def plot_stacked_bar_chart(selected_continent):
        filtered_data = data[data['Continent'] == selected_continent]
        ax.bar(filtered_data['Team'], filtered_data['Gold'], label='Gold')
        ax.bar(filtered_data['Team'], filtered_data['Silver'], bottom=filtered_data['Gold'], label='Silver')
        ax.bar(filtered_data['Team'], filtered_data['Bronze'], bottom=filtered_data['Gold'] + filtered_data['Silver'], label='Bronze')

        ax.set_ylabel('Aantal Medailles')
        ax.set_title(f'Medailleverdeling per Land in {selected_continent}')
        ax.set_xticks(filtered_data['Team'])
        ax.set_xticklabels(filtered_data['Team'], rotation=90)
        ax.legend()

    selected_continent = 'Europe'  # Hier kun je het gewenste continent specificeren
    plot_stacked_bar_chart(selected_continent)

    plt.show()

# Roep de functie aan met je DataFrame als argument
df = pd.read_csv('Tokyo 2021 dataset v3.csv')
MedailleVerdelingPerLandEnContinent(df)
