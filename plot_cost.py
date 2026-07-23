import json
import matplotlib.pyplot as plt
import sys
import os

def plot_costs(filename, output_image="cost_plot.png"):
    if not os.path.exists(filename):
        print(f"Error: No se encontró el archivo '{filename}'.")
        sys.exit(1)

    # Cargar los datos generados por build_table.py
    with open(filename, "r") as f:
        table = json.load(f)
        
    # Convertir las claves de string a int y ordenarlas
    numbers = sorted([int(k) for k in table.keys()])
    
    # Extraer los costos en el mismo orden
    costs = [table[str(n)]["cost"] for n in numbers]
    
    # Configurar y generar el gráfico
    plt.figure(figsize=(10, 6))
    
    plt.scatter(numbers, costs, s=2, alpha=0.6, color="blue")
    
    plt.title("Costo de construcción por número (solo base 1-20)")
    plt.xlabel("Número objetivo (N)")
    plt.ylabel("Costo (cantidad de operaciones)")
    plt.grid(True, linestyle="--", alpha=0.5)
    
    plt.tight_layout()
    
    # Guardar en archivo en lugar de abrir la ventana interactiva
    plt.savefig(output_image, dpi=300)
    print(f"Gráfico guardado exitosamente en '{output_image}'.")

if __name__ == "__main__":
    # Argumentos: <archivo_json> <archivo_salida_imagen>
    table_file = sys.argv[1] if len(sys.argv) > 1 else "table.json"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "cost_plot.png"
    plot_costs(table_file, output_file)
