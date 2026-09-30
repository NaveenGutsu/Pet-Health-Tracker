import pandas as pd
import numpy as np


puppy_log = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Weight_kg": [2.1, 2.1, 2.2, 2.2, 2.3, 2.3, 2.4],
    "Walk_Minutes": [20, 25, 15, 30, 0, 35, 40],
    "Meals_Eaten": [3, 3, 2, 3, 3, 3, 3],
    "Naps_Count": [5, 4, 6, 4, 5, 3, 4],
    "Mood": ["Happy", "Playful", "Sleepy", "Energetic", "Lazy", "Hyper", "Playful"]
}


df = pd.DataFrame(puppy_log)

print("--- WEEKLY PUPPY DIARY ---")
print(df)
print("\n" + "=" * 45 + "\n")


avg_walk = df["Walk_Minutes"].mean()
print(f"Average daily walk: {avg_walk:.1f} minutes")


weight_gain = df["Weight_kg"].iloc[-1] - df["Weight_kg"].iloc[0]
print(f"Total weight gained this week: {weight_gain:.2f} kg")


lazy_days = df[df["Walk_Minutes"] < 20]
print("\n--- DAYS WITH LOW ACTIVITY (< 20 mins) ---")
print(lazy_days[["Day", "Walk_Minutes", "Mood"]])


df["Day_Type"] = np.where(df["Walk_Minutes"] >= 30, "Active Day", "Chill Day")


print("\n--- EXERCISE SUMMARY STATS ---")
print(df["Walk_Minutes"].describe())


df.to_csv("puppy_weekly_report.csv", index=False)
print("\nReport saved as 'puppy_weekly_report.csv'!")
