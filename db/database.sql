-- Crear la tabla de enfermedades
CREATE TABLE enfermedades (
    id_enfermedad SERIAL PRIMARY KEY,
    nombre_enfermedad VARCHAR(255) NOT NULL,
    descripcion TEXT
);

CREATE TABLE sintomas (
    id_sintoma SERIAL PRIMARY KEY,
    nombre_sintoma VARCHAR(255) NOT NULL
);

CREATE TABLE enfermedad_sintoma (
    id_enfermedad INT REFERENCES enfermedades(id_enfermedad) ON DELETE CASCADE,
    id_sintoma INT REFERENCES sintomas(id_sintoma) ON DELETE CASCADE,
    PRIMARY KEY (id_enfermedad, id_sintoma)
);


-- Crear la tabla de predicciones
CREATE TABLE predicciones (
    id_prediccion SERIAL PRIMARY KEY,
    id_enfermedad INT REFERENCES enfermedades(id_enfermedad) ON DELETE SET NULL,
    url_imagen TEXT NOT NULL,
    url_audio TEXT,
    resumen TEXT,
    porcentaje_coincidencia DECIMAL(5,2),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posibles_condiciones (
    id_posible_condicion SERIAL PRIMARY KEY,
    id_prediccion INT REFERENCES predicciones(id_prediccion) ON DELETE CASCADE,
    nombre_condicion VARCHAR(255) NOT NULL,
    nombre_interno VARCHAR(100),
    porcentaje DECIMAL(5,2) DEFAULT 0.00
);
