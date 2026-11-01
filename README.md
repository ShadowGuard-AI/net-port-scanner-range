# net-port-scanner-range
Scans a specified range of ports on a given host. Provides status for each port, such as open, closed, or filtered. - Focused on Basic network operations

## Install
`git clone https://github.com/ShadowStrikeHQ/net-port-scanner-range`

## Usage
`./net-port-scanner-range [params]`

## Parameters
- `-h`: Show help message and exit

## License
Copyright (c) ShadowStrikeHQ

## Notes
- The target is resolved once, before any port is scanned. If the host cannot be resolved, the run prints an error and exits 1 without scanning.
- No third-party packages are required: the tool uses only the Python standard library.
