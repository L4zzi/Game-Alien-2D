from abc import ABC, abstractmethod


# Classe abstrata que define o contrato para todos os tipos de desconto
class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass


# Implementação para cliente normal
class DescontoNormal(Desconto):
    def calcular(self, valor):
        return valor * 0.1


# Implementação para cliente VIP
class DescontoVIP(Desconto):
    def calcular(self, valor):
        return valor * 0.2


# Implementação para cliente Premium
class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.3


def main():
    valor = 100

    normal = DescontoNormal()
    vip = DescontoVIP()
    premium = DescontoPremium()

    print(f"Desconto Normal: R$ {normal.calcular(valor):.2f}")
    print(f"Desconto VIP: R$ {vip.calcular(valor):.2f}")
    print(f"Desconto Premium: R$ {premium.calcular(valor):.2f}")


if __name__ == "__main__":
    main()
