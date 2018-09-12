'''
matrices  cuyos indices o keys son tuplas


'''

matrix ={
    (0,0):3,
    (0,2):-2,
    (0,3): "tres",

    (1,1): "fila 1 1",
    (2,1): 7,
    (3,3): -10
}

if ( 1,1 ) in matrix:
    print(matrix[(1,1)])
else:
    print("0")


element = matrix.get((4, 4), 1000)
print(element)