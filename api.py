from flask import Flask, request
import boto3, uuid

app = Flask(__name__)
client = boto3.client('secretsmanager', region_name='us-east-1')

@app.route('/submit-hash', methods=['POST'])
def submit_hash():
    data = request.get_json()
    hash_val = data.get('hash')
    hash_id = f"hash-{uuid.uuid4()}"
    client.create_secret(Name=hash_id, SecretString=hash_val)
    return {"status": "received", "id": hash_id}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
