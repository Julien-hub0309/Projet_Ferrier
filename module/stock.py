from module.inventaire import Inventaire


class Stock:

    def __init__(self, fichier):

        self.inventaire = Inventaire(
            fichier
        )

    def ajouter_machine(self, machine):

        self.inventaire.ajouter_machine(
            machine
        )

    def supprimer_machine(self, identifiant):

        self.inventaire.supprimer_machine(
            identifiant
        )

    def rechercher_machine(self, mot_cle):

        resultat = []

        for machine in self.inventaire.machines:

            if (
                mot_cle.lower()
                in machine.get(
                    "nom",
                    ""
                ).lower()
            ):
                resultat.append(machine)

        return resultat

    def analyser_machine(self, identifiant):

        for machine in self.inventaire.machines:

            if machine["id"] == identifiant:
                return machine

        return None