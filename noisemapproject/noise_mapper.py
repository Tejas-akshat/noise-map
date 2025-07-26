import pandas as pd
import folium

# Step 1: Read the CSV file
data = pd.read_csv("noise.csv", skipinitialspace=True)

# Step 2: Create Base Map (Satellite View - Esri)
center_lat = data['Latitude'].mean()
center_lng = data['Longitude'].mean()

mymap = folium.Map(
    location=[center_lat, center_lng],
    zoom_start=18,
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Tiles © Esri — Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye'
)

# Step 3: Add Colored Markers with Popup
for _, row in data.iterrows():
    dB = row['Sound_Level']
    place = row['Place']

    if dB > 60:
        color = 'red'
    elif dB > 40:
        color = 'orange'
    else:
        color = 'green'

    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=10,
        popup=f"{place} - {dB} dB",
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.9
    ).add_to(mymap)

# Step 4: Save the map
mymap.save("noise_map.html")
print("✅ Map created successfully with satellite view!")
