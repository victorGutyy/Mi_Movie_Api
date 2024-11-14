from fastapi import FastAPI, Body  # importa la clase FastAPI y Body de la librería fastapi
from fastapi.responses import HTMLResponse  # importa la clase HTMLResponse de la librería fastapi

app = FastAPI() #crea una instancia de la clase FastAPI
app.title = "Mis peliculas favoritas" #asigna el valor de title a la instancia de la clase FastAPI
app.version = "0.0.1" #asigna el valor de version a la instancia de la clase FastAPI

movies_list = [
    {
        "id": 1,
        "title": "Deadpool y Wolverine",
        "overview": "Deadpool se retira, pero regresa para salvar a sus seres queridos y al mundo, con la ayuda de Wolverine",
        "year": "2024",
        "rating": 9.5
    },

     {
        "id": 2,
        "title": "Spider-Man: No Way Home",
        "overview": "Peter Parker busca ayuda de Doctor Strange para borrar su identidad secreta, pero las cosas se complican cuando se abren portales hacia el multiverso.",
        "year": "2021",
        "rating": 8.7
    },
     {
        "id": 3,
        "title": "The Godfather",
        "overview": "La historia de la familia Corleone y el ascenso de su imperio criminal en Nueva York.",
        "year": "1972",
        "rating": 9.2
    },
    {
        "id": 4,
        "title": "The Shawshank Redemption",
        "overview": "La historia de la esperanza y amistad de un hombre encarcelado injustamente.",
        "year": "1994",
        "rating": 9.3
    },
    {
        "id": 5,
        "title": "Inception",
        "overview": "Un ladrón experto en el arte de extraer secretos del subconsciente es contratado para realizar la tarea inversa: implantar una idea en la mente de alguien.",
        "year": "2010",
        "rating": 8.8
    },
    {
        "id": 6,
        "title": "Parasite",
        "overview": "Una familia pobre se infiltra poco a poco en la vida de una familia rica con intenciones ocultas.",
        "year": "2019",
        "rating": 8.6
    },
    {
        "id": 7,
        "title": "The Dark Knight",
        "overview": "Batman se enfrenta a su mayor enemigo, el Joker, en una batalla que pondrá a prueba sus principios.",
        "year": "2008",
        "rating": 9.0
    },
    {
        "id": 8,
        "title": "Pulp Fiction",
        "overview": "Varias historias entrelazadas que exploran la vida criminal y las relaciones en Los Ángeles.",
        "year": "1994",
        "rating": 8.9
    },
    {
        "id": 9,
        "title": "Schindler's List",
        "overview": "La historia real de Oskar Schindler, quien salvó a miles de judíos durante el Holocausto.",
        "year": "1993",
        "rating": 9.0
    },
    {
        "id": 10,
        "title": "Interstellar",
        "overview": "Un grupo de exploradores viaja a través de un agujero de gusano en el espacio para buscar un nuevo hogar para la humanidad.",
        "year": "2014",
        "rating": 8.6
    },
    {
        "id": 11,
        "title": "The Matrix",
        "overview": "Un hacker descubre la verdadera naturaleza de su realidad y se une a una rebelión contra los controladores del mundo.",
        "year": "1999",
        "rating": 8.7
    }
]

@app.get('/', tags=["Home"]) #definimos una ruta de la clase FastAPI y le asignamos la etiqueta "Home"
def message(): #definimos una función de la ruta
    return HTMLResponse('<h1>Hello World</h1>')  # retorna un objeto de la clase HTMLResponse

@app.get('/movies', tags=["Movies"])  # definimos una ruta de la clase FastAPI
def movies():
    return movies_list

@app.get('/movies/{id}', tags=["Movies"])
def get_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=["Movies"])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies_list if item['category'] == category]

@app.post('/movies', tags=['Movies'])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies_list.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies_list

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies_list:
        if item["id"] == id:
            item["title"] = title
            item["overview"] = overview
            item["year"] = year
            item["rating"] = rating
            item["category"] = category
            return movies_list

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            movies_list.remove(item)
            return movies_list
        
# para correr la app: uvicorn main:app --reload
# uvicorn nombreApp:app --reload --port 5000
# swagger: http://127.0.0.1:5000/docs#/




