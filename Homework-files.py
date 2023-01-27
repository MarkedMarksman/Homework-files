import os
current = os.getcwd()
file_name = 'Cook_book.txt'
full_path = os.path.join(current,file_name)
print(full_path)

# cook_book = {}

# # with open(full_path,'rt',encoding='utf-8') as f:
# #     cook_book = {}
# #     for line in f:
# #         dish = line.strip()
# #         ingridients_count =(int(f.readline().strip()))
# #         ingridients = []
# #         for i in range(ingridients_count):
# #             ing = f.readline().strip()
# #             ingridient_name,number,measure = ing.split(' | ')
# #             ingridients.append({
# #                 'ingridient_name': ingridient_name,
# #                 'number': number ,
# #                 'measure': measure,
# #             })
# #         f.readline()
# #         cook_book[dish] = ingridients

# def get_shop_list_by_dishes(dishes,person_count):
#     dishes_dict = {}
#     for dish in dishes:
#         if dish in cook_book:
#             for ingridient in cook_book[dish]:
#                 dishes_dict[ingridient['ingridient_name']] = {
#                 'number':int(ingridient['number']) * person_count,'measure':ingridient['measure']
#                 } 

#     return print(dishes_dict)  

# get_shop_list_by_dishes(['Омлет','Фахитос'],4)

file_1 = '1.txt'
file_2 = '2.txt'
file_3 = '3.txt'
file_4 = 'New_text.txt'
full_path_1 = os.path.join(current,file_1)
full_path_2 = os.path.join(current,file_2)
full_path_3 = os.path.join(current,file_3)
full_path_4 = os.path.join(current,file_4)
text_dict = {}
string_dict = {}

with open (full_path_1, 'rt', encoding='utf-8') as f:
    string_count = 0
    first_text = []
    for i in f:
        first_text.append(i)
        string_count += 1
        text_dict[file_1] = first_text

string_dict.setdefault('1.txt',string_count)

with open (full_path_2, 'rt', encoding='utf-8') as f:
    string_count = 0
    second_text = []
    for i in f:
        second_text.append(i)
        string_count += 1
        text_dict[file_2] = second_text

string_dict.setdefault('2.txt',string_count)

with open (full_path_3, 'rt', encoding='utf-8') as f:
    string_count = 0
    third_text = []
    for i in f:
        third_text.append(i)
        string_count += 1
        text_dict[file_3] = third_text
string_dict.setdefault('3.txt',string_count,)

import operator
sorted_dict = dict(sorted(string_dict.items(),key=operator.itemgetter(1)))

with open(full_path_4,'w',encoding='utf-8') as f:
    for k,v in sorted_dict.items():
        print(k,file=f)
        print(v,file=f)
        for i in text_dict[k]:
            text = i.strip()
            print(text,file=f)


# for i in sorted_files:
#     for k in string_dict.keys() :
#         if string_dict[k] == i:
#             sorted_dict[k] = string_dict[k]

# new_text = ""

# for k,v in sorted_dict.items():
#     new_text += k
#     for j in v:
#         new_text += str(j)

# print(new_text)
