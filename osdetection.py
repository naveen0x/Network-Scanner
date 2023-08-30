import socket

def os_fingerprinting(target_ip, target_port):
    try:
        # Create a socket and connect to the target device
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Set a timeout for the connection attempt
        s.connect((target_ip, target_port))

        # Send a sample request (you can customize this based on the target application)
        s.sendall(b"GET / HTTP/1.0\r\n\r\n")

        # Receive the response
        response = s.recv(1024)
        print(response)

        # Analyze the response for characteristic patterns of specific OS
        if b"Windows" in response:
            return "Windows"
        elif b"Linux" in response:
            return "Linux"
        elif b"FreeBSD" in response:
            return "FreeBSD"
        elif b"Mac" in response:
            return "Mac OS"
        else:
            return "Unknown"

    except socket.timeout:
        return "Timeout: Unable to connect to the target device."
    except (socket.error, ConnectionRefusedError):
        return "Error: Unable to connect to the target device."
    finally:
        s.close()

if __name__ == "__main__":
    target_ip = "192.168.8.1"  # Replace this with the IP address of the target device
    target_port = 80  # Replace this with the target device's open port (e.g., 80 for HTTP)

    os_info = os_fingerprinting(target_ip, target_port)
    print(f"IP: {target_ip} - Operating System: {os_info}")
    
