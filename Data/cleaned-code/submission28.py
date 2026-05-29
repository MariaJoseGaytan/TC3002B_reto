import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

                         
def create_population_data(years):
    years_array = np.arange(2000, 2000 + years)
    population_data = 300000000 + np.cumsum(np.random.normal(1000000, 500000, years))
    return pd.DataFrame({'Year': years_array, 'Population': population_data})

                          
def calculate_moving_avg(dataframe, window_size):
    return dataframe['Population'].rolling(window=window_size).mean()

                   
def plot_population_and_avg(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Year'], data['Population'], label='Population')
    plt.plot(data['Year'], calculate_moving_avg(data, 5), label='5-Year Moving Avg', linestyle='--')
    plt.title('Population Growth with Moving Average')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.show()

                
if __name__ == "__main__":
    population_df = create_population_data(20)
    plot_population_and_avg(population_df)
