import webuntis
import sys
from datetime import datetime, timedelta
import json
from dotenv import load_dotenv
import os

load_dotenv()

base_path = './frontend/static/timetables/'

TIMETABLE = os.getenv("UNTIS_TIMETABLE")
USERNAME = os.getenv("UNTIS_USERNAME")
PASSWORD = os.getenv("UNTIS_PASSWORD")
SCHOOL = os.getenv("UNTIS_SCHOOL")

def main():
    # get monday of the current week
    start = datetime.strptime((datetime.now() - timedelta(days=datetime.now().weekday())).strftime('%Y-%m-%d'), '%Y-%m-%d')
    #get friday of current week
    end = datetime.strptime((datetime.now() + timedelta(days=4-datetime.now().weekday())).strftime('%Y-%m-%d'), '%Y-%m-%d')

    try:
        with webuntis.Session(server='melpomene.webuntis.com', username=USERNAME, password=PASSWORD, school=SCHOOL, useragent='WebUntis API Test').login() as s:
            klasse = s.klassen().filter(name=TIMETABLE)[0]

            table = s.timetable(start=start, end=end, klasse=klasse).to_table()
            with open(base_path + 'timetable.json', 'w') as f:
                periods_dict = {}
                for time, periods in table:
                    for date, period_set in periods:
                        for period in period_set:
                            subject = period.subjects[0]

                            period_dict = {
                                'id': period.id,
                                'subject': subject.long_name,
                                'startTime': period.start.strftime('%H:%M:%S') if period.start else None,
                                'endTime': period.end.strftime('%H:%M:%S') if period.end else None,
                                'activityType': period.activityType
                            }
                            day_of_week = date.strftime('%A').lower()

                            if day_of_week not in periods_dict:
                                periods_dict[day_of_week] = []

                            periods_dict[day_of_week].append(period_dict)

                f.write(json.dumps(periods_dict, indent=4))

            s.logout()
        
        with open(base_path + 'timetable.json', 'r') as f:
            timetable = f.read()
            print(timetable)

    except KeyboardInterrupt:
        print("Aborted.")
        sys.exit(0)

if __name__ == '__main__':
    main()