# Prometheus and Grafana Demo Application

This repository contains a Python application designed to demonstrate the functionality of Prometheus and Grafana. The application exposes various Prometheus metrics and produces JSON logs to show how these tools can be used to monitor and visualize application performance and behavior.

## Features

- **Prometheus Metrics**: The application exposes several types of Prometheus metrics, including counters, gauges, summaries, and histograms.
- **JSON Logging**: The application produces logs in JSON format, suitable for use with Loki and Grafana for log visualization and filtering.
- **Realistic Simulation**: Metrics and logs are generated in a realistic manner to replicate typical use cases for monitoring an application's performance.

## Metrics Exposed

- **Total Requests** (`app_requests_total`): Counter for the total number of requests processed.
- **In-Progress Requests** (`app_in_progress_requests`): Gauge for the number of requests currently being processed.
- **Request Duration** (`app_request_duration_seconds`): Summary for the duration of request processing.
- **Request Size** (`app_request_size_bytes`): Histogram for the size of requests, with specified buckets.

## Logging

- The application uses the `logging` library to produce logs in JSON format.
- Each log entry includes details such as `request_id`, `status`, `duration`, `size`, and `timestamp`.

## Getting Started

### Prerequisites

- Python 3.11+
- Poetry

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/prometheus-demo.git
    cd prometheus-demo
    ```

2. Install the required dependencies using Poetry:
    ```sh
    poetry install
    ```

### Running the Application

1. Start the application:
    ```sh
    poetry run prometheus-demo
    ```

2. The Prometheus metrics will be exposed at `http://localhost:8000/metrics`.

3. The application will continuously generate requests asynchronously, producing metrics and logs.

### Docker

You can also run the application using Docker. Ensure you have Docker installed on your system.

1. Build the Docker image:
    ```sh
    docker build -t prometheus-demo .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8000:8000 prometheus-demo
    ```

## Visualization with Grafana

- **Prometheus**: Add Prometheus as a data source in Grafana and import the metrics from `http://localhost:8000/metrics`.
- **Loki**: Add Loki as a data source in Grafana to visualize and filter the JSON logs produced by the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This repository aims to provide a practical example of how to use Prometheus, Grafana, and Loki together to monitor and visualize application metrics and logs. Happy monitoring!
