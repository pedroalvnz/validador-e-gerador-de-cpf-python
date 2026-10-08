# Validador e Gerador de CPF em Python

Dois scripts simples em Python para trabalhar com CPF: um **valida** números de CPF e o outro **gera** CPFs matematicamente válidos. Projeto educacional, feito para praticar lógica de programação.

## Conteúdo do repositório

| Arquivo | O que faz |
|---|---|
| `validador_cpf.py` | Verifica se um CPF é válido |
| `gerador_cpf.py` | Gera CPFs matematicamente válidos |

## Validador de CPF

- Aceita o CPF com ou sem pontuação (`123.456.789-09` ou `12345678909`)
- Remove os caracteres que não são números
- Confere se o CPF tem 11 dígitos
- Rejeita CPFs com todos os dígitos iguais (ex.: `111.111.111-11`)
- Calcula o primeiro e o segundo dígito verificador e compara com os informados

## Gerador de CPF

- Sorteia os 9 primeiros dígitos aleatoriamente
- Calcula o primeiro e o segundo dígito verificador
- Retorna o CPF completo, com ou sem formatação (`123.456.789-09`)

## Como usar

1. Tenha o Python 3 instalado
2. Baixe os arquivos deste repositório
3. Execute no terminal o script que quiser:

```
python validador_cpf.py
python gerador_cpf.py
```

## Como funciona o cálculo dos dígitos verificadores

Cada um dos dois dígitos verificadores é calculado multiplicando os dígitos anteriores por pesos decrescentes, somando tudo e usando o resto da divisão por 11 para chegar ao dígito. O gerador usa esse cálculo para criar o CPF, e o validador usa o mesmo cálculo para conferir se o CPF informado está correto.

## Avisos importantes

- Este projeto tem **fins educacionais e de teste**.
- O validador só verifica se o CPF é matematicamente válido. Ele **não confirma** se o CPF existe ou pertence a alguém na Receita Federal.
- Os CPFs gerados são apenas válidos pela matemática e podem coincidir com CPFs reais por acaso.
- **Não use para fraudes, cadastros falsos ou qualquer atividade ilegal.**

## Autor

Pedro Lucas Castro Alvernaz
