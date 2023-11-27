def online_count(statuses):
    numOnline = 0
    
    for value in statuses.values():
        if(value == "online"):
            numOnline += 1
    return
    
    
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))
