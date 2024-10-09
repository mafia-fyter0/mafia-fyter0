from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Define a function to run a script
def run_script(script_name):
    # Replace this with your script running logic
    print(f"Running script: {script_name}")

# Define a route to run a script
@app.route('/run_script', methods=['POST'])
def run_script_route():
    script_name = request.json['script_name']
    run_script(script_name)
    return jsonify({'message': f"Script {script_name} run successfully"})

# Define a function to schedule a script
def schedule_script(script_name, interval):
    schedule.every(interval).seconds.do(run_script, script_name)

# Define a route to schedule a script
@app.route('/schedule_script', methods=['POST'])
def schedule_script_route():
    script_name = request.json['script_name']
    interval = request.json['interval']
    schedule_script(script_name, interval)
    return jsonify({'message': f"Script {script_name} scheduled to run every {interval} seconds"})

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
