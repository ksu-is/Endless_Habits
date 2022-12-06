from datetime import datetime
from Habit_tracker_View import habit_break

import pandas as pd

from tabulate import tabulate

habits =[
    habit_break('coffee', datetime(2022, 11, 23, 10, 45))
]

df = pd.DataFrame(habits)

print(df)