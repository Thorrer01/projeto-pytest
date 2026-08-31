import pytest

from notas import calcular_media, verificar_situacao


def test_calcular_media():
    assert calcular_media(8, 7, 9) == 8


def test_calcular_media_com_notas_zero():
    assert calcular_media(0, 0, 0) == 0


def test_calcular_media_com_notas_maximas():
    assert calcular_media(10, 10, 10) == 10


def test_aluno_aprovado():
    assert verificar_situacao(8) == "Aprovado"


def test_aluno_recuperacao():
    assert verificar_situacao(6) == "Recuperação"


def test_aluno_reprovado():
    assert verificar_situacao(4) == "Reprovado"


def test_nota_negativa():
    with pytest.raises(ValueError):
        calcular_media(-1, 8, 7)


def test_nota_maior_que_dez():
    with pytest.raises(ValueError):
        calcular_media(11, 8, 7)


def test_media_invalida():
    with pytest.raises(ValueError):
        verificar_situacao(11)
