from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        if caminho.endswith(".csv"):
            with open(caminho, encoding="utf8") as file:
                return list(csv.DictReader(file))
        else:
            raise ValueError("Arquivo inválido")
