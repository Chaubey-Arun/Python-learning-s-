# # Find the Birthday of the Person 

# Name = input('Enter The name of Person \n')
# dict1 = {'Arun':'21/11/1995' 
#          , 'karan' : '33/2/2993'
#         ,'saktiman': '34/3/3333' }          

# if Name in dict1:
#     print ('Mr./Mrs {} is born on {}' .format(Name,dict1[Name])
#         )
# else:
#     print('Mr/Mrs .{} is not Found'.format(Name))

# ---------------------------------------------------------------------------
# Challenge : Finding Meanings in Dictionary

# dict1 ={
# 'piece' : 'senetence which makes wonders'
# ,'parch': 'a piece of cloth or other material used to mend or surengthen a tom or weak poin'
# ,'area' : 'a region or part of a town, a country, or the world'
# ,'visit': 'go to see aed spend time with(someone)' 
# }
# key= list(dict1.keys())
# value = list(dict1.values())
# lent= [len(x) for x in value]
# max_value= max(lent)
# min_value= min(lent)

# max_index = lent.index(max_value)
# min_index = lent.index(min_value)

# print('max_key_value :::' ,key[max_index],value[max_index])
print('Min key-vlaue:::',key[min_index],value[min_index])
    


