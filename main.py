import ipaddress

def calcular_rango_ips(red):
    # Crear un objeto de red basado en la dirección de red y la máscara de subred
    red_ip = ipaddress.ip_network(red, strict=False)
    
    # Obtener la dirección de red
    direccion_red = red_ip.network_address
    
    # Obtener la primera IP usable
    primera_ip = list(red_ip.hosts())[0]
    
    # Obtener la última IP usable
    ultima_ip = list(red_ip.hosts())[-1]
    
    # Obtener la dirección de broadcast
    direccion_broadcast = red_ip.broadcast_address
    
    # Máscara de subred
    mascara_subred = red_ip.netmask
    
    # Número de hosts posibles
    numero_hosts = red_ip.num_addresses - 2  # Restando red y broadcast
    
    return {
        "Direccion de Red": str(direccion_red),
        "Primera IP": str(primera_ip),
        "Ultima IP": str(ultima_ip),
        "Broadcast": str(direccion_broadcast),
        "Mascara de Subred": str(mascara_subred),
        "Numero de Hosts": numero_hosts
    }

# Redes a calcular
redes = [
    "133.225.128.0/20",
    "142.104.81.64/28",
    "78.51.90.0/23"
]

# Calcular y mostrar los resultados
for red in redes:
    resultado = calcular_rango_ips(red)
    print(f"Red: {red}")
    for key, value in resultado.items():
        print(f"{key}: {value}")
    print("-" * 40)
