# SSH
## os: Windows
guide: [ssh-copy-id on Windows](https://www.chrisjhart.com/Windows-10-ssh-copy-id/)

source:
`type $env:USERPROFILE\.ssh\id_rsa.pub | ssh {IP-ADDRESS-OR-FQDN} "cat >> .ssh/authorized_keys"`

password:
https://geekrewind.com/how-to-set-up-ssh-key-login-with-windows-11/
