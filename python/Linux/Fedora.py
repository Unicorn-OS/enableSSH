enableSSHCommand():
    cmd0 = "systemctl enable sshd.service"
    cmd1 = "systemctl start sshd.service"
    return (cmd0, cmd1)
