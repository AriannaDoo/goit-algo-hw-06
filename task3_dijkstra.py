import networkx as nx
from task1_graph import build_graph

"""
Алгоритм Дейкстри для знаходження найкоротших шляхів
"""

def build_weighted_graph() -> nx.Graph:
    G = build_graph()

    # Умовні "хвилини в дорозі" між станціями
    weights = {
        ("Groenplaats", "Meir"): 2,
        ("Meir", "Opera"): 2,
        ("Opera", "Astrid"): 2,
        ("Astrid", "Diamant"): 2,
        ("Diamant", "Plantin"): 2,
        ("Astrid", "Schijnpoort"): 3,
        ("Schijnpoort", "Sport"): 2,
        ("Sport", "Sportpaleis"): 2,
        ("Schijnpoort", "Luchtbal"): 4,
        ("Astrid", "Elisabeth"): 1,
        ("Elisabeth", "Handel"): 2,
        ("Handel", "Schijnpoort"): 2,
        ("Astrid", "Carnot"): 1,
        ("Carnot", "Drink"): 2,
        ("Drink", "Zegel"): 3,
    }

    for (u, v), w in weights.items():
        G[u][v]["weight"] = w

    return G


def main():
    G = build_weighted_graph()

    paths = nx.single_source_dijkstra_path(G, source="Groenplaats", weight="weight")

    print("Найкоротші шляхи від Groenplaats:")
    for station, path in paths.items():
        print(f"{station:12s} -> {path}")

    print("""
Висновок :
Алгоритм Дейкстри дозволяє знайти оптимальні маршрути
у зваженому графі, що є критично важливим
для транспортних та навігаційних систем.
""")


if __name__ == "__main__":
    main()
