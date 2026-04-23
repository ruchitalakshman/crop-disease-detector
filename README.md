AI Crop Disease Detector

An intelligent web application that detects crop diseases from leaf images using a deep learning model. This project demonstrates how machine learning can assist farmers and researchers in identifying plant diseases quickly and efficiently.

Features

* Upload crop images for analysis
* AI-powered disease detection
* Confidence score visualization
* Identifies healthy vs diseased plants
* Fast and simple web interface


Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (FastAPI / Lambda)
* **Machine Learning:** PyTorch
* **Cloud Services:** AWS SageMaker, S3, Lambda


Project Structure

.
├── index.html        # Frontend UI
├── backend/          # API / ML integration
├── notebook/         # Model training & experimentation
```

---

Important Note (About Live Prediction)

The current deployed version of this project uses a **demo prediction system**.

The actual AWS SageMaker endpoint has been **disabled**.

### Why?

AWS SageMaker endpoints are **not free** and incur continuous charges while running.
To avoid unnecessary costs, the endpoint used for real-time predictions has been stopped/deleted.

How Real Prediction Works (When Enabled)

1. Image is uploaded from the frontend
2. Converted to base64 format
3. Sent to backend API
4. API forwards request to SageMaker endpoint
5. Model returns prediction + confidence
6. Result displayed on UI

How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/ruchitalakshman/crop-disease-detector.git
   ```

2. Open `index.html` in your browser


Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

License

This project is for educational and demonstration purposes.

Author

Ruchita L
Computer Science Engineering Student

