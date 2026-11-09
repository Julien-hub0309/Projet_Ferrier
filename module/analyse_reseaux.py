from scapy.all import ARP, Ether, srp
import socket


class AnalyseReseau:

    def __init__(self, ip_range):
        self.ip_range = ip_range

    def scan_reseau(self):

        arp = ARP(pdst=self.ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")

        packet = ether / arp

        result = srp(
            packet,
            timeout=2,
            verbose=False
        )[0]

        machines = []

        for _, received in result:
            machines.append({
                "ip": received.psrc,
                "mac": received.hwsrc
            })

        return machines

    def analyser_machines(self):

        resultat = []

        for machine in self.scan_reseau():

            try:
                nom = socket.gethostbyaddr(
                    machine["ip"]
                )[0]
            except Exception:
                nom = None

            resultat.append({
                "ip": machine["ip"],
                "name": nom,
                "mac": machine["mac"],
                "type": "ordinateur"
            })

        return resultat

    def run(self):
        return self.analyser_machines()


if __name__ == "__main__":

    analyse_reseau = AnalyseReseau(
        "192.168.1.0/24"
    )

    print(analyse_reseau.run())
