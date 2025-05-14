# 🔐 AWS Hash Vault

A lightweight Flask API for securely storing and cracking password hashes using AWS Secrets Manager and John the Ripper.

## Features
- Flask API to submit hashes
- AWS Secrets Manager for secure storage
- Wordlist-based cracking on EC2
- Uses John the Ripper Jumbo

## Project Structure
```
aws_hash_cracker_project/
├── api.py                # Flask API to receive and store hashes
├── md5.txt               # Example hash file
├── crack_result_log.txt  # Final cracked output log
├── screenshots/          # Screenshots (add yours here)
└── README.md             # Project instructions
```

## Setup Steps (Summary)
1. Launch EC2 (Ubuntu t2.micro)
2. Set up Python & Flask (venv, pip install flask boto3)
3. Attach IAM role with SecretsManager access
4. Run `api.py` on port 5000
5. Submit hash from PowerShell
6. Retrieve hash using boto3
7. Crack it with John the Ripper

## Final Result
Hash cracked: `5f4dcc3b5aa765d61d8327deb882cf99`
Password found: `password`

---
Made by Karol • For educational use only 🔐
