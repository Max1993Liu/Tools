# open a temporary python file in /tmp directory
alias test='subl /tmp/test.py'

# close all chrome windows
alias bosscoming="kill $(ps -e | grep chrome | cut -d " " -f 2 | tr  '\n' ' ')"
