\# AtmoSync – Micro-Climate Arbitrage Analytics



AtmoSync is a Python-based micro-climate analytics application designed to analyze environmental sensor data and estimate the impact of changing climate conditions on perishable goods during transportation and storage.



\## Features



\- \*\*Climate Data Analysis:\*\* Analyze temperature and humidity readings collected from sensors.

\- \*\*IoT Sensor Simulation:\*\* Generate simulated sensor readings for testing and analysis.

\- \*\*Spoilage Prediction:\*\* Estimate potential spoilage risks using environmental data.

\- \*\*Interactive Dashboard:\*\* Visualize sensor readings and analytics through a Streamlit application.

\- \*\*Shipment Monitoring:\*\* Work with shipment-related data to understand environmental conditions during transit.



\## Project Structure



```text

AtmoSync/

│

├── app.py

├── iot\_simulator.py

├── spoilage\_model.py

├── sensor\_data.csv

├── sensor\_data (1).csv

├── requirements.txt

├── req.txt

├── README.md

└── AtmoSync/

&#x20;   ├── analytics/

&#x20;   ├── simulator/

&#x20;   └── tests/

```



\## Technologies Used



\- Python

\- Streamlit

\- Pandas

\- NumPy

\- Data Visualization Libraries

\- Machine Learning / Data Analysis



\## Installation



1\. Clone the repository:



&#x20;  ```bash

&#x20;  git clone https://github.com/deekshi224-tec/AtmoSync.git

&#x20;  ```



2\. Navigate to the project directory:



&#x20;  ```bash

&#x20;  cd AtmoSync

&#x20;  ```



3\. Install the required dependencies:



&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```



\## Run the Application



Start the Streamlit dashboard:



```bash

streamlit run app.py

```



\## Run the IoT Simulator



```bash

python iot\_simulator.py

```



\## Project Goal



The goal of AtmoSync is to use environmental sensor data and analytics to help monitor micro-climate conditions, identify potential spoilage risks, and support better decisions in perishable-goods transportation and storage.



\## Future Enhancements



\- Real-time IoT sensor integration.

\- Improved spoilage prediction models.

\- Automated alerts for unsafe temperature and humidity conditions.

\- Expanded shipment analytics and reporting.



\## Contributors



Developed collaboratively as a project team.



