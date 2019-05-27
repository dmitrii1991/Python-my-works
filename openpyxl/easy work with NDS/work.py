from openpyxl import load_workbook

column = {}
i = 1
DAS = load_workbook('DAS.xlsx') #загружаем файл
print(DAS.sheetnames) #показать все листы

DASwork = DAS['Work 1'] # назначили раб лист

for row in DASwork.iter_rows(min_row=1, max_col=5, max_row=1, values_only=True): #  закрепили название столбцов
    for value in row:
        column[i] = value
        i += 1

print(column)

for x in range(2, 6):
    for y in range(1, 6):
        if column[y] == 'цена без НДС':
            price_wh_NDS = DASwork.cell(row=x, column=y).value
        elif column[y] == 'Кол-во':
            count = DASwork.cell(row=x, column=y).value
        elif column[y] == 'Общая цена БЕЗ НДС':
             DASwork.cell(row=x, column=y).value = price_wh_NDS * count
        elif column[y] == 'Общая цена с НДС':
            DASwork.cell(row=x, column=y).value = price_wh_NDS * count * 1.2


        print(DASwork.cell(row=x, column=y).value)

DAS.save('database.xlsx')
