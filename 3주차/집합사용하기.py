# foods = ['된장찌개','피자','제육볶음','된장찌개']
# foods_set = set(foods)

# print(foods, foods_set)

menu1 = set(['된장찌개', '피자', '제육볶음'])
menu2 = set(['된장찌개','떡국','김밥'])

menu3 = menu1 | menu2
print(menu3)
menu3 = menu1 & menu2
print(menu3)
menu3 = menu1 - menu2
print(menu3)