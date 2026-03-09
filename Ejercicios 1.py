def precedencia(op):
    if op in ['+', '-']: return 1
    if op in ['*', '/']: return 2
    if op == '^': return 3
    return 0

def infija_a_postfija(expresion):
    pila = []
    salida = []
    
    for char in expresion:
        if char.isalnum(): # Operando
            salida.append(char)
        elif char == '(':
            pila.append(char)
        elif char == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop() # Eliminar '('
        else: # Operador
            while pila and precedencia(pila[-1]) >= precedencia(char):
                salida.append(pila.pop())
            pila.append(char)
            
    while pila:
        salida.append(pila.pop())
    return "".join(salida)

def infija_a_prefija(expresion):
    # 1. Invertir expresión y cambiar paréntesis
    invertida = expresion[::-1]
    invertida = invertida.replace('(', 'TEMP').replace(')', '(').replace('TEMP', ')')
    
    # 2. Convertir a postfija
    postfija = infija_a_postfija(invertida)
    
    # 3. Invertir postfija para obtener prefija
    return postfija[::-1]

# Ejemplo de uso
expresion = "A+B*C"
print(f"Infija: {expresion}")
print(f"Postfija: {infija_a_postfija(expresion)}")
print(f"Prefija: {infija_a_prefija(expresion)}")
