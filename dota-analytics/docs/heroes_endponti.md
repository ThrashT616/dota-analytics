# Endpoint heroes

## Endpoint

GET /heroes

## Obejetivo

Retornar à lista de heróis disponíveis no Dota 2.

## Campos Retornandos


    - id
    - name
    - localized_name
    - primary_attr
    - attack_type
    - roles
    - legs

## Observação de modelagem

O campo roles retorna uma lista de funções do heróis.

Exemplo:

Axe possui roles como Initiador, Durable, Disabler e Carry.

Para o MVP, o campo roles pode ser salvo como array ou texto. Futuramente pode ser normalizado em tabelas Role e HeroRole.