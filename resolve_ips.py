import socket

input_file = "ips.txt"
output_file = "hostnames.csv"


with open(output_file, "w") as out_file:
    out_file.write(f"IP,hostname\n")
    # Lê a lista de IPs
    with open(input_file, "r") as in_file:
        for ip in in_file:
            ip = ip.strip()
            if ip:
                try:
                    # Resolve o hostname
                    hostname = socket.gethostbyaddr(ip)[0]
                except socket.herror:
                    # Caso não encontre o hostname
                    hostname = "not_found"
                # Salva no arquivo de saída
                out_file.write(f"{ip},{hostname}\n")

print(f"Consulta concluída. Resultado salvo em {output_file}")
