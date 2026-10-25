from abc import ABC, abstractmethod


# Classe base: qualquer filha deve poder substituí-la sem quebrar o programa
class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass


class DescontoNormal(Desconto):
    def calcular(self, valor):
        return valor * 0.1


class DescontoVIP(Desconto):
    def calcular(self, valor):
        return valor * 0.2


class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.3


def aplicar_desconto(desconto: Desconto, valor: float) -> float:
    return desconto.calcular(valor)


if __name__ == "__main__":
    valor = 100

    print("Normal:", aplicar_desconto(DescontoNormal(), valor))
    print("VIP:", aplicar_desconto(DescontoVIP(), valor))
    print("Premium:", aplicar_desconto(DescontoPremium(), valor))
