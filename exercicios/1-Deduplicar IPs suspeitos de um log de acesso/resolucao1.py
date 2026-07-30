# Lista de IPs suspeitos de um log de acesso
ips = [
    "192.168.1.10",
    "10.0.0.5",
    "172.16.0.2",
    "192.168.1.10",
    "203.0.113.45",
    "198.51.100.18",
    "10.0.0.5",
    "8.8.8.8",
    "172.16.0.2",
    "192.0.2.25",
    "203.0.113.45",
    "10.10.10.10",
    "192.168.0.15",
    "198.51.100.18",
    "172.20.5.9",
    "203.0.113.77",
    "8.8.4.4",
    "10.10.10.10",
    "192.168.100.100",
    "203.0.113.90",
    "172.20.5.9",
    "192.0.2.25",
    "198.18.0.1",
    "203.0.113.77",
    "100.64.0.10",
    "192.168.1.10",
    "198.18.0.1",
    "203.0.113.90",
    "8.8.8.8",
    "10.0.0.5"
]
# Função para ler os ips e se não constiver na lista de ips_unicos, adiciona na lista
def ips_duplicados(ips):
    ips_unicos = []
    
    for ip in ips:
        if ip not in ips_unicos:
            ips_unicos.append(ip)
            
    print(ips_unicos)
    return ips_unicos

#chamada da funcao
ips_duplicados(ips)