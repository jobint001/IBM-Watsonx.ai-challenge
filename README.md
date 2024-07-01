# IBM-Watsonx.ai-challenge
Leverages Watsonx.ai, specifically the IBM Granite model, to analyze and summarize customer reviews, providing city planners and administrators with actionable insights.

## Prerequisites

- Python 3.7 or higher
- Node.js 14.x or higher
- npm 6.x or higher
- IBM Watsonx.ai credentials

## Installation

### Backend

1. **Clone the repository:**
    ```bash
    git clone https://github.com/jobint001/IBM-Watsonx.ai-challenge.git
    cd IBM-Watsonx.ai-challenge/backend
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv ibm
    source ibm/Scripts/activate (Windows)
    source ibm/bin/activate (MacOS/Linux)
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Frontend

1. **Navigate to the frontend directory:**
    ```bash
    cd ../frontend/urban-forum
    ```

2. **Install the required packages:**
    ```bash
    npm install
    ```

## Configuration

### Backend

- Create a `.env` file in the `backend` directory with the necessary environment variables. For example:
    ```
    WATSON_API_KEY=your_watson_api_key
    WATSON_URL=your_watson_url
    ```

### Frontend

- Update the configuration in the `vite.config.js` file if necessary.

## Running the Code

### Backend

1. **Activate the virtual environment (if not already activated):**
    ```bash
    source ibm/Scripts/activate (Windows)
    source ibm/bin/activate (MacOS/Linux)
    ```

2. **Run the backend server:**
    ```bash
    python run.py
    ```

### Frontend

1. **Navigate to the frontend directory:**
    ```bash
    cd ../frontend/urban-forum
    ```

2. **Run the frontend development server:**
    ```bash
    npm run dev
    ```

## Usage

- Access the application through the frontend server (default is `http://localhost:3000`).
- Use the various features of the application to interact with Chennai's public transportation system.

## Troubleshooting

- **Virtual Environment Issues:** Ensure that the virtual environment is properly activated before running backend commands.
- **Package Installation Errors:** Ensure that you have the correct versions of Python, Node.js, and npm installed. Check the `requirements.txt` and `package.json` for specific version requirements.
- **Environment Variables:** Make sure all necessary environment variables are correctly set in the `.env` file.
- **Server Issues:** Check the terminal output for any error messages when starting the backend or frontend servers. Ensure that the servers are running on the specified ports.
