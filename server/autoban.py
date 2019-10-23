#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2015 clowwindy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import absolute_import, division, print_function, \
    with_statement

import os
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='See README')
    parser.add_argument('-c', '--count', default=1, type=int,
                        help='with how many failure times it should be '
                             'considered as an attack')
    config = parser.parse_args()
    ips = {}
    banned = set()
	
    cmd1='firewall-cmd --list-rich-rules'
    f = os.popen(cmd1,"r")
    bannedips = f.read()
    f.close()
    if bannedips != '':
	    bannedips2 = bannedips.split('\n')
	    for line1 in bannedips2:
		    if line1 != '':
			    ip1 = line1.split('"')[3]
			    banned.add(ip1)

    for line in sys.stdin:
        if 'Protocol ERROR, TCP ogn data' in line:
            ip = line.split(':')[6]
            if ip not in ips:
                ips[ip] = 1
                sys.stdout.flush()
            else:
                ips[ip] += 1

#            print(config.count)
            if ip not in banned and ips[ip] >= config.count:
                banned.add(ip)
                cmd = 'firewall-cmd --permanent --add-rich-rule="rule family=\'ipv4\' source address=%s reject"' % ip
                print(cmd, file=sys.stderr)
                sys.stderr.flush()
                os.system(cmd)
    cmd2 = 'firewall-cmd --reload'
    print(cmd2, file=sys.stderr)
    os.system(cmd2)
