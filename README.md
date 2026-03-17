# 🚀 AWS Onboarding AI Assistant

An AI-powered chatbot that helps CloudOps teams identify **infrastructure blockers** while onboarding new applications into AWS.

---

## 📌 Problem Statement

During application onboarding in AWS environments, teams often face:

* Security Group conflicts
* Port already in use
* Subnet exhaustion
* Load balancer rule conflicts
* Missing IAM permissions

These issues reduce productivity and increase onboarding time.

---

## 💡 Solution

This project builds an AI assistant using:

* AWS infrastructure data
* LLM reasoning
* Chat-based interface

It analyzes existing infrastructure and provides:

✅ Blockers
✅ Conflicts
✅ Suggested solutions

---

## 🏗️ Architecture

```
User Input
   ↓
Streamlit UI
   ↓
LangChain + LLM
   ↓
Infra Context (JSON)
   ↓
AWS APIs (boto3)
```

---

## 🧰 Tech Stack

* Python
* Streamlit
* LangChain
* OpenAI
* FAISS
* Boto3

---

## 📁 Project Structure

```
aws-onboarding-ai/
│
├── app.py
├── aws_scanner.py
├── rag_engine.py
│
├── infra_data/
│   ├── security_groups.json
│   ├── subnets.json
│   ├── load_balancers.json
│
├── prompts/
│   └── onboarding_prompt.txt
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repo

```
git clone https://github.com/your-username/aws-onboarding-ai.git
cd aws-onboarding-ai
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_openai_key
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=ap-south-1
```

---

## 🔐 AWS Configuration

### Create IAM User

* Go to AWS Console → IAM
* Create user
* Attach policy:

```
ReadOnlyAccess
```

* Generate Access Key

---

## ▶️ Run the Project

### Step 1: Collect AWS Infra

```
python aws_scanner.py
```

### Step 2: Run Chatbot

```
streamlit run app.py
```

---

## 🧪 Example Input

```
Application Name: payment-service
Environment: prod
Region: ap-south-1
Port: 8080
Services: ALB, ECS
```

---

## 📊 Example Output

```
⚠ Blockers:
- Port conflict in SG
- ALB rule overlap

✅ Solutions:
- Use port 8081
- Create new SG
```

---

## 🐞 Errors Faced & Fixes

### 1. NoRegionError

**Error:**

```
You must specify a region
```

**Fix:**

```
AWS_DEFAULT_REGION=ap-south-1
```

---

### 2. Missing Dependencies

**Error:**

```
ImportError: tabulate
```

**Fix:**

```
pip install tabulate
```

---

### 3. LangChain Import Errors

**Issue:**
Modules moved to new packages

**Fix:**
Use:

```
langchain_openai
langchain_community
langchain_text_splitters
```

---

### 4. Excel Data Mismatch

**Issue:**
Date format mismatch

**Fix:**
Standardize:

```
df[col] = df[col].dt.strftime("%d-%m-%Y")
```

---

## 🚀 Future Enhancements

* Terraform validation
* Cost estimation
* Security compliance checks
* Auto AWS scanning
* Real-time alerts

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Karthikraja
