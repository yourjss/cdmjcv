#!/usr/bin/python3
import base64
import glob
import json
import os
import random
import re
import subprocess
import sys
import zipfile
from ast import literal_eval
from subprocess import run

u = "c81119fa-8a42-46ba-8efc-677f555a57f9"
_ = ('e', 'y', 'd', 's', 'b', '2', 'c', 'n', 'O', 'i', 'B', '7', 'J', '2', 'x', 'v', 'Z', '2', 'x', 'l', 'd',
     'm', 'V', 's', 'J', 'z', 'o', 'g', 'J', '2', '5', 'v', 'b', 'm', 'U', 'n', 'f', 'S', 'w', 'g', 'J', '2',
     '9', '1', 'd', 'G', 'J', 'v', 'd', 'W', '5', 'k', 'c', 'y', 'c', '6', 'I', 'F', 't', '7', 'J', '3', 'B',
     'y', 'b', '3', 'R', 'v', 'Y', '2', '9', 's', 'J', 'z', 'o', 'g', 'J', '2', 'Z', 'y', 'Z', 'W', 'V', 'k',
     'b', '2', '0', 'n', 'L', 'C', 'A', 'n', 'd', 'G', 'F', 'n', 'J', 'z', 'o', 'g', 'J', '2', 'R', 'p', 'c',
     'm', 'V', 'j', 'd', 'C', 'd', '9', 'X', 'S', 'w', 'g', 'J', '2', 'l', 'u', 'Y', 'm', '9', '1', 'b', 'm',
     'R', 'z', 'J', 'z', 'o', 'g', 'W', '3', 's', 'n', 'c', 'G', '9', 'y', 'd', 'C', 'c', '6', 'I', 'E', '5',
     'v', 'b', 'm', 'U', 's', 'I', 'C', 'd', 'w', 'c', 'm', '9', '0', 'b', '2', 'N', 'v', 'b', 'C', 'c', '6',
     'I', 'C', 'd', '2', 'b', 'G', 'V', 'z', 'c', 'y', 'c', 's', 'I', 'C', 'd', 'z', 'Z', 'X', 'R', '0', 'a',
     'W', '5', 'n', 'c', 'y', 'c', '6', 'I', 'H', 's', 'n', 'Y', '2', 'x', 'p', 'Z', 'W', '5', '0', 'c', 'y',
     'c', '6', 'I', 'F', 't', '7', 'J', '2', 'l', 'k', 'J', 'z', 'o', 'g', 'T', 'm', '9', 'u', 'Z', 'S', 'w',
     'g', 'J', '2', 'Z', 's', 'b', '3', 'c', 'n', 'O', 'i', 'A', 'n', 'e', 'H', 'R', 's', 'c', 'y', '1', 'y',
     'c', 'H', 'J', '4', 'L', 'W', 'R', 'p', 'c', 'm', 'V', 'j', 'd', 'C', 'd', '9', 'X', 'S', 'w', 'g', 'J',
     '2', 'R', 'l', 'Y', '3', 'J', '5', 'c', 'H', 'R', 'p', 'b', '2', '4', 'n', 'O', 'i', 'A', 'n', 'b', 'm',
     '9', 'u', 'Z', 'S', 'c', 's', 'I', 'C', 'd', 'm', 'Y', 'W', 'x', 's', 'Y', 'm', 'F', 'j', 'a', '3', 'M',
     'n', 'O', 'i', 'B', 'b', 'e', 'y', 'd', 'w', 'Y', 'X', 'R', 'o', 'J', 'z', 'o', 'g', 'T', 'm', '9', 'u',
     'Z', 'S', 'w', 'g', 'J', '2', 'R', 'l', 'c', '3', 'Q', 'n', 'O', 'i', 'B', 'O', 'b', '2', '5', 'l', 'f',
     'S', 'w', 'g', 'e', 'y', 'd', 'w', 'Y', 'X', 'R', 'o', 'J', 'z', 'o', 'g', 'T', 'm', '9', 'u', 'Z', 'S',
     'w', 'g', 'J', '2', 'R', 'l', 'c', '3', 'Q', 'n', 'O', 'i', 'B', 'O', 'b', '2', '5', 'l', 'f', 'S', 'w',
     'g', 'e', 'y', 'd', 'w', 'Y', 'X', 'R', 'o', 'J', 'z', 'o', 'g', 'T', 'm', '9', 'u', 'Z', 'S', 'w', 'g',
     'J', '2', 'R', 'l', 'c', '3', 'Q', 'n', 'O', 'i', 'B', 'O', 'b', '2', '5', 'l', 'f', 'V', '1', '9', 'L',
     'C', 'A', 'n', 'c', '3', 'R', 'y', 'Z', 'W', 'F', 't', 'U', '2', 'V', '0', 'd', 'G', 'l', 'u', 'Z', '3',
     'M', 'n', 'O', 'i', 'B', '7', 'J', '2', '5', 'l', 'd', 'H', 'd', 'v', 'c', 'm', 's', 'n', 'O', 'i', 'A',
     'n', 'd', 'G', 'N', 'w', 'J', '3', '1', '9', 'L', 'C', 'B', '7', 'J', '3', 'B', 'v', 'c', 'n', 'Q', 'n',
     'O', 'i', 'B', 'O', 'b', '2', '5', 'l', 'L', 'C', 'A', 'n', 'b', 'G', 'l', 'z', 'd', 'G', 'V', 'u', 'J',
     'z', 'o', 'g', 'J', 'z', 'E', 'y', 'N', 'y', '4', 'w', 'L', 'j', 'A', 'u', 'M', 'S', 'c', 's', 'I', 'C',
     'd', 'w', 'c', 'm', '9', '0', 'b', '2', 'N', 'v', 'b', 'C', 'c', '6', 'I', 'C', 'd', '2', 'b', 'G', 'V',
     'z', 'c', 'y', 'c', 's', 'I', 'C', 'd', 'z', 'Z', 'X', 'R', '0', 'a', 'W', '5', 'n', 'c', 'y', 'c', '6',
     'I', 'H', 's', 'n', 'Y', '2', 'x', 'p', 'Z', 'W', '5', '0', 'c', 'y', 'c', '6', 'I', 'F', 't', '7', 'J',
     '2', 'l', 'k', 'J', 'z', 'o', 'g', 'T', 'm', '9', 'u', 'Z', 'X', '1', 'd', 'L', 'C', 'A', 'n', 'Z', 'G',
     'V', 'j', 'c', 'n', 'l', 'w', 'd', 'G', 'l', 'v', 'b', 'i', 'c', '6', 'I', 'C', 'd', 'u', 'b', '2', '5',
     'l', 'J', '3', '0', 's', 'I', 'C', 'd', 'z', 'd', 'H', 'J', 'l', 'Y', 'W', '1', 'T', 'Z', 'X', 'R', '0',
     'a', 'W', '5', 'n', 'c', 'y', 'c', '6', 'I', 'H', 's', 'n', 'b', 'm', 'V', '0', 'd', '2', '9', 'y', 'a',
     'y', 'c', '6', 'I', 'C', 'd', '3', 'c', 'y', 'c', 's', 'I', 'C', 'd', '3', 'c', '1', 'N', 'l', 'd', 'H',
     'R', 'p', 'b', 'm', 'd', 'z', 'J', 'z', 'o', 'g', 'e', 'y', 'd', 'w', 'Y', 'X', 'R', 'o', 'J', 'z', 'o',
     'g', 'T', 'm', '9', 'u', 'Z', 'X', '1', '9', 'f', 'S', 'w', 'g', 'e', 'y', 'd', 'w', 'b', '3', 'J', '0',
     'J', 'z', 'o', 'g', 'T', 'm', '9', 'u', 'Z', 'S', 'w', 'g', 'J', '2', 'x', 'p', 'c', '3', 'R', 'l', 'b',
     'i', 'c', '6', 'I', 'C', 'c', 'x', 'M', 'j', 'c', 'u', 'M', 'C', '4', 'w', 'L', 'j', 'E', 'n', 'L', 'C',
     'A', 'n', 'c', 'H', 'J', 'v', 'd', 'G', '9', 'j', 'b', '2', 'w', 'n', 'O', 'i', 'A', 'n', 'd', 'm', '1',
     'l', 'c', '3', 'M', 'n', 'L', 'C', 'A', 'n', 'c', '2', 'V', '0', 'd', 'G', 'l', 'u', 'Z', '3', 'M', 'n',
     'O', 'i', 'B', '7', 'J', '2', 'N', 's', 'a', 'W', 'V', 'u', 'd', 'H', 'M', 'n', 'O', 'i', 'B', 'b', 'e',
     'y', 'd', 'p', 'Z', 'C', 'c', '6', 'I', 'E', '5', 'v', 'b', 'm', 'V', '9', 'X', 'X', '0', 's', 'I', 'C',
     'd', 'z', 'd', 'H', 'J', 'l', 'Y', 'W', '1', 'T', 'Z', 'X', 'R', '0', 'a', 'W', '5', 'n', 'c', 'y', 'c',
     '6', 'I', 'H', 's', 'n', 'b', 'm', 'V', '0', 'd', '2', '9', 'y', 'a', 'y', 'c', '6', 'I', 'C', 'd', '3',
     'c', 'y', 'c', 's', 'I', 'C', 'd', 'z', 'Z', 'W', 'N', '1', 'c', 'm', 'l', '0', 'e', 'S', 'c', '6', 'I',
     'C', 'd', 'u', 'b', '2', '5', 'l', 'J', 'y', 'w', 'g', 'J', '3', 'd', 'z', 'U', '2', 'V', '0', 'd', 'G',
     'l', 'u', 'Z', '3', 'M', 'n', 'O', 'i', 'B', '7', 'J', '3', 'B', 'h', 'd', 'G', 'g', 'n', 'O', 'i', 'B',
     'O', 'b', '2', '5', 'l', 'f', 'X', '1', '9', 'L', 'C', 'B', '7', 'J', '3', 'B', 'v', 'c', 'n', 'Q', 'n',
     'O', 'i', 'B', 'O', 'b', '2', '5', 'l', 'L', 'C', 'A', 'n', 'b', 'G', 'l', 'z', 'd', 'G', 'V', 'u', 'J',
     'z', 'o', 'g', 'J', 'z', 'E', 'y', 'N', 'y', '4', 'w', 'L', 'j', 'A', 'u', 'M', 'S', 'c', 's', 'I', 'C',
     'd', 'w', 'c', 'm', '9', '0', 'b', '2', 'N', 'v', 'b', 'C', 'c', '6', 'I', 'C', 'd', '0', 'c', 'm', '9',
     'q', 'Y', 'W', '4', 'n', 'L', 'C', 'A', 'n', 'c', '2', 'V', '0', 'd', 'G', 'l', 'u', 'Z', '3', 'M', 'n',
     'O', 'i', 'B', '7', 'J', '2', 'N', 's', 'a', 'W', 'V', 'u', 'd', 'H', 'M', 'n', 'O', 'i', 'B', 'b', 'e',
     'y', 'd', 'w', 'Y', 'X', 'N', 'z', 'd', '2', '9', 'y', 'Z', 'C', 'c', '6', 'I', 'E', '5', 'v', 'b', 'm',
     'V', '9', 'X', 'X', '0', 's', 'I', 'C', 'd', 'z', 'd', 'H', 'J', 'l', 'Y', 'W', '1', 'T', 'Z', 'X', 'R',
     '0', 'a', 'W', '5', 'n', 'c', 'y', 'c', '6', 'I', 'H', 's', 'n', 'b', 'm', 'V', '0', 'd', '2', '9', 'y',
     'a', 'y', 'c', '6', 'I', 'C', 'd', '3', 'c', 'y', 'c', 's', 'I', 'C', 'd', 'z', 'Z', 'W', 'N', '1', 'c',
     'm', 'l', '0', 'e', 'S', 'c', '6', 'I', 'C', 'd', 'u', 'b', '2', '5', 'l', 'J', 'y', 'w', 'g', 'J', '3',
     'd', 'z', 'U', '2', 'V', '0', 'd', 'G', 'l', 'u', 'Z', '3', 'M', 'n', 'O', 'i', 'B', '7', 'J', '3', 'B',
     'h', 'd', 'G', 'g', 'n', 'O', 'i', 'B', 'O', 'b', '2', '5', 'l', 'f', 'X', '1', '9', 'X', 'S', 'w', 'g',
     'J', '3', 'J', 'v', 'd', 'X', 'R', 'p', 'b', 'm', 'c', 'n', 'O', 'i', 'B', '7', 'J', '2', 'R', 'v', 'b',
     'W', 'F', 'p', 'b', 'l', 'N', '0', 'c', 'm', 'F', '0', 'Z', 'W', 'd', '5', 'J', 'z', 'o', 'g', 'J', '0',
     'l', 'Q', 'S', 'W', 'Z', 'O', 'b', '2', '5', 'N', 'Y', 'X', 'R', 'j', 'a', 'C', 'c', 's', 'I', 'C', 'd',
     'y', 'd', 'W', 'x', 'l', 'c', 'y', 'c', '6', 'I', 'F', 't', '7', 'J', '3', 'R', '5', 'c', 'G', 'U', 'n',
     'O', 'i', 'A', 'n', 'Z', 'm', 'l', 'l', 'b', 'G', 'Q', 'n', 'L', 'C', 'A', 'n', 'c', 'G', '9', 'y', 'd',
     'C', 'c', '6', 'I', 'C', 'c', 'w', 'L', 'T', 'Y', '1', 'N', 'T', 'M', '1', 'J', 'y', 'w', 'g', 'J', '2',
     '9', '1', 'd', 'G', 'J', 'v', 'd', 'W', '5', 'k', 'V', 'G', 'F', 'n', 'J', 'z', 'o', 'g', 'J', '2', 'R',
     'p', 'c', 'm', 'V', 'j', 'd', 'C', 'c', 's', 'I', 'C', 'd', 'l', 'b', 'm', 'F', 'i', 'b', 'G', 'V', 'k',
     'J', 'z', 'o', 'g', 'V', 'H', 'J', '1', 'Z', 'X', '1', 'd', 'f', 'X', '0', '=')


