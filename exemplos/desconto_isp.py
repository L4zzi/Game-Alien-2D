# Interfaces específicas: cada classe implementa apenas o que faz sentido para ela
class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError


class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError


class IVIP:
    def validar_usuario_vip(self, usuario):
        raise NotImplementedError


class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1


class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor):
        return valor * 0.2

    def aplicar_cupom(self, codigo):
        return True

    def validar_usuario_vip(self, usuario):
        return usuario == "vip"


def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)


def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)


if __name__ == "__main__":
    valor = 100

    normal = DescontoNormal()
    vip = DescontoVIP()

    print("Desconto normal:", aplicar_desconto(normal, valor))
    print("Desconto VIP:", aplicar_desconto(vip, valor))

    print("Cupom VIP:", aplicar_cupom(vip, "DESC10"))
