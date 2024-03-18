df = pd.read_csv("Tokyo 2021 dataset v3.csv")
#df

df2 = pd.read_csv("athlete_events.csv")
#df2

df3 = pd.read_csv("noc_regions.csv")
#df3

df2 = df2.drop('Medal', axis=1) # meer dan 80% was missende waarden, dus ik heb het weggehaald
mean_age = df2['Age'].mean()  # Bereken het gemiddelde
df2['Age'].fillna(mean_age, inplace=True)  # Vul ontbrekende waarden in met het gemiddelde
mean_height = df2['Height'].mean()  # Bereken het gemiddelde
df2['Height'].fillna(mean_height, inplace=True)  # Vul ontbrekende waarden in met het gemiddelde
mean_weight = df2['Weight'].mean()  # Bereken het gemiddelde
df2['Weight'].fillna(mean_weight, inplace=True)  # Vul ontbrekende waarden in met het gemiddelde

df3 = df3.drop('notes', axis=1)

merged_data = pd.merge(df, df2, left_on='NOCCode', right_on='NOC')
merged_data2 = pd.merge(merged_data, df3, on='NOC')
merged_data2
#--------------------------------------------------------------------------------------------
st.title('Totaal aantal medailles per land')

fig = px.choropleth(df,
                    locations='Team/NOC',
                    locationmode='country names',
                    color='Total',
                    color_continuous_scale='rdbu'
                   )

# Toon de kaart in de Streamlit-app
st.plotly_chart(fig)
#--------------------------------------------------------------------------------------------
import streamlit as st
import plotly.express as px

def Kaart(df):
    st.title('Totaal aantal medailles per land')

    fig = px.choropleth(df,
                    locations='Team/NOC',  # Zorg ervoor dat deze kolom bestaat in je DataFrame
                    locationmode='country names',
                    color='Total',  # Zorg ervoor dat deze kolom bestaat in je DataFrame
                    color_continuous_scale='rdbu'  # Kies een geschikt kleurenschema
                   )

    st.plotly_chart(fig)
    return fig

# Roep de functie aan met je DataFrame als argument
Kaart(df)
#--------------------------------------------------------------------------------------------
# Voorbeeldgegevens
teams = df['Team/NOC']
gold_medals = df['Gold Medal']
silver_medals = df['Silver Medal']
bronze_medals = df['Bronze Medal']
continents = df['Continent']

# Creëer een DataFrame met de gegevens
data = pd.DataFrame({
    'Team': teams,
    'Gold': gold_medals,
    'Silver': silver_medals,
    'Bronze': bronze_medals,
    'Continent': continents
})

st.title('Medailleverdeling per Land en Continent')

# Functie om de stacked bar chart weer te geven voor een specifiek continent
def plot_stacked_bar_chart(selected_continent):
    filtered_data = data[data['Continent'] == selected_continent]
    
    fig, ax = plt.subplots()
    ax.bar(filtered_data['Team'], filtered_data['Gold'], label='Gold')
    ax.bar(filtered_data['Team'], filtered_data['Silver'], bottom=filtered_data['Gold'], label='Silver')
    ax.bar(filtered_data['Team'], filtered_data['Bronze'], bottom=filtered_data['Gold'] + filtered_data['Silver'], label='Bronze')

    ax.set_ylabel('Aantal Medailles')
    ax.set_title(f'Medailleverdeling per Land in {selected_continent}')
    ax.set_xticks(filtered_data['Team'])
    ax.set_xticklabels(filtered_data['Team'], rotation=90)
    ax.legend()

    st.pyplot(fig)

# Maak een interactieve dropdown om een continent te selecteren
selected_continent = st.selectbox('Selecteer een Continent', data['Continent'].unique())
plot_stacked_bar_chart(selected_continent)

#--------------------------------------------------------------------------------------------
def MedailleVerdelingPerLandEnContinent(df):
    # Voorbeeldgegevens
    teams = df['Team/NOC']
    gold_medals = df['Gold Medal']
    silver_medals = df['Silver Medal']
    bronze_medals = df['Bronze Medal']
    continents = df['Continent']

    # Creëer een DataFrame met de gegevens
    data = pd.DataFrame({
        'Team': teams,
        'Gold': gold_medals,
        'Silver': silver_medals,
        'Bronze': bronze_medals,
        'Continent': continents
    })

    st.title('Medailleverdeling per Land en Continent')

    # Functie om de stacked bar chart weer te geven voor een specifiek continent
    def plot_stacked_bar_chart(selected_continent):
        filtered_data = data[data['Continent'] == selected_continent]
    
        fig, ax = plt.subplots()
        ax.bar(filtered_data['Team'], filtered_data['Gold'], label='Gold')
        ax.bar(filtered_data['Team'], filtered_data['Silver'], bottom=filtered_data['Gold'], label='Silver')
        ax.bar(filtered_data['Team'], filtered_data['Bronze'], bottom=filtered_data['Gold'] + filtered_data['Silver'], label='Bronze')

        ax.set_ylabel('Aantal Medailles')
        ax.set_title(f'Medailleverdeling per Land in {selected_continent}')
        ax.set_xticks(filtered_data['Team'])
        ax.set_xticklabels(filtered_data['Team'], rotation=90)
        ax.legend()

        st.pyplot(fig)

    # Maak een interactieve dropdown om een continent te selecteren
    selected_continent = st.selectbox('Selecteer een Continent', data['Continent'].unique(), key='continent_selectbox')
    plot_stacked_bar_chart(selected_continent)

# Roep de functie aan met je DataFrame als argument
MedailleVerdelingPerLandEnContinent(df)
#--------------------------------------------------------------------------------------------

import streamlit as st
import plotly.express as px

# Veronderstel dat 'merged_data2' je DataFrame is

st.title('Leeftijdsverdeling per sport over de jaren')
st.write('Selecteer een jaar met behulp van de slider.')

# Sorteer de unieke jaren in oplopende volgorde
sorted_years = sorted(merged_data2['Year'].unique())

# Maak een interactieve slider om een jaar te selecteren
selected_year = st.slider('Selecteer een jaar', min_value=min(sorted_years), max_value=max(sorted_years), value=min(sorted_years))

# Filter de data voor het geselecteerde jaar
filtered_data = merged_data2[merged_data2['Year'] == selected_year]

# Maak de boxplot
fig = px.box(filtered_data, x='Sport', y='Age', labels={'Sport': 'Sport', 'Age': 'Leeftijd'})

# Pas de plot aan
fig.update_layout(xaxis_title='Sport', yaxis_title='Leeftijd')

# Toon de plot in Streamlit
st.plotly_chart(fig)
#--------------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px

def boxmetslider(merged_data2):
    
    st.title('Leeftijdsverdeling per sport over de jaren')
    st.write('Selecteer een jaar met behulp van de slider.')

    # Sorteer de unieke jaren in oplopende volgorde
    sorted_years = sorted(merged_data2['Year'].unique())

    # Maak een interactieve slider om een jaar te selecteren
    selected_year = st.slider('Selecteer een jaar', min_value=min(sorted_years), max_value=max(sorted_years), value=min(sorted_years), key='year_slider')

    # Filter de data voor het geselecteerde jaar
    filtered_data = merged_data2[merged_data2['Year'] == selected_year]

    # Maak de boxplot
    fig = px.box(filtered_data, x='Sport', y='Age', labels={'Sport': 'Sport', 'Age': 'Leeftijd'})

    # Pas de plot aan
    fig.update_layout(xaxis_title='Sport', yaxis_title='Leeftijd')

    # Toon de plot in Streamlit
    st.plotly_chart(fig)

boxmetslider(merged_data2)
