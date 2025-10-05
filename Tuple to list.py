

details = (
    "Hari",     
    "Punith",      
    14,          
    1,         
    60,        
    "Science"   
)

#  Print tuple
print("Tuple:")
print(details)

#  Convert tuple 
details_list = list(details)

# Print list
print("\nList:")
print(details_list)


print("\nAccessing values:")
print(details_list[0])
print(details_list[1])
print(details_list[2])
print(details_list[3])
print(details_list[4])
print(details_list[5])

print("\nLoop:")
for item in details_list:
    print(item)
