with open("countries.txt" , 'r') as f:
    a = f.read()
with open("countries.txt" , 'w') as f:
    a = f.write("me")
print(a)


