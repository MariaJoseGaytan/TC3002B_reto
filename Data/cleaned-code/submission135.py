import openpyxl

                                                                
def create_excel_different_data(filename):
                                                       
    wb = openpyxl.Workbook()
    sheet = wb.active
    
                                              
    sheet['A1'] = "Product"
    sheet['B1'] = "Price"
    
    sheet['A2'] = "Laptop"
    sheet['B2'] = 999.99
    
    sheet['A3'] = "Smartphone"
    sheet['B3'] = 499.99
    
                       
    wb.save(filename)
    print(f"File '{filename}' created with product data successfully!")

                                                          
def main():
    create_excel_different_data("products.xlsx")

if __name__ == "__main__":
    main()
