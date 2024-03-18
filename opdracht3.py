import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Laad de dataset
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Bekijk de eerste paar rijen van de dataset
print(train.head())

# Bekijk statistieken van de dataset
print(train.describe())

train.columns

# Visualiseer de verdeling van de doelvariabele (SalePrice)
sns.histplot(train['SalePrice'], kde=True)
plt.title('Verdeling van SalePrice')
plt.show()

# Correlatie matrix om relaties tussen variabelen te bekijken
correlation_matrix = train.corr()
correlation_matrix

# Selecteer variabelen met sterke correlatie met SalePrice
important_variables = correlation_matrix['SalePrice'][abs(correlation_matrix['SalePrice']) > 0.5].index
print(important_variables)

# Veronderstel dat je de dataset al hebt ingeladen en 'GrLivArea' en 'SalePrice' kolommen hebt
# bijvoorbeeld: dataset = pd.read_csv('train.csv')

# Kies de X-variabele
X = train['GrLivArea'].values.reshape(-1, 1)

# Kies de afhankelijke variabele (target)
y = train['SalePrice'].values

# Split de dataset in trainings- en testsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Maak een lineair regressiemodel
model = LinearRegression()
model.fit(X_train, y_train)

# Maak voorspellingen op basis van het testset
y_pred = model.predict(X_test)

# Plot de resultaten
plt.scatter(X_test, y_test, color='black', label='Werkelijke waarden')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Voorspellingen')
plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
plt.legend()
plt.show()

# Bereken de Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
