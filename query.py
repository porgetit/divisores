import sys
import json

def reconstruct_sequence(n, table, sequence):
    str_n = str(n)
    
    # Casos base: si es un número del 1 al 20, no requiere operaciones
    if str_n not in table or table[str_n]["cost"] == 0:
        return
        
    node = table[str_n]
    
    # Post-order traversal: resolvemos rama izquierda, luego derecha
    reconstruct_sequence(node["left"], table, sequence)
    reconstruct_sequence(node["right"], table, sequence)
    
    # Agregamos la operación actual a la secuencia
    sequence.append(f"{n} = {node['left']} {node['op']} {node['right']}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python query.py <archivo.json> <objetivo>")
        sys.exit(1)
        
    table_file = sys.argv[1]
    target = int(sys.argv[2])
    
    with open(table_file, "r") as f:
        table = json.load(f)
        
    if str(target) not in table:
        print(f"Error: El número {target} no está en la tabla precalculada.")
        sys.exit(1)
        
    print(f"Objetivo: {target}\n")
    
    if table[str(target)]["cost"] == 0:
        print("El número ya está disponible (coste cero, pertenece al rango 1-20).")
        sys.exit(0)
        
    sequence = []
    
    reconstruct_sequence(target, table, sequence)
    
    for step in sequence:
        print(step)
        
    print(f"\nOperaciones: {len(sequence)}")
    # El tamaño de la secuencia ahora coincidirá exactamente con table[str(target)]["cost"]
