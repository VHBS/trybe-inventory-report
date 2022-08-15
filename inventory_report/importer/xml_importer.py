from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        if caminho.endswith(".xml"):
            with open(caminho, encoding="utf8") as file:
                return xmltodict.parse(file.read())["dataset"][
                    "record"
                ]
        else:
            raise ValueError("Arquivo inválido")
