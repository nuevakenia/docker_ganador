
CREATE TABLE sucursal (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE colaborador (
    id SERIAL PRIMARY KEY,
    personnum VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    sucursal_id INT NOT NULL,
    FOREIGN KEY (sucursal_id) REFERENCES sucursal(id)
);

CREATE TABLE marca (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    colaborador_id INT NOT NULL,
    FOREIGN KEY (colaborador_id) REFERENCES colaborador(id)
);

CREATE TABLE reporte (
    id SERIAL PRIMARY KEY,
    archivo JSON NOT NULL,
    estado VARCHAR(50) NOT NULL,
    sucursal_id INT NOT NULL,
    FOREIGN KEY (sucursal_id) REFERENCES sucursal(id)
);


INSERT INTO sucursal (nombre) VALUES ('Talagante');
INSERT INTO sucursal (nombre) VALUES ('Maipo');
INSERT INTO sucursal (nombre) VALUES ('Buin');

-- Sucursal Talagante
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('12345678-9', 'Juan Perez', 1);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('23456789-0', 'Maria Rodriguez', 1);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('34567890-1', 'Carlos González', 1);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('45678901-2', 'Fernanda Muñoz', 1);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('56789012-3', 'Roberto Valenzuela', 1);

-- Sucursal Maipo
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('67890123-4', 'Catalina Herrera', 2);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('78901234-5', 'Francisco Jara', 2);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('89012345-6', 'Sofia Vargas', 2);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('90123456-7', 'Miguel Araya', 2);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('01234567-8', 'Valentina Nuñez', 2);

-- Sucursal Buin
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('12345678-0', 'Javier Espinoza', 3);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('23456789-1', 'Daniela Soto', 3);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('34567890-2', 'Sebastian Ortiz', 3);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('45678901-3', 'Camila Pizarro', 3);
INSERT INTO colaborador (personnum, nombre, sucursal_id) VALUES ('56789012-4', 'Nicolas Riquelme', 3);


-- Colaboradores sucursal 1

-- Colaborador ID 1
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 1), ('2023-03-27 17:00', 1);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 1), ('2023-03-28 17:00', 1);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 1), ('2023-03-29 17:00', 1);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 1), ('2023-03-30 17:00', 1);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 1), ('2023-03-31 17:00', 1);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 1), ('2023-04-01 17:00', 1);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 1), ('2023-04-02 17:00', 1);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 1), ('2023-04-03 17:00', 1);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 1), ('2023-04-04 17:00', 1);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 1), ('2023-04-05 17:00', 1);
-- Colaborador ID 2
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 2), ('2023-03-27 17:00', 2);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 2), ('2023-03-28 17:00', 2);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 2), ('2023-03-29 17:00', 2);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 2), ('2023-03-30 17:00', 2);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 2), ('2023-03-31 17:00', 2);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 2), ('2023-04-01 17:00', 2);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 2), ('2023-04-02 17:00', 2);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 2), ('2023-04-03 17:00', 2);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 2), ('2023-04-04 17:00', 2);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 2), ('2023-04-05 17:00', 2);

-- Colaborador ID 3
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 14:00', 3), ('2023-03-27 22:00', 3);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 14:00', 3), ('2023-03-28 22:00', 3);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 14:00', 3), ('2023-03-29 22:00', 3);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 14:00', 3), ('2023-03-30 22:00', 3);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 14:00', 3), ('2023-03-31 22:00', 3);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 14:00', 3), ('2023-04-01 22:00', 3);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 14:00', 3), ('2023-04-02 22:00', 3);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 14:00', 3), ('2023-04-03 22:00', 3);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 14:00', 3), ('2023-04-04 22:00', 3);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 14:00', 3), ('2023-04-05 22:00', 3);

-- Colaborador ID 4
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 14:00', 4), ('2023-03-27 22:00', 4);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 14:00', 4), ('2023-03-28 22:00', 4);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 14:00', 4), ('2023-03-29 22:00', 4);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 14:00', 4), ('2023-03-30 22:00', 4);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 14:00', 4), ('2023-03-31 22:00', 4);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 14:00', 4), ('2023-04-01 22:00', 4);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 14:00', 4), ('2023-04-02 22:00', 4);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 14:00', 4), ('2023-04-03 22:00', 4);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 14:00', 4), ('2023-04-04 22:00', 4);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 14:00', 4), ('2023-04-05 22:00', 4);

-- Colaborador ID 5
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 5), ('2023-03-27 17:00', 5);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 5), ('2023-03-28 17:00', 5);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 5), ('2023-03-29 17:00', 5);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 5), ('2023-03-30 17:00', 5);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 5), ('2023-03-31 17:00', 5);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 5), ('2023-04-01 17:00', 5);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 5), ('2023-04-02 17:00', 5);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 5), ('2023-04-03 17:00', 5);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 5), ('2023-04-04 17:00', 5);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 5), ('2023-04-05 17:00', 5);

-- Colaboradores ID 6

