https://adamtheautomator.com/openssh-windows/#Installing_OpenSSH

```
# Start
## changes the sshd service's startup type from manual to automatic.
 Set-Service sshd -StartupType Automatic
## starts the sshd service.
 Start-Service sshd
 
# Open Firewall
 New-NetFirewallRule -Name sshd -DisplayName 'Allow SSH' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
 ```
