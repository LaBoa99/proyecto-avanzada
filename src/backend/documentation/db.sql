# CREATE DATABASE `siau` /*!40100 COLLATE 'latin1_swedish_ci' */
USE siau;

CREATE TABLE profesores (
  id int not null primary key AUTO_INCREMENT,
  nombre varchar(255) not null
);

CREATE TABLE carreras (
    id int not null primary key AUTO_INCREMENT,
    descripcion varchar(255),
    coordinador_id int unique,
   
    constraint fk_coordinador
      foreign key (coordinador_id)
      references profesores(id) on delete set null
);

CREATE TABLE centros_universitarios(
  id int not null primary key AUTO_INCREMENT,
  nombre varchar(255) not null unique,
  ubicacion varchar(255) not null,
  descripcion varchar(255),
  rector_id int unique,
 
  constraint fk_rector
    foreign key (rector_id)
    references profesores(id) on delete set null
);

CREATE TABLE horarios(
    id int not null primary key AUTO_INCREMENT,
    horario_inicio TIME not null,
    horario_fin TIME not null,
    dia_semana tinyint(1) unsigned,
   
    constraint check_dia
      check(dia_semana > 0 and dia_semana < 8),
    constraint check_horario
      check(horario_fin < horario_fin)
);

CREATE TABLE materias(
  id int not null primary key AUTO_INCREMENT,
  nrc varchar(7) unique not null,
  nombre varchar(255) unique not null,
  creditos  tinyint(2) unsigned not null,
  cupo_disponible tinyint unsigned not null,
  cupo  tinyint unsigned not null,
  horario_id int,
  profesor_id int,
 
  constraint fk_profesor
    foreign key (profesor_id) references profesores(id) on delete set null,
  constraint fk_horario
    foreign key (horario_id) references horarios(id) on delete set null,
 
  constraint check_cupo
    check(cupo <= cupo_disponible)
);

CREATE TABLE aulas(
  id int not null primary key AUTO_INCREMENT,
  aula varchar(3) unique not null
);

CREATE TABLE periodos(
    id int not null primary key AUTO_INCREMENT,
    year YEAR unique not null,
    periodo CHAR(1) NOT NULL,
   
    constraint check_periodo
    check(periodo in ('A', 'B', 'C', 'D'))
);

CREATE TABLE horario_materias(
  id int not null primary key AUTO_INCREMENT,
  materia_id int not null,
  horario_id int not null,
  aula_id int not null,
 
  constraint unique_horario_materias
    unique(materia_id, horario_id, aula_id),
 
  constraint fk_materia
    foreign key (materia_id) references materias(id) on delete cascade,
  constraint fk_horario_materia
    foreign key (horario_id) references horarios(id) on delete cascade,
  constraint fk_aula
    foreign key (aula_id) references aulas(id) on delete cascade
);

CREATE TABLE alumnos(
    id int not null primary key AUTO_INCREMENT,
    codigo varchar(9) NOT NULL unique,
    situacion tinyint(1) check(situacion in (0, 1)),
    periodo_ingreso_id int,
    carrera_id int,
    centro_id int not null,
   
    constraint fk_periodo_ingreso
    foreign key (periodo_ingreso_id) references periodos(id) on delete set null,
   
    constraint fk_centro
    foreign key (centro_id) references centros_universitarios(id) on delete cascade,
   
    constraint fk_carrera_alumno
    foreign key (carrera_id) references carreras(id) on delete set null
   
);

CREATE TABLE alumnos_materias(
    id int not null primary key AUTO_INCREMENT,
    alumno_id int not null,
    materia_id int not null,
    periodo_id int not null,
    calificacion  decimal(5, 2) unsigned default 0,
    intento  tinyint(1) unsigned default 1,
   
    constraint fk_alumno_materia
    foreign key(alumno_id) references alumnos(id) on delete cascade,
   
    constraint fk_materia_materia
    foreign key (materia_id) references materias(id) on delete cascade,
   
    constraint fk_periodo_materias
    foreign key (periodo_id) references periodos(id) on delete cascade
);

DELIMITER $$
	CREATE TRIGGER uppercase_periodo BEFORE INSERT ON periodos
	FOR EACH ROW
	BEGIN
		SET NEW.periodo = UPPER(NEW.periodo);
	END$$
	
	CREATE TRIGGER uppecase_periodo_update BEFORE UPDATE ON periodos
	FOR EACH ROW
	BEGIN
		SET NEW.periodo = UPPER(NEW.periodo);
	END$$
DELIMITER ;