from flask import Flask, render_template, request, jsonify
import openai
import finnhub
import json

app = Flask(__name__)

# Initialize OpenAI and Finnhub clients
client = openai.OpenAI(api_key="sk-xxxx")  # Replace with your API key
finnhub_client = finnhub.Client(api_key="xxxx")  # Replace with Finnhub API key

assistant_id = "asst_xxxxx"  # Replace with your Assistant ID

# Start a conversation thread
thread = client.beta.threads.create()
thread_id = thread.id

# Function to fetch stock quotes
def get_stock_quote(stock_ticker):
    stock_quote = finnhub_client.quote(stock_ticker)
    return json.dumps(stock_quote)

# Function to handle user messages
def send_message(prompt):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

        if run_status.status == "requires_action":
            tool_outputs = []
            for tool_call in run_status.required_action.submit_tool_outputs.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                if function_name == "get_stock_quote":
                    result = get_stock_quote(arguments['stock_ticker'])
                    tool_outputs.append({
                        "tool_call_id": tool_call.id,
                        "output": result
                    })

            client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread_id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )

        elif run_status.status == "completed":
            break

    messages = client.beta.threads.messages.list(thread_id=thread_id)
    if messages:
        return messages.data[0].content[0].text.value
    return "No response received."

# Flask route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# API route for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    user_prompt = request.json.get("prompt")
    response = send_message(user_prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
