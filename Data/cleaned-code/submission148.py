import pandas as pd
import matplotlib.pyplot as plt


                            
def read_csv(file_path):
    data = pd.read_csv(file_path)
    return data


                                      
def compute_growth(data):
    data['Growth_Percent'] = data['Population'].pct_change() * 100
    return data


                                                   
def visualize_data(data):
    plt.figure(figsize=(10, 6))

                      
    plt.subplot(2, 1, 1)
    plt.plot(data['Year'], data['Population'], marker='o', linestyle='-')
    plt.title('Population Trend Over Years')
    plt.xlabel('Year')
    plt.ylabel('Population')

                             
    plt.subplot(2, 1, 2)
    plt.plot(data['Year'], data['Growth_Percent'], marker='o', linestyle='-', color='orange')
    plt.title('Yearly Growth Percentage')
    plt.xlabel('Year')
    plt.ylabel('Growth Percentage (%)')

    plt.tight_layout()
    plt.show()


                     
def run():
    file_path = "population_data.csv"
    data = read_csv(file_path)
    data = compute_growth(data)
    visualize_data(data)


if __name__ == "__main__":
    run()