query_template = '''
INSERT INTO vidya.event.event(KEY,VALUE) VALUES(
    "event-gs-{month}-{day}",
    {{
      "endDate": "{year}-{month}-{day_end}",
      "programConfigs": [
        {{
          "accessType": 0,
          "delivery": 0,
          "donationMode": 2,
          "participationLocation": 2,
          "participationScope": 0
        }}
      ],
      "programId": "event-program-gita-samagam",
      "sessions": [],
      "startDate": "{year}-{month}-01",
      "title": {{
        "english": "Bhagavad Gita Course - {month_name} {year}",
        "hindi": "श्रीमद्भगवद्गीता कोर्स {month_name} {year}"
      }},
      "type": "Event"
    }})
'''

day = 25  # You can modify this variable to change the day (it is yyyy in yy day)
month = "04"  # You can modify this variable to change the month
year = 2025  # You can modify this variable to change the year
day_end = 30  # You can modify this variable to change the end day
month_name = "April"  # You can modify this variable to change the month name

query = query_template.format(day=day, month=month, year=year, day_end=day_end, month_name=month_name)

print(query)