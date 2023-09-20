import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(actorOrigen, actorDestino):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    
    """
    #State = ID del Actor
    #Parent = Nodo Padre
    #Action = ID de la Pelicula que asoicia al actor del nodo padre con el actor del nodo actual
    #Node = (State, Parent, Action)

    #Inicializamos Frontera
    frontera = QueueFrontier()

    #Inicializamos Conjunto de Nodos Explorados
    explorados = set()

    #Inicializamos Nodo de Inicio
    nodoInicial = Node(state=actorOrigen, parent=None, action=None)
    
    #Agregamos Nodo Inicial a la Frontera
    frontera.add(nodoInicial)
    
    #Loop infinito hasta encontrar la solución o recorrer todos los nodos
    while True:

        #Si la frontera esta vacia, no hay solución
        if frontera.empty():
            return None
        
        #Sacamos el primer nodo de la frontera para analizarlo
        #Inicialmente será el nodoInicial (actorOrigen)
        node = frontera.remove()
        
        #Si el actor del nodo es el actorDestino, encontramos la solución
        if node.state == actorDestino:
            #Creamos una lista de tuplas (movie_id, person_id) que representan la solución
            solution = []

            #Recorremos los nodos hasta llegar al nodoInicial (actorOrigen)
            while node.parent is not None:
                #Agregamos la tupla (movie_id, person_id) a la solución (path)
                solution.append((node.action,node.state))
                #El nodo actual pasa a ser el nodo padre (Vamos haciendo backtracking)
                node = node.parent
            
            #Invertimos la solución para que quede en el orden correcto (actorOrigen -> actorDestino) y no (actorDestino -> actorOrigen)
            solution.reverse()
            #Devolvemos la solución
            return solution
        
        #Si el actor del nodo no es el actorDestino, lo agregamos al conjunto de nodos explorados para no reexplorarlo
        explorados.add(node.state) 
        
        #Agregamos los vecinos del nodo a la frontera
        #Por cada pelicula en la que participa el actor del nodo, agregamos a la frontera los actores que participan en esa pelicula
        for movie_id, person_id in neighbors_for_person(node.state):
            #Se agregan solo si ya no estan en la frontera y no fueron explorados
            if not frontera.contains_state(person_id) and person_id not in explorados:
                #El nodo actual se convierte en el padre, la pelicula en la accion con la que se llega al actor del nodo
                child = Node(state=person_id, parent=node, action=movie_id)
                #Agrego a la frontera
                frontera.add(child) 
            

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
