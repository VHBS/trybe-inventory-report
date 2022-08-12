from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
      1,
      "Borracha",
      "Papelaria Solar",
      "2021-07-04",
      "2029-02-09",
      "FR48",
      "Ao abrigo de luz solar"
    )
    assert produto.id == 1
    assert produto.nome_do_produto == "Borracha"
    assert produto.nome_da_empresa == "Papelaria Solar"
    assert produto.data_de_fabricacao == "2021-07-04"
    assert produto.data_de_validade == "2029-02-09"
    assert produto.numero_de_serie == "FR48"
    assert produto.instrucoes_de_armazenamento == "Ao abrigo de luz solar"
