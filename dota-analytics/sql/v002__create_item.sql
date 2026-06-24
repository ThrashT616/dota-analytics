CREATE TABLE item (
    
   id               INTEGER PRIMARY KEY,
   name             VARCHAR (255) NOT NULL,
   dname            VARCHAR (255),
   qual             VARCHAR (50),
   cost             INTEGER,
   behavior         VARCHAR (100),
   mc               BOOLEAN,
   hc               BOOLEAN,
   cd               NUMERIC (10,2),
   created          BOOLEAN
);