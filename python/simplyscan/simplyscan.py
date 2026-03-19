import socket
import threading
import time

common_ports = {
    21: "FTP", 
    22: "SSH",
    23: "TelNet", 
    25: "SMTP",
    53: "DNS", 
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}
print     (r"""
                      (  )   (   )  )
                      ) (   )  (  (
                      ( )  (    ) )
                      ____________
                     <____________>___
                    |             |/ _ \
                    |               | | |
                    |               |_| |
                 ___|             |\___/
                /    \___________/    \
                \_____________________/
""") 
print("=======================================================")
print("                    SimplyScan v1.0                    ")
print("               By Ryan McClure, March 2026             ")
print("=======================================================")

# I worked really hard on this mug, okay?

target = input("Enter Target IP Address: ")

start_port = 1
end_port = 1024

open_ports = []

print("\nScanning Target IP", target)
print("Port Range:", start_port, "to" , end_port)
print("-----------------------------------")

start_time = time.time()


try: 
    hostname = socket.gethostbyaddr(target)
    print("Hostname:", hostname[0])
except:
    print("Hostname: Not Found")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    
    result = sock.connect_ex((target, port))
    
    if result == 0:
        if port in common_ports:
            print("Port", port, "is Open -", common_ports[port])
        else:
            print("Port", port, "is Open")

        open_ports.append(port)

sock.close()

print("------------------------------------")
print("Scan Complete.")

if len(open_ports) > 0:
        print("Open Ports Found:")
        for port in open_ports:
         if port in common_ports:
            print(port, "-", common_ports[port])
        else:
            print(port)

else:
     print("No Open Ports Found.")