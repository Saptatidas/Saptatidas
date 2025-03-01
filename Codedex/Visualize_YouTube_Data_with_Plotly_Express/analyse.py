import pandas as pd
import plotly.express as px
import kagglehub
from pathlib import Path

# Download latest version
path = kagglehub.dataset_download("surajjha101/top-youtube-channels-data")

print("Path to dataset files:", path)

df = pd.read_csv(f"{path}/most_subscribed_youtube_channels.csv")

df = df.replace(',', '', regex=True)

df['subscribers'] = pd.to_numeric(df['subscribers'], errors='coerce')
df['video views'] = pd.to_numeric(df['video views'], errors='coerce')
df['video count'] = pd.to_numeric(df['video count'], errors='coerce')
df['started'] = pd.to_numeric(df['started'], errors='coerce')

print("Path to dataset files:", path)
print(df.head())

fig1 = px.histogram(df, x='subscribers')
fig1.update_layout(title_text="Subscriber Count")  # ✅ Correct way

fig1.show()

fig2 = px.pie(df, values='subscribers', names='category')
fig2.update_layout(title_text="YouTube Categories")  
fig2.show()

fig3 = px.box(df, y='started')
fig3.update_layout(title_text="Years Started")  
fig3.show()


