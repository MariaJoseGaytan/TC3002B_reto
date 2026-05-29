import pandas as pd
import matplotlib.pyplot as plt


               
def load_data(file_name):
    df = pd.read_csv(file_name)
    return df


                                      
def calculate_growth(df):
    df['Growth'] = df['Population'].pct_change() * 100
    return df


                                          
def plot_data(df):
    plt.figure(figsize=(10, 6))

                     
    plt.subplot(2, 1, 1)
    plt.plot(df['Year'], df['Population'], marker='o', linestyle='-')
    plt.title('Population Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population')

                      
    plt.subplot(2, 1, 2)
    plt.plot(df['Year'], df['Growth'], marker='o', linestyle='-', color='orange')
    plt.title('Population Growth Rate')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')

    plt.tight_layout()
    plt.show()


                                
def main():
    file_name = "population_data.csv"
    df = load_data(file_name)
    df = calculate_growth(df)
    plot_data(df)


if __name__ == "__main__":
    main()
