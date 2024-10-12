from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    command = data['command']
    try:
        # 处理输入的命令
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout if result.stdout else result.stderr
        if result.returncode != 0:
            raise Exception(output)
    except Exception as e:
        return jsonify({'error': f"Command failed: {str(e)}"})

    return jsonify({'output': output})



if __name__ == '__main__':
    app.run(debug=True,port=10000, host='0.0.0.0')
