import re
from collections import Counter

# File path to the authentication log
LOG_FILE_PATH = "auth.log"

# Threshold for flagging brute-force attempts
THRESHOLD = 5

def parse_auth_logs(file_path):
    # Regex pattern to match failed SSH login attempts and capture the IP address
    # Example log entry: "Failed password for invalid user admin from 192.168.1.100 port 54321 ssh2"
    failed_ip_pattern = re.compile(r"Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    
    failed_attempts = Counter()

    try:
        with open(file_path, "r") as file:
            for line in file:
                match = failed_ip_pattern.search(line)
                if match:
                    ip_address = match.group(1)
                    failed_attempts[ip_address] += 1

        print("=== SSH Authentication Failure Summary ===")
        if not failed_attempts:
            print("No failed SSH login attempts detected.")
            return

        print(f"{'Source IP Address':<20} | {'Failed Attempts':<15} | {'Status':<15}")
        print("-" * 55)

        for ip, count in failed_attempts.items():
            status = "🚨 ALERT (Brute-Force)" if count >= THRESHOLD else "NORMAL"
            print(f"{ip:<20} | {count:<15} | {status:<15}")

    except FileNotFoundError:
        print(f"Error: Log file '{file_path}' not found. Make sure the file exists in the directory.")

if __name__ == "__main__":
    parse_auth_logs(LOG_FILE_PATH)
