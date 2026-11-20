import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 250)
pd.set_option("display.max_colwidth", 90)

rows = []
with open("data/HDFS_2k.log") as f:
    for line in f:
        rows.append(line.split(" ", 5))

df = pd.DataFrame(rows, columns=["date", "time", "pid", "level", "component", "message"])
df["message"] = df["message"].str.strip()

print(df.head())
print(df.shape)
print(df["level"].value_counts())
print(df["component"].value_counts().head(5))

warn = df[df["level"] == "WARN"]
print(warn["component"].value_counts())
print(warn["message"].str.contains("Got exception while serving").sum())
