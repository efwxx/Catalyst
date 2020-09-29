from replit import db

db["key"] = "VGDPS"

value = db["key"]

del db["key"]

keys = db.keys()

matches = db.prefix("prefix")
