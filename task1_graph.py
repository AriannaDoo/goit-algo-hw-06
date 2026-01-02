import networkx as nx
import matplotlib.pyplot as plt

"""
Створення та аналіз графа реальної транспортної мережі.

Модель: підземний трамвай (Premetro) міста Антверпен.
Вершини — станції
Ребра — прямі тунельні з'єднання
"""

def build_graph() -> nx.Graph:
    G = nx.Graph()

    # === ВЕРШИНИ (СТАНЦІЇ) ===
    stations = [
        "Groenplaats", "Meir", "Opera", "Astrid",
        "Diamant", "Plantin",
        "Schijnpoort", "Sport", "Sportpaleis", "Luchtbal",
        "Elisabeth", "Handel",
        "Carnot", "Drink", "Zegel"
    ]
    G.add_nodes_from(stations)

    # === РЕБРА (З'ЄДНАННЯ) ===
    edges = [
        ("Groenplaats", "Meir"),
        ("Meir", "Opera"),
        ("Opera", "Astrid"),
        ("Astrid", "Diamant"),
        ("Diamant", "Plantin"),
        ("Astrid", "Schijnpoort"),
        ("Schijnpoort", "Sport"),
        ("Sport", "Sportpaleis"),
        ("Schijnpoort", "Luchtbal"),
        ("Astrid", "Elisabeth"),
        ("Elisabeth", "Handel"),
        ("Handel", "Schijnpoort"),
        ("Astrid", "Carnot"),
        ("Carnot", "Drink"),
        ("Drink", "Zegel"),
    ]
    G.add_edges_from(edges)

    return G


def visualize_graph(G: nx.Graph) -> None:
    """
    Ручне позиціонування вершин для відповідності схемі метро
    """
    pos = {
        "Groenplaats": (-6, 0),
        "Meir": (-4, 0),
        "Opera": (-2, 0),
        "Astrid": (0, 0),
        "Diamant": (0, -2),
        "Plantin": (0, -4),
        "Schijnpoort": (2, 2),
        "Sport": (4, 3),
        "Sportpaleis": (6, 4),
        "Luchtbal": (2, 4),
        "Elisabeth": (-1, 2),
        "Handel": (1, 3),
        "Carnot": (2, -1),
        "Drink": (4, -2),
        "Zegel": (6, -3),
    }

    plt.figure(figsize=(12, 7))
    nx.draw(G, pos, with_labels=True, node_size=1600, font_size=10)
    plt.title("Antwerp Premetro — граф транспортної мережі")
    plt.show()


def main():
    G = build_graph()

    print("=== АНАЛІЗ ГРАФА ===")
    print(f"Кількість вершин: {G.number_of_nodes()}")
    print(f"Кількість ребер: {G.number_of_edges()}")

    print("\nСтупінь вершин:")
    for node, degree in G.degree():
        print(f"{node:12s} -> {degree}")

    visualize_graph(G)

    print("""
Висновок :
Граф дозволяє наочно змоделювати реальну транспортну мережу.
Центральні станції (наприклад Astrid) мають більший ступінь,
що відповідає їх ролі транспортних вузлів.
""")


if __name__ == "__main__":
    main()
