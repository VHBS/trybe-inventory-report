from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
      1,
      "Borracha",
      "Papelaria Solar",
      "2021-07-04",
      "2029-02-09",
      "FR48",
      "Ao abrigo de luz solar"
    )
    assert produto.__repr__() == (
        "O produto Borracha"
        " fabricado em 2021-07-04"
        " por Papelaria Solar com validade"
        " até 2029-02-09"
        " precisa ser armazenado Ao abrigo de luz solar."
    )
