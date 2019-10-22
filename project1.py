import os
import time
# luas segitiga ---------------------------------------------------------------------------------
def luassegitiga():
    print("\33[31m-----------------------------------------------------------------\33[31m")
    print("\33[1;34m----                Menghitung Luas segitiga                 ----\33[1;31m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[33m-----------------------------------------------------------------\33[33m")
    print("\33[1;34m----                 create by 90s Rabbits                   ----\33[1;34m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("Menghitung luas persegi ")
    Alas = float(input("Alas :"))
    Tinggi = float(input("Tinggi :"))
    a = 1/2 * Alas * Tinggi
    print(a)
    print("Anda ingin kembali ke menu [Y/N]")
    a = input("Masukan Pilihan anda :")
    if a == "y" or "Y":
        Menu()
        os.system("cls") or os.system("clear")
    else:
        exit("Terima kasih")
# Luas persegi ----------------------------------------------------------------------------------
def Luaspersegi():
    print("\33[31m-----------------------------------------------------------------\33[31m")
    print("\33[1;34m----                Menghitung Luas persegi                  ----\33[1;31m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[33m-----------------------------------------------------------------\33[33m")
    print("\33[1;34m----                 create by 90s Rabbits                   ----\33[1;34m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    sisi = int(input("masukan sisi :"))

    a = sisi * sisi
    print("Luas persegi adalah :",a)
    print("Anda ingin kembali ke menu [Y/N]")
    a = input("Masukan Pilihan anda :")
    if a == "y" or "Y":
        Menu()
        os.system("cls") or os.system("clear")
    else:
        exit("Terima kasih")
def cramer3x3():

    def perkalian(x,y):
        return x * y

    print("\33[31m-----------------------------------------------------------------\33[31m")
    print("\33[1;34m----    penyelesaian linier menggunakan Aturan cramer3x3     ----\33[1;31m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[33m-----------------------------------------------------------------\33[33m")
    print("\33[1;34m----                 create by 90s Rabbits                   ----\33[1;34m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    a11 = int(input("Masukan Angka a11 :"))
    a12 = int(input("Masukan Angka a12 :"))
    a13 = int(input("Masukan Angka a13 :"))
    a21 = int(input("Masukan Angka a21 :"))
    a22 = int(input("Masukan Angka a22 :"))
    a23 = int(input("Masukan Angka a23 :"))
    a31 = int(input("Masukan Angka a31 :"))
    a32 = int(input("Masukan Angka a32 :"))
    a33 = int(input("Masukan Angka a33 :"))
    c1  = int(input("Masukan Angka  c1 :"))
    c2  = int(input("Masukan Angka  c2 :"))
    c3  = int(input("Masukan Angka  c3 :"))

    a = a11
    b = a12
    c = a13
    d = a21
    e = a22
    f = a23
    g = a31
    h = a32
    i = a33
    j = c1
    k = c2
    l = c3

    # mencari determinan
    u = perkalian(b,f) - perkalian(e,c)
    v = perkalian(a,f) - perkalian(d,c)
    o = perkalian(a,e) - perkalian(d,b)
    y = u * g
    Y = v * h
    G = o * i
    U = y - Y + G
    # determinan
    print("Bentuk Determinan")
    print(""""""""    """       |""""",a,""" """,b,""" """,c,"""|""")
    print("""""""""  D = |""""",d,""" """,e,""" """,f,"""|""")
    print(""""""""    """       |""""",g,""" """,h,""" """,i,"""|""")
    print("-------------------------------------------------------")
    # Mencari determinan 1
    print("Mencari determinan 1")
    print(   """""""+",g,"""|""""",b,""" """,c,"""|""")
    print("""""""""      |""""",e,""" """,f,"""|""")
    print("-------------------------------------------------------")
    # Mencari determinan 2
    print("Mencari determinan 2")
    print(   """""""-",h,"""|""""",a,""" """,c,"""|""")
    print("""""""""      |""""",d,""" """,f,"""|""")
    print("-------------------------------------------------------")
    # Mencari determinan 3
    print("Mencari determinan 3")
    print(   """""""+",i,"""|""""",a,""" """,b,"""|""")
    print("""""""""      |""""",d,""" """,e,"""|""")
    print("-------------------------------------------------------")
    print("Hasil Dari determinan : ",U)
    print("-------------------------------------------------------")
    # Mencari Dx
    x = perkalian(b, f) - perkalian(e, c)
    z = perkalian(j, f) - perkalian(k, c)
    S = perkalian(j, e) - perkalian(k, b)
    R = x * l
    W = z * h
    Q = S * i
    q = R - W + Q
    # -------------------------------------------------------------
    print("Bentuk Determinan Dx ")
    print(""""""""     """       |""""",j,""" """,b,""" """,c,"""|""")
    print("""""""""  Dx = |""""",k, """ """,e, """ """,f, """|""")
    print(""""""""     """       |""""",l,""" """,h,""" """,i,"""|""")
    print("-------------------------------------------------------")
    print("Hasil Dari Dx :",q)
    print("-------------------------------------------------------")
    # -------------------------------------------------------------
    E = perkalian(j, f) - perkalian(k, c)
    I = perkalian(a, f) - perkalian(d, c)
    o = perkalian(a, k) - perkalian(d, j)
    a1 = E * g
    a2 = I * l
    a3 = o * i
    a4 = a1 - a2 + a3
    print("Bentuk Determinan Dy")
    print(""""""""     """       |""""", a, """ """, j, """ """, c, """|""")
    print("""""""""  Dx = |""""", d, """ """, k, """ """, f, """|""")
    print(""""""""     """       |""""", g, """ """, l, """ """, i, """|""")
    print("-------------------------------------------------------")
    print("Hasil Dari Dy :", a4)
    print("-------------------------------------------------------")
    # ------------------------------------------------------------
    b1 = perkalian(b,k) - perkalian(e,j)
    b2 = perkalian(a,k) - perkalian(d,j)
    b3 = perkalian(a,e) - perkalian(d,b)
    b4 = b1 * g
    b5 = b2 * h
    b6 = b3 * l
    b7 = b4 - b5 + b6
    print("Bentuk Determinan Dz")
    print(""""""""     """       |""""", a, """ """, b, """ """, j, """|""")
    print("""""""""  Dx = |""""", d, """ """, e, """ """, k, """|""")
    print(""""""""     """       |""""", g, """ """, h, """ """, l, """|""")
    print("-------------------------------------------------------")
    print("Hasil Dari Dz :", b7)
    print("-------------------------------------------------------")
    # ------------------------------------------------------------
    c1 = q / U
    c2 = a4 / U
    c3 = b7 / U
    print("Sehingga anda mendapat")
    print("x = Dx / D = ",c1)
    print("Sehingga anda mendapat")
    print("y = Dy / D = ", c2)
    print("Sehingga anda mendapat")
    print("z = Dz / D = ", c3)
    # Pilihan kembali Ke menu atau tidak -----------------------------------------------------
    time.sleep(4)
    print("Anda ingin kembali ke menu [Y/N]")
    a = input("Masukan Pilihan anda :")
    if a == "y" or "Y":
        Menu()
        os.system("cls") or os.system("clear")
    else:
        exit("Terima kasih")
# Aturan Cramer ----------------------------------------------------------------------------
def Determinan():
    def perkalian(x, y):
        return x * y

    def perkurangan(x, y):
        return x - y

    def pembagian(x, y):
        return x / y

    print("\33[31m-----------------------------------------------------------------\33[31m")
    print("\33[1;34m----    penyelesaian linier menggunakan Aturan cramer2x2     ----\33[1;31m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[33m-----------------------------------------------------------------\33[33m")
    print("\33[1;34m----                 create by 90s Rabbits                   ----\33[1;34m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    a11 = int(input("Masukan Nilai a11 :"))
    a12 = int(input("Masukan Nilai a12 :"))
    a21 = int(input("Masukan Nilai a21 :"))
    a22 = int(input("Masukan Nilai a22 :"))
    c1   = int(input("Masukan Nilai c1 :"))
    c2   = int(input("Masukan Nilai c2 :"))
    os.system("cls")
    # perkalian determinan
    a = perkalian(a11,a22)
    b = perkalian(a21,a12)
    f = perkurangan(a,b)
    print("Bentuk Determinan")
    print("|", a11,"  ",a12, "|")
    print("|", a21,"  ",a22, "|")
    print("Hasil Determinan =",f)
    print("--------------------------")
    # perkalian determinan x
    A = perkalian(c1,a22) - perkalian(c2,a12)
    print("Bentuk Determinan Dx")
    print("|", c1, "  ", a12, "|")
    print("|", c2, "  ", a22, "|")
    print("Hasil Determinan =", A)
    print("--------------------------")
    # perkalian determinan y
    x = perkalian(a11,c2) - perkalian(a21,c1)
    print("Bentuk Determinan Dy")
    print("|", a11, "  ",c1, "|")
    print("|", a21, "  ",c2, "|")
    print("Hasil Determinan =", x)
    print("--------------------------")
    T = pembagian(A,f)
    print("Sehingga anda mendapat")
    print("x = Dx / D = ",T)
    t = pembagian(x,f)
    print("Sehingga anda mendapat")
    print("y = Dy / D = ",t)
    time.sleep(4)
    # Pilihan kembali Ke menu atau tidak -----------------------------------------------------
    print("Anda ingin kembali ke menu [Y/N]")
    a = input("Masukan Pilihan anda :")
    if a == "y" or "Y":
        Menu()
        os.system("cls") or os.system("clear")
    else:
        exit("Terima kasih")
# Matrix invers 3x3 ----------------------------------------------------------------------------
def InversMatrix3x3():

    # fungsi perkalian
    def perkalian(o, u):
        return o * u

    def perkalian2(u, o, t):
        return u * o * t

    print("\33[31m-----------------------------------------------------------------\33[31m")
    print("\33[1;34m----                 TOOLS Invers MATRIX3x3                  ----\33[1;31m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[33m-----------------------------------------------------------------\33[33m")
    print("\33[1;34m----                 create by 90s Rabbits                   ----\33[1;34m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[1;33mPencari Matriks 3x3\33[1;33m")
    print("Contoh :")
    print("| A     B      C |")
    print("| D     E      F |")
    print("| G     H      I |")
    print("\33[1;30mIsikan input dengan angka\33[1;30m")
    a = int(input(" Nilai A = "))

    b = int(input(" Nilai B = "))

    c = int(input(" Nilai C = "))

    d = int(input(" Nilai D = "))

    e = int(input(" Nilai E = "))

    f = int(input(" Nilai F = "))

    g = int(input(" Nilai G = "))

    h = int(input(" Nilai H = "))

    i = int(input(" Nilai I = "))
    os.system("cls")

    # Mencari Determinan
    detA = perkalian2(a, e, i) + \
           perkalian2(b, f, g) + \
           perkalian2(c, d, h) - \
           perkalian2(g, e, c) - \
           perkalian2(h, f, a) - \
           perkalian2(i, d, b)
    print("\n[Matriks A]")

    print("| ", a, " ", b, " ", c, "|")
    print("| ", d, " ", e, " ", f, "|")
    print("| ", g, " ", h, " ", i, "|")

    print("\n[Determinan A]")

    print("| ", a, " ", b, " ", c, ":", a, " ", b, "|")
    print("| ", d, " ", e, " ", f, ":", d, " ", e, "| ===> DetA = ", detA)
    print("| ", g, " ", h, " ", i, ":", g, " ", h, "|")

    # Mencari Adjoin

    a11 = perkalian(e, i) - perkalian(h, f)

    a12 = perkalian(d, i) - perkalian(g, f)

    a13 = perkalian(d, h) - perkalian(g, e)

    a21 = perkalian(b, i) - perkalian(h, c)

    a22 = perkalian(a, i) - perkalian(g, c)

    a23 = perkalian(a, h) - perkalian(g, b)

    a31 = perkalian(b, f) - perkalian(e, c)

    a32 = perkalian(a, f) - perkalian(d, c)

    a33 = perkalian(a, e) - perkalian(d, b)
    print("-------------------------------------------------------------------------------")
    print('[Adjoin]')
    print("A11 = +|", e, "", i, "|= ", a11 * (1), "A12 = -|", d, "", i, "|=", a12 * (-1), "A13 = +|", d, "", h, "|=",
          a13 * (1), )
    print("       |", h, "", f, "|                 |", g, "", f, "|                |", g, "", e, "|")

    print("A21 = -|", b, "", i, "|= ", a21 * (-1), "A22 = +|", a, "", i, "|=", a22 * (1), "A23 = -|", a, "", h, "|=",
          a23 * (-1), )
    print("       |", h, "", c, "|                 |", g, "", c, "|                |", g, "", b, "|")

    print("A31 = +|", b, "", f, "|= ", a31 * (1), "A32 = -|", a, "", f, "|=", a32 * (-1), "A33 = +|", a, "", e, "|=",
          a33 * (1), )
    print("       |", e, "", c, "|                 |", d, "", c, "|                |", d, "", b, "|")

    # Menampilkan Adjoin

    print("-------------------------------------------------------------------------------")

    print("[Koy A] = | ", a11 * (1), "", a12 * (-1), "", a13 * (1), "|")

    print("          | ", a21 * (-1), "", a22 * (1), "", a23 * (-1), "|")

    print("          | ", a31 * (1), "", a32 * (-1), "", a33 * (1), "|")

    print("")

    print("Adjoin di Transpose = ")

    print("[A Transpose] = | ", a11 * (1), '', a21 * (-1), '', a31 * (1), '|')

    print('                | ', a12 * (-1), '', a22 * (1), '', a32 * (-1), '|')

    print('                | ', a13 * (1), '', a23 * (-1), '', a33 * (1), '|')

    print("-------------------------------------------------------------------------------")
    time.sleep(4)
    # Pilihan kembali Ke menu atau tidak -----------------------------------------------------
    print("Anda ingin kembali ke menu [Y/N]")
    a = input("Masukan Pilihan anda :")
    if a == "y" or "Y":
        Menu()
        os.system("cls") or os.system("clear")
    else:
        exit("Terima kasih")
# Matrix invers 2x2 ----------------------------------------------------------------------------
def Matrix2x2():
    def perkalian(x,y):
        return x * y
    print("\33[31m-----------------------------------------------------------------\33[31m")
    print("\33[1;34m----                 TOOLS Invers MATRIX2x2                  ----\33[1;31m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[33m-----------------------------------------------------------------\33[33m")
    print("\33[1;34m----                 create by 90s Rabbits                   ----\33[1;34m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[1;33mPencari Matriks 2x2\33[1;33m")
    print("Contoh :")
    print("A = |  A    B  |")
    print("    |  C    D  |")
    print("--------------------------")
    print("Masukan input dengan angka")
    a = int(input("Masukan nilai A :"))
    b = int(input("Masukan nilai B :"))
    c = int(input("Masukan nilai C :"))
    d = int(input("Masukan nilai D :"))
    print("---------------------------------------")
    a1 = a
    b1 = perkalian(b,-1.0)
    c1 = perkalian(c,-1.0)
    d1 = d

    hasil = (perkalian(a,d)-perkalian(c,b))
    print("Bentuk semula")
    print("A = A-1|",a,"",b,"|")
    print("       |",c,"",d,"|")
    print("---------------------------------------")
    print("Bentuk Adjoin")
    print("A = A-1|",d,"",b*(-1),"|")
    print("       |",c*(-1),"",a,"|")
    print("---------------------------------------")
    if hasil == 0:
        print("A = |",d1,"",b1,"|")
        print("    |",c1,"",a1,"|")
    else:
        print("Penyelesaian")
        print("|",perkalian(d1,(1.0/hasil)),"| |",perkalian(b1,(1.0/hasil)))
        print("|",perkalian(c1,(1.0/hasil)),"| |",perkalian(a1,(1.0/hasil)))
    time.sleep(4)
    # Pilihan kembali Ke menu atau tidak -----------------------------------------------------
    print("Anda ingin kembali ke menu [Y/N]")
    a = input("Masukan Pilihan anda :")
    if a == "y" or "Y":
        Menu()
        os.system("cls") or os.system("clear")
    else:
        exit("Terima kasih")
def Menu():
    print("\33[31m-----------------------------------------------------------------\33[31m")
    print("\33[1;34m----                     MENU PEMILIHAN                      ----\33[1;31m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[33m-----------------------------------------------------------------\33[33m")
    print("\33[1;34m----                 create by 90s Rabbits                   ----\33[1;34m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("1. Meyelesaikan persamaan linier dengan aturan Cramer 2x2")
    print("2. Mencari InversMatrix Ordo 3x3")
    print("3. Mencari InversMatrix Ordo 2x2")
    print("4. Meyelesaikan persamaan linier dengan aturan Cramer 3x3")
    print("5. Menghitung Luas persegi")
    print("6. Menghitung Luas segitiga")
    print("0. Exit")
    menu = input("Masukan Pilihan Anda :")
    os.system("cls") or os.system("clear")
    if menu == "1":
        Determinan()
    elif menu == "2":
        InversMatrix3x3()
    elif menu == "3":
        Matrix2x2()
    elif menu == "4":
         cramer3x3()
    elif menu == "5":
        Luaspersegi()
    elif menu == "6":
        luassegitiga()
    elif menu == "0":
        exit("Terimakasih")
    else:
        print("Menu salah")

print (Menu())
