import csv
max_sale = 0.0
#urrent_sale = None
with open('Bestseller - Sheet1.csv', 'r') as file:
    csv_read = csv.reader(file)
    for row in csv_read:
        #print(row)
        current_sale = (row[4])
        if current_sale > str(max_sale):
            max_sale = current_sale
            bestseller_info = row
            
    
    
with open('bestseller_info.csv', 'w',newline = '') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])        
    csv_writer.writerow(bestseller_info)
    
