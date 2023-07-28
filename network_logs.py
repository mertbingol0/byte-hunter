from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def process_packet(packet):
    # IP paketini al
    ip_packet = packet.getlayer(IP)
    if ip_packet:
        # Kaynak ve hedef IP adreslerini al
        src_ip = ip_packet.src
        dst_ip = ip_packet.dst

        # Port bilgilerini kontrol et
        if ip_packet.haslayer(TCP):
            src_port = ip_packet[TCP].sport
            dst_port = ip_packet[TCP].dport
            protocol = "TCP"
        elif ip_packet.haslayer(UDP):
            src_port = ip_packet[UDP].sport
            dst_port = ip_packet[UDP].dport
            protocol = "UDP"
        else:
            return

        # Elde edilen bilgileri log dosyasına yaz
        with open('trafik.log', 'a') as f:
            log_entry = f"{src_ip}:{src_port} -> {dst_ip}:{dst_port}: {protocol}\n"
            f.write(log_entry)

# Ağ trafiğini dinleme işlemi
sniff(iface="eth0", filter="ip", prn=process_packet)
