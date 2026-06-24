-- Cria tabela de items

CREATE TABLE item (
    
   id               INTEGER PRIMARY KEY,
   name             VARCHAR (255) NOT NULL,
   dname            VARCHAR (255) NOT NULL,
   qual             VARCHAR (255),
   cost             INTEGER,
   behavior         VARCHAR (100),
   mc               BOOLEAN,
   hc               BOOLEAN,
   cd               NUMERIC (10,2),
   created          BOOLEAN
);