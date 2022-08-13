import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(caminho, tipo_de_relatorio):
        with open(caminho, encoding="utf8") as file:
            if caminho.endswith(".csv"):
                lista_de_dicionarios = list(csv.DictReader(file))
            if caminho.endswith(".json"):
                lista_de_dicionarios = json.load(file)
            if caminho.endswith(".xml"):
                lista_de_dicionarios = xmltodict.parse(file.read())["dataset"][
                    "record"
                ]

        if tipo_de_relatorio == "simples":
            return SimpleReport.generate(lista_de_dicionarios)
        else:
            return CompleteReport.generate(lista_de_dicionarios)
