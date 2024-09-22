config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPass" : "admin123"
}
print(len(config))
print(config["dbType"])

for key, values in config.items():
    print("Klucz w config: "+ key + " z wartością: " + values)