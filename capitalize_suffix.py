import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(name):
    return name.capitalize()
result_map = list(map(capitalize_suffix, suffixes))

#random_names = []
#names = ['kelly', 'larissa', 'raissa', 'ange', 'prudencia', 'darisca',' vanessa,' 'beatrice']
def create_user_name(list1, list2):
    return random.choice(list1) + ' ' + random.choice(list2)
random_names = [create_user_name(prefixes, result_map) for name in range(10)]
    

def fire_in_name(name):
    return 'Fire' in name
   
    
    
def concatenate_names(name1, name2):
    return name1 + ' ' + name2

filtered_name = list(filter(fire_in_name, random_names))
reduced_name = reduce(concatenate_names, filtered_name,' ' )

def display_name_info():
    print('Fantasy Names: ')
    for name in random_names:
        print(name)
    print(f'Filtered names with \'Fire\': {filtered_name}')
    print('Concatenated names:', reduced_name)
    
display_name_info() 
    
        
    
    