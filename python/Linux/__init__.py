include os
include subprocess



if ( ubuntu ):
    Command.runSudo(Ubuntu.enableSSHCommand())
else if ( fedora ):
    Command.runSudo(Ubuntu.enableSSHCommand())
