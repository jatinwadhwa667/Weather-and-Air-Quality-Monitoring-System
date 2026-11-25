# Weather and Air Quality Monitoring System

## Project Overview

This is a Python-based project that fetches real-time weather and air quality information for a city using OpenWeather APIs.

The project provides details such as temperature, weather conditions, geographical coordinates, and Air Quality Index (AQI).

## Technologies Used

- Python
- Requests
- REST APIs
- JSON
- Python-dotenv
- Logging

## Project Features

- Fetches real-time weather information using the OpenWeather Current Weather API.
- Retrieves Air Quality Index (AQI) using the OpenWeather Air Pollution API.
- Uses latitude and longitude from the Weather API to fetch air pollution data.
- Converts temperature from Kelvin to Celsius.
- Displays weather conditions, temperature, and AQI status.
- Handles API errors, timeouts, and connection issues.
- Manages API keys securely using environment variables.
- Uses logging to track application activities and errors.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd YOUR_PROJECT_FOLDER
```

### 3. Install Required Libraries

```bash
pip install requests python-dotenv
```

### 4. Configure the API Key

- Create a `.env` file in the project root directory.
- Add your OpenWeather API key:

```env
API_KEY=your_openweather_api_key
```

**Note:** Replace `your_openweather_api_key` with your actual API key.

### 5. Run the Project

```bash
python weather.py
```

Replace `weather.py` with your actual Python filename if it is different.

## How It Works

1. The user enters a city name.
2. The application sends a request to the OpenWeather Current Weather API.
3. The API returns weather details, temperature, latitude, and longitude.
4. The application uses latitude and longitude to call the Air Pollution API.
5. The Air Pollution API returns the Air Quality Index (AQI).
6. The application converts temperature from Kelvin to Celsius.
7. Finally, it displays the weather report and AQI status.

## Air Quality Index (AQI) Levels

| AQI Value | Air Quality |
|---|---|
| 1 | Good |
| 2 | Fair |
| 3 | Moderate |
| 4 | Poor |
| 5 | Very Poor |

*Note: These AQI levels follow the OpenWeather API's 1–5 scale.*

## Project Files

- `weather.py` – Main Python application.
- `.env` – Stores the OpenWeather API key locally.
- `weather.log` – Stores application logs.
- `README.md` – Project documentation.

## Error Handling

The project handles different errors, including:

- Invalid API key.
- Invalid city name or HTTP errors.
- Request timeout.
- Internet connection issues.
- Missing or unexpected API response data.

## Security

- API keys are stored in a `.env` file.
- Environment variables are loaded using Python-dotenv.
- The `.env` file should not be uploaded to GitHub.

Add the following to your `.gitignore` file:

```text
.env
__pycache__/
```

## Project Objective

The main objective of this project is to understand REST API integration, JSON data handling, Python exception handling, environment variables, and logging through a practical real-time weather and air quality application.