from dateutil import parser
from datetime import *
from dateutil import relativedelta

txt = 'in 30 minutes'
date = parser.parse(txt, fuzzy=True).time()
now = datetime.now()
print(date + relativedelta(time=now + date))
