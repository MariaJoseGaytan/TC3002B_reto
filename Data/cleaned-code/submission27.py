import pandas as pd
import matplotlib.pyplot as plt


                                          
def read_csv_data(filename):
    data = pd.read_csv(filename)
    return data


                                       
def compute_growth(dataframe):
    dataframe['GrowthRate'] = dataframe['Population'].pct_change() * 100
    return dataframe


                          
def create_plots(dataframe):
    plt.figure(figsize=(10, 6))

                                  
    plt.subplot(2, 1, 1)
    plt.plot(dataframe['Year'], dataframe['Population'], marker='o', linestyle='-')
    plt.title('Yearly Population')
    plt.xlabel('Year')
    plt.ylabel('Population')

                              
    plt.subplot(2, 1, 2)
    plt.plot(dataframe['Year'], dataframe['GrowthRate'], marker='o', linestyle='-', color='orange')
    plt.title('Yearly Population Growth Rate')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')

    plt.tight_layout()
    plt.show()


                         
def run():
    filename = "population_data.csv"
    dataframe = read_csv_data(filename)
    dataframe = compute_growth(dataframe)
    create_plots(dataframe)


if __name__ == "__main__":
    run()
