import sys
import json
from tqdm import tqdm

def build_table(max_n):
    table = {}
    
    # Casos base: 1 al 20 cuestan cero (siempre disponibles)
    for i in range(1, min(20, max_n) + 1):
        table[i] = {
            "cost": 0,
            "op": None,
            "left": None,
            "right": None
        }
        
    if max_n <= 20:
        return table
        
    # Programación dinámica estándar (Árboles) para n > 20
    for i in tqdm(range(21, max_n + 1), desc="Calculando óptimos"):
        best_cost = float('inf')
        best_op, best_left, best_right = None, None, None
        
        # 1. Evaluar todas las sumas posibles (x + y = i)
        for x in range(1, i // 2 + 1):
            y = i - x
            # El costo es la suma de construir cada parte, más 1 por la suma actual
            current_cost = table[x]["cost"] + table[y]["cost"] + 1
            if current_cost < best_cost:
                best_cost = current_cost
                best_left, best_right, best_op = x, y, '+'
                
        # 2. Evaluar todas las multiplicaciones posibles (x * y = i)
        # CORRECCIÓN: Empezamos en 2 para evitar x=1 -> y=i (que causaba el KeyError)
        for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                y = i // x
                current_cost = table[x]["cost"] + table[y]["cost"] + 1
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_left, best_right, best_op = x, y, '*'
                    
        # Guardar en la tabla
        table[i] = {
            "cost": best_cost,
            "op": best_op,
            "left": best_left,
            "right": best_right
        }
        
    return table

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python build_table.py <N>")
        sys.exit(1)
        
    max_target = int(sys.argv[1])
    computed_table = build_table(max_target)
    
    with open("table.json", "w") as f:
        json.dump(computed_table, f, indent=4)
        
    print(f"Tabla generada exitosamente en 'table.json' hasta el número {max_target}.")
