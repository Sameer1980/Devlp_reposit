from openpyxl import Workbook
# Create a workbook
wb = Workbook()
# Change the name of worksheet to changed sheet
ws = wb.active
ws.title = "changed sheet"
wb.save('sample_book.xlsx')