import openpyxl
wb = openpyxl.load_workbook("HW13.xlsx")
file = wb["money"]
wb.create_sheet(title="good")
file2 = wb["good"]
file2["A1"].value = 1
wb.save("HW13.xlsx")