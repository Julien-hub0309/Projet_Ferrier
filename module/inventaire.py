import json
from tabulate import tabulate


class Inventaire:

    def __init__(self, fichier):

        self.fichier = fichier
        self.machines = self.charger()

    def charger(self):

        try:
            with open(
                self.fichier,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):
            return []

    def enregistrer(self):

        with open(
            self.fichier,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.machines,
                f,
                indent=4,
                ensure_ascii=False
            )

    def afficher_inventaire(self):

        headers = [
            "ID",
            "Nom",
            "Type",
            "Marque",
            "Modele",
            "Serie",
            "Localisation",
            "Etat"
        ]

        donnees = []

        for machine in self.machines:

            donnees.append([
                machine.get("id"),
                machine.get("nom"),
                machine.get("type"),
                machine.get("marque"),
                machine.get("modele"),
                machine.get("numero_de_serie"),
                machine.get("localisation"),
                machine.get("etat")
            ])

        print(tabulate(
            donnees,
            headers=headers,
            tablefmt="grid"
        ))

    def ajouter_machine(self, machine):

        self.machines.append(machine)
        self.enregistrer()

    def supprimer_machine(self, identifiant):

        self.machines = [
            m for m in self.machines
            if m["id"] != identifiant
        ]

        self.enregistrer()