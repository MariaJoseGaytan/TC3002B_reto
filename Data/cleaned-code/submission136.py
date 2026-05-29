import openpyxl

                                                      
def create_and_update_excel(filename):
                                                       
    wb = openpyxl.Workbook()
    sheet = wb.active
    
                                            
    sheet['A1'] = "Employee"
    sheet['B1'] = "Salary"
    
    sheet['A2'] = "John"
    sheet['B2'] = 50000
    
    sheet['A3'] = "Jane"
    sheet['B3'] = 55000
    
                       
    wb.save(filename)
    
                                           
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    sheet['B2'] = 51000                          
    
                               
    wb.save(filename)
    print(f"File '{filename}' updated successfully!")

                                                   
def main():
    create_and_update_excel("employees.xlsx")

if __name__ == "__main__":
    main()
