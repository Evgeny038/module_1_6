my_dict={'Evgeni': 1994, 'Sveta':1997, 'Denis': 1999}
print(my_dict)
print(my_dict['Sveta'])
my_dict['Mila'] = 2002
print(my_dict)
my_dict.update({'Koly':1991,'Petya': 2000})
print(my_dict)
my_dict.pop('Evgeni')
print(my_dict)
my_set={1,1,1,2,3,4,4,5,'машина','стол','стол'}
print(my_set)
my_set.add('cash')
my_set.add(12) #получилось добавить два новых элемента, но в разные строки, а могу ли в одной все сделать ?
print(my_set)
my_set.remove(1)
print(my_set)