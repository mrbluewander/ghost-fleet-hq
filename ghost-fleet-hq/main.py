import requests
import datetime

def fetch_market_data():
    try:
        response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", timeout=5)
        data = response.json()
        btc_price = float(data['price'])
        return f"${btc_price:,.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

def lobster_operation():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    market_info = fetch_market_data()
    
    print("\n=============================================")
    print(f" WANXIANG BASE - LOBSTER CORE ONLINE")
    print(f" TIME: {current_time}")
    print(f" REAL-TIME BTC PRICE: {market_info}")
    print("=============================================\n")

    with open("LOBSTER_LOG.md", "a", encoding="utf-8") as f:
        f.write(f"### LOG - {current_time}\n")
        f.write(f"- BTCUSDT = {market_info}\n")
        f.write(f"- STATUS: ACTIVE\n\n")
        
    try:
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>WANXIANG BASE COMMAND</title>
    <style>
        body {{ background-color: #111; color: #00ff00; font-family: monospace; padding: 50px; }}
        .container {{ border: 2px solid #00ff00; padding: 20px; border-radius: 5px; max-width: 600px; margin: 0 auto; }}
        h1 {{ color: #fff; text-align: center; }}
        .data {{ font-size: 24px; text-align: center; margin: 20px 0; color: #ffcc00; }}
        .time {{ text-align: right; color: #888; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>WANXIANG BASE COMMAND</h1>
        <hr style="border-color: #00ff00;">
        <p><strong>LOBSTER REBORN:</strong> HTML REFRESH SUCCESSFUL.</p>
        <div class="data">Bitcoin (BTC): {market_info}</div>
        <div class="time">LAST UPDATE: {current_time}</div>
    </div>
</body>
</html>"""
        with open("index.html", "w", encoding="utf-8") as h:
            h.write(html_content)
        print("[SUCCESS] index.html updated successfully!")
    except Exception as e:
        print(f"[ERROR] HTML update failed: {str(e)}")

if __name__ == "__main__":
    lobster_operation()