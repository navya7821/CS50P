from datetime import date
import sys
import inflect
class Seasons:
    def __init__(self):
        self.birth_date = self.get_birthdate()
        self.today_date = date.today()
        self.duration = round((self.today_date - self.birth_date).total_seconds()/60)
        #print(self.duration)
        self.final = self.get_sec(self.duration).capitalize().replace(' and','')




    def __str__(self):
        return f"{self.final} minutes"

    @classmethod
    def get_sec(cls,minutes):
        p = inflect.engine()
        duration = p.number_to_words(minutes)
        return duration

    @classmethod
    def get_birthdate(cls):
        try:
            date_inp = input("Date of Birth: ")
            year,month,day = date_inp.split('-')
            year,month,day = int(year),int(month),int(day)
            birth_date = date(year,month,day)
            return birth_date
        except ValueError:
            sys.exit('Invalid date')

def main():
    season = Seasons()
    print(season)


if __name__ == "__main__":
    main()


