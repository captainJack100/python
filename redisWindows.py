""" RedisWindows.py'
Simple redis in windows 7 example.
"""

import redis as rr

def main():
	r = rr.StrictRedis(host = "127.0.0.1", port = 6379, db = 0)
	r.set("name", "kem")
	print(r.get("name"))

if __name__ == "__main__":
	main()


