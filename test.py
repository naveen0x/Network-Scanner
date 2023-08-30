import ping3

def check_device_status(target_ip):
    try:
        response_time = ping3.ping(target_ip, timeout=2)
        if response_time is not None:
            return f"Device at {target_ip} is online. Response time: {response_time} ms"
        else:
            return f"Device at {target_ip} is offline or unreachable."

    except OSError:
        return f"Error: Unable to reach the device at {target_ip}."

def check_ip_range_status(ip_range):
    for i in range(ip_range[0], ip_range[1] + 1):
        target_ip = f"{ip_range[2]}.{ip_range[3]}.{ip_range[4]}.{i}"
        status_result = check_device_status(target_ip)
        print(status_result)

if __name__ == "__main__":
    # Define the IP range as a tuple (start, end, first_octet, second_octet, third_octet)
    target_ip_range = (1, 10, 192, 168, 8)

    check_ip_range_status(target_ip_range)
