#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funcao.py
#  
#  Copyright 2018 20181bsi0121 <20181bsi0121@SR6192>
#  
# 

def main():
    
    x = int(input("Digite o valor de X: "));
    y = int(input("Digite o valor de Y: "));

    numerador = 0;
    denominador = 0;

    numerador = ((x*x) + (3*x) + (y*y) );
    denominador = ((x*y) - (5*y) - (3*x) + 15)

    if  denominador <=0:
        print('Resposta de F(X e Y): ',numerador,' / ',denominador);
    else:    
        print('Resposta de F(X e Y): ',(numerador / denominador));


    return 0

if __name__ == '__main__':
	main()
