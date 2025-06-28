# Password Hacker with Python

A sophisticated password hacking simulator that demonstrates various cybersecurity concepts and hacking techniques in a controlled environment.


This project simulates a password hacking scenario where you need to infiltrate a server with unknown credentials. The program uses several techniques to gain unauthorized access:

1. **Dictionary-based login attacks** - Using a list of common usernames to find valid accounts
2. **Time-based vulnerability exploitation** - Detecting timing differences in server responses to guess password characters
3. **Exception handling** - Robust error management for network operations
4. **JSON-based communication** - Structured data exchange with the target server


- Socket-based client-server communication
- Dictionary-based username discovery
- Character-by-character password cracking using timing attacks
- JSON request/response handling
- Comprehensive error handling and logging


- Python 3
- Core modules:
  - `socket` - For network communication
  - `json` - For data serialization/deserialization
  - `time` - For measuring response times in timing attacks
  - `string` - For character set generation
  - `sys` - For command-line arguments and program control


1. Ensure you have Python 3 installed
2. Clone this repository
3. Make sure you have the required dictionary files (`logins.txt` and `passwords.txt`)
4. Run the program with the target server's IP address and port:

```bash
python hack.py <IP_address> <port>
```

5. The program will attempt to find valid credentials and output them in JSON format if successful


This project demonstrates:
- Network programming fundamentals
- Authentication vulnerabilities
- Brute force and dictionary attack techniques
- Time-based side-channel attacks
- Proper error handling in network applications
- Working with JSON for data exchange


This tool is created for educational purposes only. Using this program against systems without explicit permission is illegal and unethical. Always practice responsible security testing and only use these techniques on systems you own or have permission to test.


This project was completed as part of the JetBrains Academy Python track.
Project link: https://hyperskill.org/projects/80


[MIT License](LICENSE)
