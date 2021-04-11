-- Criando tabela estados
create table estados(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL UNIQUE,
    sigla VARCHAR(2) NOT NULL UNIQUE,
    regiao ENUM('Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul') NOT NULL,
    populacao DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (id)

);

create table if not exists cidades(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    estado_id INT UNSIGNED NOT NULL,
    nome VARCHAR(255) NOT NULL,
    area DECIMAL(10,2),
    PRIMARY KEY (id),
    FOREIGN KEY (estado_id) REFERENCES estados (id)

);


create table if not exists prefeitos(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    cidade_id INT UNSIGNED NOT NULL UNIQUE,
    nome VARCHAR(255) NOT NULL,    
    PRIMARY KEY (id),
    FOREIGN KEY (cidade_id) REFERENCES cidades (id)

);