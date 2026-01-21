# Energy forecasting logic will be implemented here
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load sample weather data
data = pd.read_csv("data/weather_sample.csv")  # we'll add this next

X = data[["sunlight", "cloud_cover", "temperature"]]
y = data["solar_output"]

# Train simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Simulate tomorrow's weather
tomorrow_weather = [[6.0, 40, 31]]  # sunlight, cloud_cover, temperature
predicted_energy = model.predict(tomorrow_weather)

print(f"Predicted Solar Energy Tomorrow: {predicted_energy[0]:.2f} kWh")

# Simple AI Decision
if predicted_energy[0] < 15:
    print("⚠️ Low solar expected tomorrow")
    print("Recommendation: Charge EV or run appliances tonight")
else:
    print("✅ Good solar expected tomorrow")
    print("Recommendation: Use solar power during the day")
