#!/usr/bin/python
"""Set Gallery admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import hashlib
import random
import string
import shutil

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Gallery Password",
            "Enter new password for the Gallery 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Gallery Email",
            "Enter email address for the Gallery 'admin' account.",
            "admin@example.com")
    
    salt = "".join(random.choice(string.letters) for line in range(4))
    hashpass = salt + hashlib.md5(salt + password).hexdigest()

    m = MySQL()
    m.execute('UPDATE gallery2.g2_User SET g_email=\"%s\" WHERE g_userName=\"admin\";' % email)
    m.execute('UPDATE gallery2.g2_User SET g_hashedPassword=\"%s\" WHERE g_userName=\"admin\";' % hashpass)

    # delete cache so it will be rebuilt for new domain
    shutil.rmtree("/var/lib/gallery2/g2data/cache/entity", ignore_errors=True)


if __name__ == "__main__":
    main()

