from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=65)
    overview: str = Field(min_length=20, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=0.1, le=10)
    category: str = Field( min_length=2, max_length=30)


    class Config:
        schema_extra = {
            'example': {
                'title': 'mi pelicula',
                'overview': 'descripcion de la pelicula',
                'year': 2023,
                'rating': 9.1,
                'category': 'Acción'

            }
        }