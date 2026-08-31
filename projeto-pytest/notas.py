def calcular_media(nota1, nota2, nota3):
    if not all(0 <= nota <= 10 for nota in [nota1, nota2, nota3]):
        raise ValueError("As notas devem estar entre 0 e 10.")

    return (nota1 + nota2 + nota3) / 3


def verificar_situacao(media):
    if media < 0 or media > 10:
        raise ValueError("A média deve estar entre 0 e 10.")

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
