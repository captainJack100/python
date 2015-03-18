""" Hex Decoder
Used to un-obfuscate obfuscated code.
"""

import re

a = open("hexDecoderExample.php")
line=a.readlines()

# We want only the number ... remove 0x from hex 
def decoder(char):
	return char[2:].decode("hex")

# NOTE: The group() returns the entire match.
print re.sub("\\\\x[a-f0-9][a-f0-9]", lambda m: decoder(m.group()), line[0])