-- Colaborador ID 5
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 6), ('2023-03-27 17:00', 6);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 6), ('2023-03-28 17:00', 6);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 6), ('2023-03-29 17:00', 6);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 6), ('2023-03-30 17:00', 6);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 6), ('2023-03-31 17:00', 6);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 6), ('2023-04-01 17:00', 6);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 6), ('2023-04-02 17:00', 6);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 6), ('2023-04-03 17:00', 6);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 6), ('2023-04-04 17:00', 6);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 6), ('2023-04-05 17:00', 6);
-- Colaborador ID 7
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 7), ('2023-03-27 17:00', 7);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 7), ('2023-03-28 17:00', 7);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 7), ('2023-03-29 17:00', 7);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 7), ('2023-03-30 17:00', 7);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 7), ('2023-03-31 17:00', 7);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 7), ('2023-04-01 17:00', 7);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 7), ('2023-04-02 17:00', 7);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 7), ('2023-04-03 17:00', 7);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 7), ('2023-04-04 17:00', 7);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 7), ('2023-04-05 17:00', 7);

-- Colaborador ID 8
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 8), ('2023-03-27 17:00', 8);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 8), ('2023-03-28 17:00', 8);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 8), ('2023-03-29 17:00', 8);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 8), ('2023-03-30 17:00', 8);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 8), ('2023-03-31 17:00', 8);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 8), ('2023-04-01 17:00', 8);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 8), ('2023-04-02 17:00', 8);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 8), ('2023-04-03 17:00', 8);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 8), ('2023-04-04 17:00', 8);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 8), ('2023-04-05 17:00', 8);

-- Colaborador ID 9
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 9), ('2023-03-27 17:00', 9);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 9), ('2023-03-28 17:00', 9);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 9), ('2023-03-29 17:00', 9);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 9), ('2023-03-30 17:00', 9);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 9), ('2023-03-31 17:00', 9);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 9), ('2023-04-01 17:00', 9);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 9), ('2023-04-02 17:00', 9);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 9), ('2023-04-03 17:00', 9);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 9), ('2023-04-04 17:00', 9);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 9), ('2023-04-05 17:00', 9);

-- Colaborador ID 10
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 10), ('2023-03-27 17:00', 10);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 10), ('2023-03-28 17:00', 10);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 10), ('2023-03-29 17:00', 10);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 10), ('2023-03-30 17:00', 10);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 10), ('2023-03-31 17:00', 10);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 10), ('2023-04-01 17:00', 10);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 10), ('2023-04-02 17:00', 10);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 10), ('2023-04-03 17:00', 10);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 10), ('2023-04-04 17:00', 10);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 10), ('2023-04-05 17:00', 10);

-- Colaborador ID 11
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 11), ('2023-03-27 17:00', 11);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 11), ('2023-03-28 17:00', 11);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 11), ('2023-03-29 17:00', 11);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 11), ('2023-03-30 17:00', 11);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 11), ('2023-03-31 17:00', 11);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 11), ('2023-04-01 17:00', 11);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 11), ('2023-04-02 17:00', 11);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 11), ('2023-04-03 17:00', 11);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 11), ('2023-04-04 17:00', 11);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 11), ('2023-04-05 17:00', 11);

-- Colaborador ID 12
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 12), ('2023-03-27 17:00', 12);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 12), ('2023-03-28 17:00', 12);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 12), ('2023-03-29 17:00', 12);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 12), ('2023-03-30 17:00', 12);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 12), ('2023-03-31 17:00', 12);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 12), ('2023-04-01 17:00', 12);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 12), ('2023-04-02 17:00', 12);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 12), ('2023-04-03 17:00', 12);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 12), ('2023-04-04 17:00', 12);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 12), ('2023-04-05 17:00', 12);

-- Colaborador ID 13
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 13), ('2023-03-27 17:00', 13);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 13), ('2023-03-28 17:00', 13);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 13), ('2023-03-29 17:00', 13);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 13), ('2023-03-30 17:00', 13);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 13), ('2023-03-31 17:00', 13);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 13), ('2023-04-01 17:00', 13);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 13), ('2023-04-02 17:00', 13);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 13), ('2023-04-03 17:00', 13);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 13), ('2023-04-04 17:00', 13);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 13), ('2023-04-05 17:00', 13);

-- Colaborador ID 14
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 14), ('2023-03-27 17:00', 14);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 14), ('2023-03-28 17:00', 14);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 14), ('2023-03-29 17:00', 14);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 14), ('2023-03-30 17:00', 14);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 14), ('2023-03-31 17:00', 14);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 14), ('2023-04-01 17:00', 14);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 14), ('2023-04-02 17:00', 14);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 14), ('2023-04-03 17:00', 14);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 14), ('2023-04-04 17:00', 14);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 14), ('2023-04-05 17:00', 14);

-- Colaborador ID 15
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-27 08:00', 15), ('2023-03-27 17:00', 15);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-28 08:00', 15), ('2023-03-28 17:00', 15);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-29 08:00', 15), ('2023-03-29 17:00', 15);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-30 08:00', 15), ('2023-03-30 17:00', 15);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-03-31 08:00', 15), ('2023-03-31 17:00', 15);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-01 08:00', 15), ('2023-04-01 17:00', 15);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-02 08:00', 15), ('2023-04-02 17:00', 15);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-03 08:00', 15), ('2023-04-03 17:00', 15);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-04 08:00', 15), ('2023-04-04 17:00', 15);
INSERT INTO marca (timestamp, colaborador_id) VALUES ('2023-04-05 08:00', 15), ('2023-04-05 17:00', 15);
