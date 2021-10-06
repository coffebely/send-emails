import requests


def get_logs(date_start, limit):
    return requests.get(
        "https://api.mailgun.net/v3/sandbox9533174d59624751a515752235e0f2c3.mailgun.org/events",
        auth=("api", "b4067df9b14b6b473a0865341d43fc82-443ec20e-0a52789b"),
        params={"begin": f"{date_start}",
                "ascending": "yes",
                "limit": f"{limit}",
                "event": "rejected OR failed OR delivered"
                })


def delivered(logs):
    total = 0
    successfully = 0
    for log in logs['items']:
        if log['event'] == 'delivered':
            successfully += 1
        total += 1
    return str(round(successfully/total*100))

