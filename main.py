from flask import Flask, request, abort, render_template_string
import time
import random

app = Flask(__name__)

with open("flygui.txt", "r", encoding="utf-8") as f:
    PROTECTED_SCRIPT = f.read()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>System Maintenance</title>
    <style>
        body { background: #000; color: #0f0; font-family: monospace; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .container { border: 1px solid #0f0; padding: 20px; box-shadow: 0 0 15px #0f0; }
        .blink { animation: blinker 1s linear infinite; }
        @keyframes blinker { 50% { opacity: 0; } }
    </style>
</head>
<body>
    <div class="container">
        <p>> Getting script...</p>
        <p>> STATUS: <span class="blink">searching among 100,000+ scripts</span></p>
    </div>
</body>
</html>
"""

@app.route('/fly-script')
def delivery():
    agent = request.headers.get('User-Agent', '')
    
    if "Roblox" not in agent:
        time.sleep(random.randint(15, 30)) 
        return render_template_string(HTML_TEMPLATE)

    time.sleep(2)
    return PROTECTED_SCRIPT

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)