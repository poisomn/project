CREATE DATABASE gmexpress;
USE gmexpress;

-- Tabla de clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(100) UNIQUE
);

-- Tabla de choferes
CREATE TABLE choferes (
    id_chofer INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    licencia VARCHAR(50)
);

-- Tabla de vehículos
CREATE TABLE vehiculos (
    id_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
    patente VARCHAR(20) UNIQUE NOT NULL,
    modelo VARCHAR(100),
    capacidad INT
);

-- Tabla de pedidos
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    descripcion TEXT NOT NULL,
    direccion_entrega VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('pendiente','en_camino','entregado') DEFAULT 'pendiente',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Tabla de asignaciones
CREATE TABLE asignaciones (
    id_asignacion INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    id_chofer INT,
    id_vehiculo INT,
    fecha_asignacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('pendiente','en_camino','entregado') DEFAULT 'pendiente',
    evidencia VARCHAR(255),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_chofer) REFERENCES choferes(id_chofer),
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo)
);
