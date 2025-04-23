import socket
import argparse
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_port(host, port):
    """
    Scans a single port on a given host.

    Args:
        host (str): The hostname or IP address to scan.
        port (int): The port number to scan.

    Returns:
        str: A string indicating the status of the port (open, closed, or filtered).
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout to prevent indefinite blocking

        # Attempt to connect to the host and port
        result = sock.connect_ex((host, port))

        if result == 0:
            return "open"
        elif result == 111: # Connection refused
            return "closed"
        else:
            return "filtered"
    except socket.gaierror:
        logging.error(f"Could not resolve hostname: {host}")
        return "error"
    except socket.error as e:
        logging.error(f"Socket error: {e}")
        return "error"
    finally:
        sock.close()


def setup_argparse():
    """
    Sets up the argument parser for the command-line interface.

    Returns:
        argparse.ArgumentParser: The argument parser object.
    """
    parser = argparse.ArgumentParser(description="Scans a specified range of ports on a given host.")
    parser.add_argument("host", help="The hostname or IP address to scan.")
    parser.add_argument("start_port", type=int, help="The starting port number.")
    parser.add_argument("end_port", type=int, help="The ending port number.")

    return parser


def main():
    """
    The main function that drives the port scanner.
    """
    try:
        # Parse command-line arguments
        parser = setup_argparse()
        args = parser.parse_args()

        host = args.host
        start_port = args.start_port
        end_port = args.end_port

        # Input validation: Check if the port range is valid
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            logging.error("Invalid port range. Start port must be between 1 and 65535, and less than or equal to end port.")
            sys.exit(1)

        # Scan the specified port range
        logging.info(f"Scanning ports {start_port} to {end_port} on {host}")
        for port in range(start_port, end_port + 1):
            status = scan_port(host, port)
            print(f"Port {port}: {status}")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage:
    # python main.py example.com 20 25
    # python main.py 192.168.1.1 80 81
    main()