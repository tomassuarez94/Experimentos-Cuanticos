import LIB_03 as c
import math

def test_1():
    # 1 click
    m1 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
    x = [0,2,1,5,3,10]
    assert c.canicas(m1,x,1) == [0,0,12,5,1,3], c.canicas(m1,x,2)
    # 2 clicks
    m2 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0],[1, 0, 0, 0, 1, 0]]
    x2 = [0, 2, 1, 5, 3, 10]
    assert c.canicas(m2, x2, 2) == [0,0,3,5,12,1], c.canicas(m2, x2, 2)

def test_2():
    #coeficientes reales 2 clicks
    m = [[0, 0, 0, 0, 0, 0, 0, 0],
         [1/2, 0, 0, 0, 0, 0, 0, 0],
         [1/2, 0, 0, 0, 0, 0, 0, 0],
         [0, 1/3, 0, 1, 0, 0, 0, 0],
         [0, 1/3, 0, 0, 1, 0, 0, 0],
         [0, 1/3, 1/3, 0, 0, 1, 0, 0],
         [0, 0, 1/3, 0, 0, 0, 1, 0],
         [0, 0, 1/3, 0, 0, 0, 0, 1]]
    x = [1,0,0,0,0,0,0,0]
    assert c.dos_rendijas(m,x,2) == [0.0, 0.0, 0.0, 0.027777777777777776, 0.027777777777777776, 0.1111111111111111, 0.027777777777777776, 0.027777777777777776], c.dos_rendijas(m,x,2)
    #coeficientes complejos 2 clicks
    m = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [1j / math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                  [1j / math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                  [0, -1j / math.sqrt(3), 0, 1, 0, 0, 0, 0],
                  [0, 1j / math.sqrt(3), 0, 0, 1, 0, 0, 0],
                  [0, -1j / math.sqrt(3), -1j / math.sqrt(3), 0, 0, 1, 0, 0],
                  [0, 0, 1j / math.sqrt(3), 0, 0, 0, 1, 0],
                  [0, 0, -1j / math.sqrt(3), 0, 0, 0, 0, 1]]
    x = [1, 0, 0, 0, 0, 0, 0, 0]
    assert c.dos_rendijas(m,x,2) == [0j, 0j, 0j, (0.16666666666666666+0j), (0.16666666666666666-0j), (0.6666666666666666+0j), (0.16666666666666666-0j), (0.16666666666666666+0j)], c.dos_rendijas(m,x,2)

def test_3():
    m = [[1/3,0,0],[1/3,0,1],[1/3,1,0]]
    v = [1,0,0]
    assert c.multiples(m,v) == [0.3333333333333333, 0.3333333333333333, 0.3333333333333333] , c.multiples(m,v)

def test_4():
    #Haciendo uso de la probabilidad aplicada en el experimento de doble rendija con coeficientes reales graficamos:
    v = [0.0, 0.0, 0.0, 0.166, 0.166, 0.333, 0.166, 0.166]
    p = [0.0, 0.0, 0.0, 0.027777777777777776, 0.027777777777777776, 0.1111111111111111, 0.027777777777777776, 0.027777777777777776]
    c.diagrama(v,p)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    print("Prueba exitosa")