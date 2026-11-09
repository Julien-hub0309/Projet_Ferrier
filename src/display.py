import tkinter as tk
from tkinter import ttk


class ApplicationGUI:

    def __init__(self, controller):

        self.controller = controller

        self.root = tk.Tk()

        self.root.title("Ferrier Inventory Suite")
        self.root.geometry("1400x900")
        self.root.minsize(1200, 700)

        # Couleurs
        self.bg_main = "#23002e"
        self.bg_panel = "#331345"
        self.bg_card = "#401756"

        self.red = "#d51818"
        self.gold = "#FFD700"

        self.text = "#E0E0E0"

        self.root.configure(
            bg=self.bg_main
        )

        self._style()
        self._build()

    def _style(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Ferrier.TButton",
            background=self.red,
            foreground="white",
            padding=10,
            borderwidth=0,
            font=("Segoe UI", 10, "bold")
        )

        style.map(
            "Ferrier.TButton",
            background=[
                ("active", "#ff3838")
            ]
        )

    def _build(self):

        self.header = tk.Frame(
            self.root,
            bg="#6614b8",
            height=120
        )

        self.header.pack(
            fill="x"
        )

        tk.Label(
            self.header,
            text="FERRIER INVENTORY SUITE",
            bg="#6614b8",
            fg="white",
            font=("Segoe UI", 28, "bold")
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            self.header,
            text="Gestion de parc • Inventaire • Analyse réseau",
            bg="#6614b8",
            fg="white",
            font=("Segoe UI", 11)
        ).pack()

        # MAIN
        main = tk.Frame(
            self.root,
            bg=self.bg_main
        )

        main.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # LEFT
        left = tk.Frame(
            main,
            bg=self.bg_panel,
            width=350
        )

        left.pack(
            side="left",
            fill="y"
        )

        # RIGHT
        right = tk.Frame(
            main,
            bg=self.bg_panel
        )

        right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(20, 0)
        )

        # OUTILS
        tk.Label(
            left,
            text="OUTILS",
            bg=self.bg_panel,
            fg=self.gold,
            font=("Segoe UI", 16, "bold")
        ).pack(
            pady=20
        )

        ttk.Button(
            left,
            text="Scanner le réseau",
            style="Ferrier.TButton",
            command=self.controller.scanner_reseau
        ).pack(
            fill="x",
            padx=15,
            pady=10
        )

        ttk.Button(
            left,
            text="Afficher l'inventaire",
            style="Ferrier.TButton",
            command=self.controller.afficher_inventaire
        ).pack(
            fill="x",
            padx=15,
            pady=10
        )

        ttk.Button(
            left,
            text="Analyser machine #1",
            style="Ferrier.TButton",
            command=lambda:
                self.controller.analyser_machine(1)
        ).pack(
            fill="x",
            padx=15,
            pady=10
        )

        # STATS
        stat_frame = tk.Frame(
            left,
            bg=self.bg_card
        )

        stat_frame.pack(
            fill="x",
            padx=15,
            pady=30
        )

        self.machine_count = tk.Label(
            stat_frame,
            text="Machines : 0",
            bg=self.bg_card,
            fg="white",
            font=("Segoe UI", 12, "bold")
        )

        self.machine_count.pack(
            pady=20
        )

        # JOURNAL
        tk.Label(
            right,
            text="JOURNAL D'ACTIVITE",
            bg=self.bg_panel,
            fg=self.gold,
            font=("Segoe UI", 18, "bold")
        ).pack(
            pady=15
        )

        self.log_text = tk.Text(
            right,
            bg="#1e1e1e",
            fg="#d7d7d7",
            insertbackground="white",
            relief="flat",
            font=("Consolas", 11)
        )

        self.log_text.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.log_text.insert(
            "end",
            "Ferrier Inventory Suite démarré.\n"
        )

        footer = tk.Frame(
            self.root,
            bg="#6614b8",
            height=40
        )

        footer.pack(
            fill="x"
        )

        tk.Label(
            footer,
            text="© Ferrier Inventory Suite",
            bg="#6614b8",
            fg="white"
        ).pack(
            pady=10
        )

    def ajouter_log(self, texte):

        self.log_text.insert(
            "end",
            f"{texte}\n"
        )

        self.log_text.see("end")

        try:

            total = len(
                self.controller.inventaire.machines
            )

            self.machine_count.config(
                text=f"Machines : {total}"
            )

        except Exception:
            pass

    def run(self):

        self.root.mainloop()