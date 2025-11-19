import requests

url = "http://localhost:9696/predict"

pipeline_input = {
    "pipeline_length": 800,
    "inner_diameter": 24,
    "target_residual_conc": 2.3,
    "operating_pressure": 50.1,
    "temperature": 35.2,
    "num_bends": 0,
    "ambient_temperature": 30.5,
    "num_purge_cycles": 3,
    "safety_factor": 1.2,
    "pipeline_volume": 233.5
}

response = requests.post(url, json=pipeline_input)
result = response.json()

print("response:", result)

if result["nitrogen_volume_needed"] >= 1500:
    print(f"Predicted volume: {result['nitrogen_volume_needed']:.2f}")
    print("Trigger high-volume purge protocol")
else:
    print(f"Predicted volume: {result['nitrogen_volume_needed']:.2f}")
    print("Standard purge protocol")