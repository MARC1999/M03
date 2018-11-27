#coding:utf-8
Gasolina=input("Que tipo de gasolina quieres")
super=input("Quieres gasolina normal o turbo")
sin_plomo=input("Quieres gasolina normal o con aditivos (sabor naranja"))
diesel=input("Quieres gasolina normal o Fast&Furius:")
if(gasolina=="super") and (super=="normal"):
    print("1.50€")
else:
    if(gasolina=="Super") and (Super=="turbo"):
        print("1.55€")
    else:
        if(gasolina=="Sin_Plomo") and (Sin_Plomo=="normal"):
            print("1.60€")
        else:
                if(gasolina=="Sin_Plomo") and (Sin_Plomo=="con aditivios (sabor naranja)"):
                    print("1.65€")
                else:
                         if(gasolina=="Diesel") and (Diesel=="normal"):
                            print("1.70€")
                        else:
                                 if(gasolina=="Diesel") and (Diesel=="Fast&Furius"):
                                         print("1.75€")                               
litros=int(input("Cuantos litros quieres?")
importe=abs(gasolina*litros)
print("Tu importe es de", importe)
