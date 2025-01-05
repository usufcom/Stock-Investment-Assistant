# Stock and Investment-Assistant
A real-time stock quote and investment assistant built using OpenAI's API and the Finnhub API. This project allows users to interact with a chatbot that can fetch stock prices and offer investment advice based on current market conditions.

## Features

- Get real-time stock quotes for different stock tickers (e.g., TSLA, AAPL, MSFT).
- Receive investment advice based on stock price trends.
- User-friendly web interface to interact with the assistant.
- Option to press the "Send" button or use the "Enter" key to submit queries.

## Technologies Used

- **OpenAI API**: For conversational AI and generating responses.
- **Finnhub API**: For fetching real-time stock quotes.
- **HTML/CSS**: For the web interface.
- **JavaScript**: For handling user input and interacting with the APIs.
- **Node.js (optional)**: If using a backend server to handle requests.

## Setup

### Prerequisites

- Node.js and npm (for server-side setup)
- OpenAI API key
- Finnhub API key

### Steps to Run Locally

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/stock-quote-assistant.git
   cd stock-quote-assistant
   ```

2. Install necessary dependencies (if you are using a backend server):

```bash
npm install
```

3. Replace the placeholders in the script files:
In the Python code, replace YOUR_OPENAI_API_KEY and YOUR_FINNHUB_API_KEY with your actual API keys.

4. To run the project locally, open the index.html file in your browser:
Simply double-click on the index.html file, or If you're using a Node.js server, run the following:

```bash
node server.js
```
Then open your browser and go to http://localhost:3000.

### How to Use
1. Open the web page in your browser.
2. Type a stock ticker (e.g., TSLA, AAPL) or ask for investment advice in the input field.
3. Click the "Send" button or press "Enter" to submit the query.
4. The assistant will respond with the stock quote or investment advice based on the data it fetches from Finnhub.

### Example Queries
1. "What is the current stock price of TSLA?"
2. "Give me the stock quote for Apple."
3. "What can you advise me about investing in Microsoft?"
4. "Based on the current stock quote of Apple, what short advice can you give me on investing in General Electric?"

### License
This project is open source and available under the MIT License.

### Acknowledgements
- OpenAI API for providing the conversational AI service.
- Finnhub API for providing real-time stock data.
- Inspiration from AI Automation Agency Hub and Liam Ottley.
