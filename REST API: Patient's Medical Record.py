import requests

def getAverageTemperatureForUser(userId):
    base_url = "https://jsonmock.hackerrank.com/api/medical_records"

    page = 1
    total_temps = 0
    total_records = 0

    while True:
        response = requests.get(f"{base_url}?userId={userId}&page={page}").json()
        data = response["data"]

        if not data:
            break

        for record in data:
            body_temperature = record.get("vitals", {}).get("bodyTemperature", 0)
            total_temps += body_temperature
            total_records += 1

        if page >= response["total_pages"]:
            break

        page += 1

    if total_records == 0:
        return "0"

    average_temp = round(total_temps / total_records, 1)
    return str(average_temp)