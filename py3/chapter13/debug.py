#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter13/debug.py

import sys, smtplib, socket

message_template = """To: %s
From: %s
Subject: Test Message from simple.py

Hello,

This is a test message sent to you from the debug.py program
in Foundations of Python Network Programming.
"""

def main():
    if len(sys.argv) < 4:
        print("usage: %s server fromaddr toaddr [toaddr...]"
              % sys.argv[0])
        sys.exit(2)

    server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]
    message = message_template % (', '.join(toaddrs), fromaddr)

    try:
        s = smtplib.SMTP(server)
        s.set_debuglevel(1)
        s.sendmail(fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,
            smtplib.SMTPException) as e:
        print(" *** Your message may not have been sent!")
        print(e)
        sys.exit(1)
    else:
        print("Message successfully sent to %d recipient(s)"
              % len(toaddrs))
        s.quit()

if __name__ == '__main__':
    main()
