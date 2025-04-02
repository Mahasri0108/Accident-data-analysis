Project Overview
This project analyzes traffic accident data to identify patterns related to road conditions, weather, and time of day. It also visualizes accident hotspots using heatmaps.

📊 Features
✅ Data Cleaning & Preprocessing – Handles missing values and extracts meaningful insights.
✅ Exploratory Data Analysis (EDA) – Analyzes trends based on time, weather, and road conditions.
✅ Accident Cause Analysis – Identifies top contributing factors for accidents.
✅ Interactive Heatmap Visualization – Displays accident hotspots on a Folium map.

📂 Dataset
The dataset used is the NYC Motor Vehicle Collisions dataset, available from NYC Open Data.

Key Features:

CRASH DATE – Date of the accident

CRASH TIME – Time of the accident

LATITUDE & LONGITUDE – Accident location

CONTRIBUTING FACTOR VEHICLE 1 – Primary cause of the accident

NUMBER OF PERSONS INJURED – Total injuries

🚀 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/traffic-accident-analysis.git
cd traffic-accident-analysis
2️⃣ Install Dependencies
bash
Copy
Edit
pip install pandas numpy matplotlib seaborn folium
3️⃣ Run the Analysis
bash
Copy
Edit
python accident_analysis.py
4️⃣ View the Heatmap
After running the script, open accident_hotspots.html in a web browser to explore accident hotspots.

📌 Project Structure
bash
Copy
Edit
📂 traffic-accident-analysis/
│-- 📜 accident_analysis.py      # Main Python script
│-- 📜 README.md                 # Project documentation
│-- 📜 requirements.txt          # List of dependencies
│-- 📜 accident_hotspots.html    # Generated heatmap
📊 Visualizations
📅 Accidents by Time of Day
This visualization shows the distribution of accidents over 24 hours.

🔥 Accident Hotspot Map
A heatmap displays areas with a high concentration of accidents.

🎯 Future Improvements
📍 Geospatial Analysis – Cluster accidents using DBSCAN

🌧 Weather Data Integration – Analyze accidents during extreme weather

🚦 Traffic Light Impact – Study accident rates at intersections
