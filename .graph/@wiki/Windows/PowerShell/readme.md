https://adamtheautomator.com/openssh-windows/#Changing_the_Default_Shell_for_OpenSSH_to_PowerShell

```
New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force
```
