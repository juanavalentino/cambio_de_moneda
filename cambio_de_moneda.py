"""
convertor (moneda_actual:str, monto: Z,moneda_convertir:str) : Z {
requiere = {moneda = [ARS,USD,EUR,BRL]}
asegura = {Dado una moneda y determinar su conversión devuelve el monto en el tipo de cambio}
}
"""


def conversor (moneda_actual,monto,moneda_convert):
    monedas_validas = ['ARS','USD','EUR','BRL']
    if moneda_actual in monedas_validas and moneda_convert in monedas_validas:
        if moneda_actual == 'ARS':
            if moneda_convert == 'USD':
                conversion = monto * 0.00077
                return conversion
            elif moneda_convert == 'EUR':
                conversion = monto * 0.00067
                return conversion
            elif moneda_convert == 'BRL':
                conversion = monto * 0.0043
                return conversion

        elif moneda_actual == 'USD':
            if moneda_convert == 'ARS':
                conversion = monto * 1296.55
                return conversion
            elif moneda_convert == 'EUR':
                conversion = monto * 0.87
                return conversion
            elif moneda_convert == 'BRL':
                conversion = monto * 5.62
                return conversion

        elif moneda_actual == 'EUR':
            if moneda_convert == 'ARS':
                conversion = monto * 1487.09
                return conversion
            elif moneda_convert == 'USD':
                conversion = monto * 1.15
                return conversion
            elif moneda_convert == 'BRL':
                conversion = monto * 6.45
                return conversion

        elif moneda_actual == 'BRL':
            if moneda_convert == 'ARS':
                conversion = monto * 230.69
                return conversion
            elif moneda_convert == 'USD':
                conversion = monto * 0.18
                return conversion
            elif moneda_convert == 'EUR':
                conversion = monto * 0.16
                return conversion
        elif moneda_actual == moneda_convert:
            return monto

if __name__ == "__main__":
    moneda_actual = input('Determina el valor de que queres convertir:')
    monto = int(input('Monto que queres convertir:'))
    moneda_convert = input('A que monto lo queres convertir:')
    resultado = conversor (moneda_actual,monto,moneda_convert)

    if resultado != None:
        print(f'El valor por el tipo de cambio es {resultado:.2f}')
    else:
        print('Moneda no válida')