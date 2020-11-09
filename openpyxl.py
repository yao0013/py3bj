import openpyxl

wb = openpyxl.Work()

sheet = wb.active

sheet.title = 'new title'

sheet['A1'] = '漫威宇宙'
row = ['美国队长','钢铁侠','蜘蛛侠','鹰眼','浩克']
sheet.append(row)