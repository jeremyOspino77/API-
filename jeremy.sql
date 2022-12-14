

/* SQLINES DEMO *** abase [GESTION_ORDENES]    Script Date: 11/08/2022 11:44:18 p. m. ******/
CREATE DATABASE GESTION_ORDENES;

USE `GESTION_ORDENES`;

/* SQLINES DEMO *** le [dbo].[ORD_MA_CLIENTES]    Script Date: 11/08/2022 11:44:18 p. m. ******/
/* SET ANSI_NULLS ON */

/* SET QUOTED_IDENTIFIER ON */

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE `ORD_MA_CLIENTES`(
	`id` int AUTO_INCREMENT NOT NULL,
	`uuid` varchar(50) NULL,
	`fecha` varchar(30) NULL,
	`nombre` Longtext NULL,
	`identificacion` varchar(30) NULL,
	`direccion` Longtext NULL,
	`telefono` varchar(30) NULL,
	`id_pais` int NULL,
	`email` varchar(250) NULL,
	`id_estado` int NULL,
	`id_digitador` int NULL,
 CONSTRAINT `PK_ORD_CLIENTES` PRIMARY KEY
(
	`id` ASC
)
);
/* SQLINES DEMO *** le [dbo].[ORD_MA_ESTADOS]    Script Date: 11/08/2022 11:44:18 p. m. ******/
/* SET ANSI_NULLS ON */

/* SET QUOTED_IDENTIFIER ON */

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE `ORD_MA_ESTADOS`(
	`id` int NOT NULL,
	`uuid` varchar(50) NULL,
	`fecha` varchar(30) NULL,
	`nombre` varchar(20) NULL,
	`id_estado` int NULL,
	`id_digitador` int NULL,
 CONSTRAINT `PK_ORD_MA_ESTADOS` PRIMARY KEY
(
	`id` ASC
)
);
/* SQLINES DEMO *** le [dbo].[ORD_MA_PAISES]    Script Date: 11/08/2022 11:44:18 p. m. ******/
/* SET ANSI_NULLS ON */

/* SET QUOTED_IDENTIFIER ON */

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE `ORD_MA_PAISES`(
	`id` int AUTO_INCREMENT NOT NULL,
	`uuid` varchar(50) NULL,
	`fecha` varchar(30) NULL,
	`nombre` varchar(250) NULL,
	`codigo` varchar(5) NULL,
	`id_estado` int NULL,
	`id_digitador` int NULL,
 CONSTRAINT `PK_ORD_PAISES` PRIMARY KEY
(
	`id` ASC
)
);
/* SQLINES DEMO *** le [dbo].[ORD_MA_USUARIOS]    Script Date: 11/08/2022 11:44:18 p. m. ******/
/* SET ANSI_NULLS ON */

/* SET QUOTED_IDENTIFIER ON */

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE `ORD_MA_USUARIOS`(
	`id` int NOT NULL,
	`uuid` varchar(30) NULL,
	`fecha` varchar(30) NULL,
	`nombre` varchar(20) NULL,
	`usuario` varchar(250) NULL,
	`password` Longtext NULL,
	`id_estado` int NULL,
	`id_digitador` int NULL,
 CONSTRAINT `PK_ORD_MA_USUARIOS` PRIMARY KEY
(
	`id` ASC
)
);
/* SQLINES DEMO *** le [dbo].[ORD_MV_DETALLES]    Script Date: 11/08/2022 11:44:18 p. m. ******/
/* SET ANSI_NULLS ON */

/* SET QUOTED_IDENTIFIER ON */

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE `ORD_MV_DETALLES`(
	`id` int NOT NULL,
	`id_orden` int NULL,
	`largo` varchar(20) NULL,
	`ancho` varchar(20) NULL,
	`id_estado` int NULL,
 CONSTRAINT `PK_ORD_MV_DETALLES` PRIMARY KEY
(
	`id` ASC
)
);
/* SQLINES DEMO *** le [dbo].[ORD_MV_ORDENES]    Script Date: 11/08/2022 11:44:18 p. m. ******/
/* SET ANSI_NULLS ON */