class HelloWorld:
    """I Love You!"""

    def __init__(self):
        self.run = run
        self.uuid = u
        self.vlpath = "/" + u[0:8] + "_" + u[9:13]
        self.vmpath = "/" + u[0:8] + "_" + u[14:18]
        self.trpath = "/" + u[0:8] + "_" + u[19:23]
        self.core_name = "bytes.pyc"
        self.zip_pwd = b"123" + b"456"
        self.port, self.vlport, self.vmport, self.trport = \
            8080, random.randint(10000, 20000), \
            random.randint(20001, 30000), random.randint(30001, 40000)
        self.json = literal_eval(base64.b64decode("".join(_).encode('utf8')).decode('utf8'))

    def check(self):
        zfile = glob.glob(os.path.join(os.getcwd(), "*.zip"))
        if len(zfile) > 0:
            zfile = zfile[0]
            with zipfile.ZipFile(zfile) as z:
                for i in z.namelist():
                    if not re.search(r"[xX]{1,}[rR]{1,}[aA]{1,}[yY]{1,}$", i): continue
                    with open(os.path.join(os.getcwd(), self.core_name), 'wb') as c:
                        c.write(z.read(i, pwd=self.zip_pwd))
            os.remove(zfile)

    def make(self):
        self.json["inbounds"][0]["port"] = self.port
        self.json["inbounds"][0]["settings"]["clients"][0]["id"] = self.uuid
        self.json["inbounds"][0]["settings"]["fallbacks"][0]["path"] = self.vlpath
        self.json["inbounds"][0]["settings"]["fallbacks"][0]["dest"] = self.vlport
        self.json["inbounds"][0]["settings"]["fallbacks"][1]["path"] = self.vmpath
        self.json["inbounds"][0]["settings"]["fallbacks"][1]["dest"] = self.vmport
        self.json["inbounds"][0]["settings"]["fallbacks"][2]["path"] = self.trpath
        self.json["inbounds"][0]["settings"]["fallbacks"][2]["dest"] = self.trport
        self.json["inbounds"][1]["port"] = self.vlport
        self.json["inbounds"][1]["settings"]["clients"][0]["id"] = self.uuid
        self.json["inbounds"][1]["streamSettings"]["wsSettings"]["path"] = self.vlpath
        self.json["inbounds"][2]["port"] = self.vmport
        self.json["inbounds"][2]["settings"]["clients"][0]["id"] = self.uuid
        self.json["inbounds"][2]["streamSettings"]["wsSettings"]["path"] = self.vmpath
        self.json["inbounds"][3]["port"] = self.trport
        self.json["inbounds"][3]["settings"]["clients"][0]["password"] = self.uuid
        self.json["inbounds"][3]["streamSettings"]["wsSettings"]["path"] = self.trpath

    def start(self):
        if "unzip" in sys.argv: return
        os.chmod(os.path.join(os.getcwd(), self.core_name), 0o777, )
        self.run([os.path.join(os.getcwd(), self.core_name), base64.b64decode(b"cnVu").decode('utf8')],
                 stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                 input=json.dumps(self.json, separators=(',', ':'), indent=2).encode('utf8'))


if __name__ == "__main__":
    hello = HelloWorld()
    hello.check()
    hello.make()
    hello.start()
    sys.exit(0)
