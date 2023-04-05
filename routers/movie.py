from fastapi import APIRouter
from fastapi import  Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from config.database import Sesion
from models.movies import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.Jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Sesion()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=201, content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Sesion()
    result = MovieService(db).get_movie_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'no encontrado'})
    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=20)) -> List[Movie]:
    db = Sesion()
    result = MovieService(db).get_movie_category(category)
    if not result:
            return JSONResponse(status_code=404, content={'message': 'no encontado'})
    return JSONResponse(content=jsonable_encoder(result))

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Sesion()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={'message': 'se ha registrado la pelicula'}) 


@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    db = Sesion()
    result = MovieService(db).get_movie_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'mensaje': 'no encontrado'})
    
    MovieService(db).update_movie(id, movie)
    return JSONResponse(content={'message': 'se ha modificado la pelicula'})
        

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict)
def delete_novie(id: int) -> dict:
    db = Sesion()
    result = MovieService(db).get_movie_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'mensaje': 'no encontrado'})
    MovieService(db).delete(id)
    return JSONResponse(status_code=200, content={'message': 'se ha eliminado la pelicula'})
