# Sistema de Cálculo de Notas

## Objetivo

Este projeto foi desenvolvido para demonstrar a utilização de testes automatizados com Python, Pytest e GitHub Actions.

## Funções implementadas

O projeto possui duas funções principais:

- `calcular_media()`: calcula a média de três notas.
- `verificar_situacao()`: verifica se o aluno foi aprovado, ficou de recuperação ou foi reprovado.

As funções possuem tratamento de valores inválidos por meio de exceções.

## Testes

Foram desenvolvidos 9 testes automatizados utilizando Pytest.

Os testes verificam:

- Cálculo de média;
- Notas zero;
- Notas máximas;
- Aprovação;
- Recuperação;
- Reprovação;
- Notas negativas;
- Notas acima de 10;
- Médias inválidas.

Também foi utilizado `pytest.raises` para verificar o tratamento de exceções.

## Como executar os testes

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
pytest tests
```

## GitHub Actions

O projeto possui um workflow configurado para executar automaticamente os testes sempre que um `push` for realizado no repositório.

Se todos os testes forem aprovados, a execução será concluída com sucesso. Caso algum teste falhe, o GitHub Actions informará a falha e a execução será marcada como não aprovada.

## Resultado

Após enviar o projeto ao GitHub, os testes devem ser executados automaticamente na aba Actions.
