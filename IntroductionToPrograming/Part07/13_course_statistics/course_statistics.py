import json
import urllib.request

def retrieve_all() -> list:
    courses = json.load(urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses"))
    
    to_return = []

    for course in courses:
        if course["enabled"]:
            data = (course["fullName"],course["name"],course["year"],sum(course["exercises"]))
            to_return.append(data)

    return to_return
    
if __name__ == "__main__":
    retrieve_all()
