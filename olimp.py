box = 0
apples = 0

f = open("input_data", 'r')
#line = f.readline()
text = f.read()


print(text)
print('data type', type(text))

line_list = text.split('\n')
print(line_list)

f.close()

box = int(line_list[0])
apples = int(line_list[1])

print(box * apples)

f = open('output_data.txt', 'w')
f.write(str(box * apples))
f.close()