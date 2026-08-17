import json
from datetime import datetime, timezone

import yfinance as yf


symbols = ["QQQM", "TQQQ", "IQQ", "SPYM", "JEPQ"]

data = {
    "updated": datetime.now(timezone.utc).isoformat(),
    "exchangeRate": 0,
    "stocks": {}
}


# 주가 가져오기
for symbol in symbols:
    try:
        ticker = yf.Ticker(symbol)

        price = ticker.fast_info["last_price"]

        data["stocks"][symbol] = {
            "price": round(float(price), 4)
        }

    except Exception as e:
        print(f"{symbol} 오류: {e}")

        data["stocks"][symbol] = {
            "price": 0
        }


# USD/KRW 환율
try:
    fx = yf.Ticker("KRW=X")
    exchange_rate = fx.fast_info["last_price"]

    data["exchangeRate"] = round(float(exchange_rate), 4)

except Exception as e:
    print(f"환율 오류: {e}")


# data.json 저장
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


print(json.dumps(data, ensure_ascii=False, indent=2))
