import openpyxl

                                                    
def read_excel(filename):
                                                   
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    
                                   
    for row in sheet.iter_rows(values_only=True):
        print(row)

                                                          
def main():
    print("Reading data from 'students_with_city.xlsx':")
    read_excel("students_with_city.xlsx")

if __name__ == "__main__":
    main()
