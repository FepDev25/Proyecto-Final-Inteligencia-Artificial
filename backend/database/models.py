from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from .connection import Base

class Enfermedad(Base):
    __tablename__ = "enfermedades"

    id_enfermedad = Column(Integer, primary_key=True, index=True)
    nombre_enfermedad = Column(String(255), nullable=False)
    descripcion = Column(Text)

    predicciones = relationship("Prediccion", back_populates="enfermedad")
    sintomas = relationship("EnfermedadSintoma", back_populates="enfermedad")

class Sintoma(Base):
    __tablename__ = "sintomas"

    id_sintoma = Column(Integer, primary_key=True, index=True)
    nombre_sintoma = Column(String(255), nullable=False)

    enfermedades = relationship("EnfermedadSintoma", back_populates="sintoma")

class EnfermedadSintoma(Base):
    __tablename__ = "enfermedad_sintoma"

    id_enfermedad = Column(Integer, ForeignKey("enfermedades.id_enfermedad"), primary_key=True)
    id_sintoma = Column(Integer, ForeignKey("sintomas.id_sintoma"), primary_key=True)

    enfermedad = relationship("Enfermedad", back_populates="sintomas")
    sintoma = relationship("Sintoma", back_populates="enfermedades")

class Prediccion(Base):
    __tablename__ = "predicciones"

    id_prediccion = Column(Integer, primary_key=True, index=True)
    id_enfermedad = Column(Integer, ForeignKey("enfermedades.id_enfermedad"), nullable=True)
    url_imagen = Column(Text, nullable=False)
    url_audio = Column(Text)
    resumen = Column(Text)
    porcentaje_coincidencia = Column(DECIMAL(5, 2))
    fecha = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    enfermedad = relationship("Enfermedad", back_populates="predicciones")
    posibles_condiciones = relationship("PosibleCondicion", back_populates="prediccion")

class PosibleCondicion(Base):
    __tablename__ = "posibles_condiciones"

    id_posible_condicion = Column(Integer, primary_key=True, index=True)
    id_prediccion = Column(Integer, ForeignKey("predicciones.id_prediccion"), nullable=False)
    nombre_condicion = Column(String(255), nullable=False)
    nombre_interno = Column(String(100))
    porcentaje = Column(DECIMAL(5, 2), default=0.00)

    prediccion = relationship("Prediccion", back_populates="posibles_condiciones")