/* SET QUOTED_IDENTIFIER ON */

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE `ORD_MV_ORDENES`(
	`id` int AUTO_INCREMENT NOT NULL,
	`uuid` varchar(50) NULL,
	`fecha` varchar(30) NULL,
	`numero_orden` varchar(30) NULL,
	`id_cliente` int NULL,
	`id_estado` int NULL,
	`id_digitador` int NULL,
 CONSTRAINT `PK_ORD_MV_ORDENES` PRIMARY KEY
(
	`id` ASC
)
);
-- SQLINES LICENSE FOR EVALUATION USE ONLY
INSERT `ORD_MA_ESTADOS` (`id`, `uuid`, `fecha`, `nombre`, `id_estado`, `id_digitador`) VALUES (1, NULL, '2022-08-12 08:00:00', 'ANULADA', 1, 1);
-- SQLINES LICENSE FOR EVALUATION USE ONLY
INSERT `ORD_MA_ESTADOS` (`id`, `uuid`, `fecha`, `nombre`, `id_estado`, `id_digitador`) VALUES (2, NULL, '2022-08-12 08:00:00', 'APROBADA', 1, 1);
-- SQLINES LICENSE FOR EVALUATION USE ONLY
INSERT `ORD_MA_ESTADOS` (`id`, `uuid`, `fecha`, `nombre`, `id_estado`, `id_digitador`) VALUES (3, NULL, '2022-08-12 08:00:00', 'SOLICITADA', 1, 1);

-- SQLINES LICENSE FOR EVALUATION USE ONLY
INSERT `ORD_MA_USUARIOS` (`id`, `uuid`, `fecha`, `nombre`, `usuario`, `password`, `id_estado`, `id_digitador`) VALUES (1, NULL, '2022-08-12 08:00:00', 'USUARIO REGISTRA', 'USER1', '1', 1, 1);

ALTER TABLE `ORD_MA_CLIENTES`  ADD  CONSTRAINT `FK_ORD_MA_CLIENTES_ORD_MA_PAISES` FOREIGN KEY(`id_pais`)
REFERENCES `ORD_MA_PAISES` (`id`);


ALTER TABLE `ORD_MA_CLIENTES`  ADD  CONSTRAINT `FK_ORD_MA_CLIENTES_ORD_MA_USUARIOS` FOREIGN KEY(`id_digitador`)
REFERENCES `ORD_MA_USUARIOS` (`id`);


ALTER TABLE `ORD_MA_ESTADOS`  ADD  CONSTRAINT `FK_ORD_MA_ESTADOS_ORD_MA_USUARIOS` FOREIGN KEY(`id_digitador`)
REFERENCES `ORD_MA_USUARIOS` (`id`);


ALTER TABLE `ORD_MA_PAISES`  ADD  CONSTRAINT `FK_ORD_MA_PAISES_ORD_MA_USUARIOS` FOREIGN KEY(`id_digitador`)
REFERENCES `ORD_MA_USUARIOS` (`id`);


ALTER TABLE `ORD_MV_DETALLES`  ADD  CONSTRAINT `FK_ORD_MV_DETALLES_ORD_MV_ORDENES` FOREIGN KEY(`id_orden`)
REFERENCES `ORD_MV_ORDENES` (`id`);


ALTER TABLE `ORD_MV_ORDENES`  ADD  CONSTRAINT `FK_ORD_MV_ORDENES_ORD_MA_CLIENTES` FOREIGN KEY(`id_cliente`)
REFERENCES `ORD_MA_CLIENTES` (`id`);


ALTER TABLE `ORD_MV_ORDENES`  ADD  CONSTRAINT `FK_ORD_MV_ORDENES_ORD_MA_ESTADOS` FOREIGN KEY(`id_estado`)
REFERENCES `ORD_MA_ESTADOS` (`id`);


ALTER TABLE `ORD_MV_ORDENES`  ADD  CONSTRAINT `FK_ORD_MV_ORDENES_ORD_MA_USUARIOS` FOREIGN KEY(`id_digitador`)
REFERENCES `ORD_MA_USUARIOS` (`id`);



