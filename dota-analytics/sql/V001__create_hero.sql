-- Criação de tabela de HEROES

CREATE TABLE hero (

    id               INTEGER PRIMARY KEY,
    name             VARCHAR(255) NOT NULL,
    localized_name   VARCHAR(255) NOT NULL,
    primary_attr     VARCHAR(3),
    attack_type      VARCHAR(15),
    roles            TEXT[],
    legs             INTEGER
);