
'1 0 1 0 1 0 1 0'
'0 1 0 1 0 1 0 1'
'1 0 1 0 1 0 1 0'
'0 1 0 1 0 1 0 1'
'1 0 1 0 1 0 1 0'
'0 1 0 1 0 1 0 1'
'1 0 1 0 1 0 1 0'
'0 1 0 1 0 1 0 1'



def check_color(coord):
    return ((coord[0] % 2) + (coord[1] % 2)) % 2

def check_equel(coord_1, coord_2):
    return check_color(coord_1) == check_color(coord_2)

a =(1, 1)
b =(2, 1)

print(check_equel(a, b))