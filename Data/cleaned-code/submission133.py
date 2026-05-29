import openpyxl

                                                      
def create_excel(filename):
                                                       
    wb = openpyxl.Workbook()
    sheet = wb.active
    
                                    
    sheet['A1'] = "Name"
    sheet['B1'] = "Age"
    
    sheet['A2'] = "Alice"
    sheet['B2'] = 30
    
    sheet['A3'] = "Bob"
    sheet['B3'] = 25
    
                       
    wb.save(filename)
    print(f"File '{filename}' created and data written successfully!")

                                        
def main():
    create_excel("students_basic.xlsx")

if __name__ == "__main__":
    main()
