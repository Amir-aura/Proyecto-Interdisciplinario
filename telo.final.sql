-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-11-2025 a las 17:01:21
-- Versión del servidor: 8.0.33
-- Versión de PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `telo`
--
DROP DATABASE IF EXISTS `telo`;
CREATE DATABASE IF NOT EXISTS `telo` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `telo`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE `clientes` (
  `ID` int NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `DNI` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `telefono` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ultima_reserva` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`ID`, `nombre`, `DNI`, `telefono`, `ultima_reserva`) VALUES
(1, 'Lola Machuca', '48213773', '11-3726-7328', '2025-04-11'),
(2, 'chechon López', '48321732', '11-1242-8913', '2035-06-29'),
(3, 'JUAN', '47846837', '1137926146', '2025-07-11');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitaciones`
--

DROP TABLE IF EXISTS `habitaciones`;
CREATE TABLE `habitaciones` (
  `ID` int NOT NULL,
  `tipo` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `precio` int DEFAULT NULL,
  `capacidad` int DEFAULT NULL,
  `estado` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `habitaciones`
--

INSERT INTO `habitaciones` (`ID`, `tipo`, `precio`, `capacidad`, `estado`) VALUES
(1, 'Simple', 67, 1, 'Disponible'),
(2, 'Doble', 54, 2, 'Disponible'),
(3, 'Suite', 170, 4, 'Mantenimiento'),
(4, 'Sencilla', 50, 1, 'Disponible'),
(5, 'Doble', 80, 2, 'Disponible'),
(6, 'Doble', 90, 2, 'Ocupada'),
(7, 'Suite', 150, 4, 'Ocupada'),
(8, 'Sencilla', 55, 1, 'Mantenimiento'),
(9, 'Familiar', 120, 5, 'Disponible'),
(11, 'juan', 100, 3, 'disponible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

DROP TABLE IF EXISTS `reservas`;
CREATE TABLE `reservas` (
  `ID` int NOT NULL,
  `ID_Habitacion` int DEFAULT NULL,
  `ID_Cliente` int DEFAULT NULL,
  `fecha_entrada` datetime DEFAULT NULL,
  `fecha_salida` datetime DEFAULT NULL,
  `ID_servicio` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reservas`
--

INSERT INTO `reservas` (`ID`, `ID_Habitacion`, `ID_Cliente`, `fecha_entrada`, `fecha_salida`, `ID_servicio`) VALUES
(1, NULL, NULL, '2025-08-20 03:00:00', '2025-08-25 00:00:00', 0),
(2, NULL, NULL, '2025-09-01 00:00:00', '2025-09-05 00:00:00', 0),
(3, 2, 1, '2025-06-11 00:00:00', '2025-07-11 00:00:00', 0),
(4, 4, 1, '2025-08-12 00:00:00', '2025-09-12 00:00:00', 2),
(5, 1, 1, '2009-12-12 00:00:00', '2010-12-12 00:00:00', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

DROP TABLE IF EXISTS `servicios`;
CREATE TABLE `servicios` (
  `ID` int NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `precio` int NOT NULL,
  `ID_Reserva` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `servicios`
--

INSERT INTO `servicios` (`ID`, `nombre`, `precio`, `ID_Reserva`) VALUES
(1, 'Desayuno buffet', 100, NULL),
(2, 'Spa', 250, NULL),
(3, 'Servicio de limpieza', 75, NULL),
(4, 'Pileta', 200, NULL),
(5, 'Estacionamiento', 100, NULL),
(6, 'Servicios tecnicos', 30, NULL),
(7, 'Desayuno a la cama', 150, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Habitacion` (`ID_Habitacion`),
  ADD KEY `ID_Cliente` (`ID_Cliente`),
  ADD KEY `ID_servicio` (`ID_servicio`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Reserva` (`ID_Reserva`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`ID_Habitacion`) REFERENCES `habitaciones` (`ID`),
  ADD CONSTRAINT `reservas_ibfk_2` FOREIGN KEY (`ID_Cliente`) REFERENCES `clientes` (`ID`);

--
-- Filtros para la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD CONSTRAINT `servicios_ibfk_1` FOREIGN KEY (`ID_Reserva`) REFERENCES `reservas` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
