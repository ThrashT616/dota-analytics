## Quais entidades você acha que existirão no banco?
    - Match
    - Player
    - Hero
    - PlayerMatch
    - Item
    - Ability
    - Patch
    - Status
    - League
    - Team
    - ProPlayer
    - Rankings
    - PlayerMatchItem
    - HeroAbility
    - GameMode
## Como elas se relacionam?

    Um Hero pode aparecar em milhares de partidas simultâneas.

    Um Match possuí 10 Players.

    Cada player escolhe apenas um Hero naquela Match.

    Um Hero não pode ser pego por mais de 2 Players e caso ambos forem escolhido durante a mesma fase de escolha o Hero é banido e não pode ser jogado nessa partida.

    Um Hero possuí várias habilidades.

    Um Patch pode alterar atributos de Heroes, Items e Abilities. Para o MVP, Patch será usado principalmente para segmentar análises por versão do jogo.

    Um Player, dentro de uma Match, joga com um Hero e pode possuir itens em slots de inventário, mochila e neutral item. Esses itens pertencem à participação do Player naquela Match, não diretamente ao Hero.

    Ranking é calculado de acordo com seu MMR.


## MVP Inicial

    O primeiro MVP do projeto irá focar em:

    - Consultar heroes da API OpenDota
    - Persistir heroes no PostgreSQL
    - Consultar itens da API OpenDota
    - Persistir itens no PostgreSQL
    - Consultar uma partida específica
    - Persistir Match e PlayerMatch
    - Criar análises SQL simples


## Tabela Hero


### Origem 

    GET /heroes

### Descrição

Armazenar informações básicas dos heróis disponíveis no Dota 2.

### Estrutura proposta
    - id INTEGER PRIMARY KEY
    - name VARCHAR(255)
    - localized_name VARCHAR(255)
    - primary_attr VARCHAR(3)
    - attack_type VARCHAR (15)
    - roles TEXT[]
    - legs INTEGER


### Observações

    - O campo roles é retornado pela API como uma lista.
    - Para op MVP será armazedo como TEXT[] no PostgreSQL.
    - Futuramente poderá ser normalizado em tabelas role e hero_role


## Tabela Item

### Origem

    GET /constants/items


### Descrição

Retorna um dicionário onde a chave representa o nome interno do item.

### Estrutura proposta 
    - id INTEGER PRIMARY KEY
    - name VARCHAR (255)
    - dname VARCHAR (255) NOT NULL
    - qual VARCHAR (255)
    - cost INTEGER
    - behavior VARCHAR (100)
    - mc BOOLEAN
    - hc BOOLEAN
    - cd NUMERIC (10,2)
    - created BOOLEAN

## Observações

    - O campo name não vem como campo dentro do item, ele vem da chave do dicionário.
    - 