from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
app = FastAPI()
FastAPIInstrumentor().instrument_app(app)
@app.get("/")
def home():    
    return {
        "application": "DNB Banking API",
        "version": "1.0",
        "status": "Running",
        "message": "Hello DNB! Welcome to OpenTelemetry."
        }
@app.get("/customer")
def cust():
    return {
        "customer": "John Doe",
        "account": "123456789",
        "balance": 1000.00,
        "currency": "USD"
        }
@app.get("/transaction")
def transaction():
    return {
        "transaction_id": "987654321",
        "amount": 250.00,
        "currency": "USD",
        "status": "Completed"
        }
@app.get("/loan")
def loan():
    return {
        "loan_id": "555555555",
        "amount": 5000.00,
        "currency": "USD",
        "status": "Approved"
        }
@app.get("/investment")
def investment():
    return {
        "investment_id": "111111111",
        "amount": 1000.00,
        "currency": "USD",
        "status": "Active"
        }

