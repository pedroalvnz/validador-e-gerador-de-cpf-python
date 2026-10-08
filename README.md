# Validador de CPF em Python

Script simples em Python que verifica se um CPF é válido, usando o cálculo
oficial dos dígitos verificadores.

## O que ele faz

- Aceita o CPF com ou sem pontuação (`123.456.789-09` ou `12345678909`)
- Remove os caracteres que não são números
- Confere se o CPF tem 11 dígitos
- Rejeita CPFs com todos os dígitos iguais (ex.: `111.111.111-11`)
- Calcula o primeiro e o segundo dígito verificador e compara com os informados

## Como usar

1. Tenha o Python 3 instalado
2. Baixe o arquivo `validador_cpf.py`
3. Execute no terminal:

    python validador_cpf.py

4. Digite o CPF quando o programa pedir

## Como funciona o cálculo

Cada um dos dois dígitos verificadores é calculado multiplicando os dígitos
anteriores por pesos decrescentes, somando tudo e usando o resto da divisão
por 11 para chegar ao dígito.

## Aviso

Este projeto tem fins educacionais. Ele só verifica se o CPF é matematicamente
válido, não confirma se ele existe ou pertence a alguém na Receita Federal.
