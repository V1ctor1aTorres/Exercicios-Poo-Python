class Date:
    def __init__(self, year, month, day):                                              #Init method
        self.year = year
        self.month = month
        self.day = day
    def arrange_value_date(self):                                                      #Instance Method
        date = str(f'{self.day}/{self.month}/{self.year}')
        return date
    
date1 = Date(2024, 2, 26)
print(date1.arrange_value_date())