import email.utils

for _ in range(int(input())):
    email_address = str(input())

    if email.utils.parseaddr(email_address)[1]:
        if email.utils.parseaddr(email_address)[1] != ("", ""):
            print(email.utils.formataddr(email.utils.parseaddr(email_address)))

#### 2nd solution ####

import re

for _ in range(int(input())):
    email_address = str(input())

    if re.match(r"^[a-zA-Z][\w\-\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$", email_address):
        print(email_address)
