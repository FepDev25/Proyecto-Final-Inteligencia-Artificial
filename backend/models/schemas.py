from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TextRequest(BaseModel):
    text: str

class EnfermedadBase(BaseModel):
    nombre_enfermedad: str
    descripcion: Optional[str] = None

class EnfermedadCreate(EnfermedadBase):
    pass

class Enfermedad(EnfermedadBase):
    id_enfermedad: int

    class Config:
        orm_mode = True

class SintomaBase(BaseModel):
    nombre_sintoma: str

class SintomaCreate(SintomaBase):
    pass

class Sintoma(SintomaBase):
    id_sintoma: int

    class Config:
        orm_mode = True

class PosibleCondicionBase(BaseModel):
    nombre_condicion: str
    nombre_interno: Optional[str] = None
    porcentaje: Optional[float] = 0.00

class PosibleCondicionCreate(PosibleCondicionBase):
    pass

class PosibleCondicion(PosibleCondicionBase):
    id_posible_condicion: int
    id_prediccion: int

    class Config:
        orm_mode = True

class PrediccionBase(BaseModel):
    id_enfermedad: Optional[int] = None
    url_imagen: str
    url_audio: Optional[str] = None
    resumen: Optional[str] = None
    porcentaje_coincidencia: Optional[float] = None

class PrediccionCreate(PrediccionBase):
    posibles_condiciones: List[PosibleCondicionCreate] = []

class Prediccion(PrediccionBase):
    id_prediccion: int
    fecha: datetime
    posibles_condiciones: List[PosibleCondicion] = []

    class Config:
        orm_mode = True
