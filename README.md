pip install scapy
from scapy.all import ARP, Ether, srp
import ipaddress

def scan_network(network): #Cria um pacote ARP para descobrir dispositivos na rede
    arp = ARP(pdst=network)
    Ether = Ether(dst = "ff:ff:ff:ff:ff:ff")
    packet = Ether/arp
    
    #envia o pacote e recebe as respostas
    result = srp(packet, timeout=3, verbose=0)[0]
    
    #Lista para armazenar os dispositivos encontrados
    devices = []
    
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac':received.hwsrc})
        
        return devices
def main():
     #Defina sua rede aqui(por exemplo: '192.168.1.0/24')
     network = input("Digite o endereço da sua rede (EX: 192.169.1.0/24): ")
     
     #Verifica se o endereço da rede é válido
     try:
         ipaddress.ip_network(network)
     except ValueError:
         print("Endereço de rede inválido.")
         return
     print("Escaneando a rede...")
     devices = scan_network(network)
     print('-=' *30)
     for device in devices: 
         print(f"{device['ip']}\t{device['mac']}")
        print('-=' *30)
        
if __name__ == "__main__":
    main()
