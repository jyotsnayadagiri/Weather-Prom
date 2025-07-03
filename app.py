from flask import Flask
import random
import prometheus_client
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUESTS = Counter('app_requests_total', 'Total API Requests')

@app.route('/weather')
def weather():
    REQUESTS.inc()
    temperature = random.randint(20, 40)
    return {"temperature": temperature, "unit": "Celsius"}

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
