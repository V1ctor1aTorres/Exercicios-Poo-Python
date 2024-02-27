class Date:
    def __init__(self, year, month, day):                                              #Init method
        self.year = year
        self.month = month
        self.day = day
    def arrange_value_date(self):                                                      #Instance Method
        date = str(f'{self.day}/{self.month}/{self.year}')
        return date
    @classmethod
    def data_from_string(clr, string):
        import re
        data = re.findall('\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}', string)[0]                    #00-00-0000 or  00/00/0000
        list_date = data.replace('/', '-').split('-')  
        day = list_date[0]
        month = list_date[1]     
        year = list_date[2] 
        return clr(year, month, day)    

                
    
date1 = Date(2024, 2, 26)
date2 = Date.data_from_string('Today is 17/06/2024')
print(date2.__dict__)
