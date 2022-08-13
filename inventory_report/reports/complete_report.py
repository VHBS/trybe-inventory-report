from datetime import date


class CompleteReport:
    @staticmethod
    def generate(lista_de_produtos):
        data_atual = date.today().strftime("%Y-%m-%d")

        fabricacao = min([p["data_de_fabricacao"] for p in lista_de_produtos])

        validade = min(
            [
                p["data_de_validade"]
                for p in lista_de_produtos
                if p["data_de_validade"] >= data_atual
            ]
        )

        empresas = {}

        for p in lista_de_produtos:
            if p["nome_da_empresa"] in empresas:
                empresas[p["nome_da_empresa"]] += 1
            else:
                empresas[p["nome_da_empresa"]] = 1

        empresa = max(empresas, key=empresas.get)

        empresas_return = "Produtos estocados por empresa:\n"
        for emp in empresas:
            empresas_return += f"- {emp}: {empresas[emp]}\n"
        return (
            f"Data de fabricação mais antiga: {fabricacao}\n"
            f"Data de validade mais próxima: {validade}\n"
            f"Empresa com mais produtos: {empresa}\n"
            f"{empresas_return}"
        )
