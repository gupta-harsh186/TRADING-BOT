# Binance Futures Testnet Trading Bot

##  Overview

This project is a CLI-based Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

---

##  Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI-based input using argparse
* Structured modular code
* Logging of API requests and responses
* Error handling for invalid inputs and API failures

---

##  Tech Stack

* Python 3.10
* python-binance
* dotenv

---

##  Setup Instructions

### 1. Clone the repo

git clone <your-repo-link>
cd trading_bot

### 2. Create virtual environment

py -3.10 -m venv venv
.\venv\Scripts\Activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add API keys

Create a `.env` file:

API_KEY=your_key
API_SECRET=your_secret

---

## ▶️ Usage

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

### LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000

---

##  Output Example

* Order ID
* Status
* Executed Quantity
* Average Price

---

##  Logging

All API requests, responses, and errors are logged in:
bot.log

---

##  Assumptions

* Minimum order value must be ≥ 100 USDT (Binance rule)
* Only USDT-M futures supported
* Tested on Binance Futures Testnet

---

##  Status

Project completed and tested successfully with both MARKET and LIMIT orders.
