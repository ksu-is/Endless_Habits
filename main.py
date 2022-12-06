from datetime import datetime
from Habit_tracker_View import habit_break

import pandas as pd

from tabulate import tabulate

habits =[
    habit_break('coffee', datetime(2022, 11, 23, 10, 45)),
    habit_break('vaping', datetime(2022, 12, 2, 8, 16)),
    habit_break('sleeping late', datetime(2022, 11, 15, 5, 28)),
]

df = pd.DataFrame(habits)

print(tabulate(df, headers='keys', tablefmt='psql'))