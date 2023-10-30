## shift+alt+e로 특정 라인만 실행 가능

# 5.1. pybithumb
# 5-1-1. 가상화폐 티커 목록 얻기
import pybithumb

tickers = pybithumb.get_tickers()
print(tickers)
print(len(tickers))
print(type(tickers))

# 5-1-2. 현재가 얻기
import pybithumb
import time

price = pybithumb.get_current_price("BTC")
print(price)

while True:
    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(1)

## 모든 가상 화폐의 현재가 출력
tickers = pybithumb.get_tickers()
for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(ticker, price)
    time.sleep(0.1)

# 5-1-3. 거래소 거래 정보
## 24시간 동안의 시가/고가/저가/종가(현재가)/거래량
import pybithumb

detail = pybithumb.get_market_detail("BTC")
print(detail)
print(type(detail))

# 5-1-4. 호가
## 매도호가: 가상화폐를 팔고자 하는 사람이 제시한 가격과 수량, ask
## 매수호가: 가상화폐를 사고자 하는 사람이 제시한 가격과 수량, bid
import pybithumb

# orderbook 딕셔너리의 키: [timestamp, payment_currency, order_currency, bids, asks]
orderbook = pybithumb.get_orderbook("BTC")
print(orderbook)

for k in orderbook:
    print(k)

print(orderbook['payment_currency']) # KRW -> 빗썸 가상화페 거래시 원화 결제만 지원
print(orderbook['order_currency']) # BTC -> 조회한 가상화폐의 티커

## datetime 사용하기
import pybithumb
import datetime

orderbook = pybithumb.get_orderbook("BTC")
ms = int(orderbook['timestamp'])

dt = datetime.datetime.fromtimestamp(ms/1000)
print(dt)

# 매도호가와 매수호가의 가격과 잔고 출력하기
import pybithumb

orderbook = pybithumb.get_orderbook("BTC")
bids = orderbook['bids']
asks = orderbook['asks']
print(bids)
print(asks)

for bid in bids:
    price = bid['price']
    quant = bid['quantity']
    print("매수호가: ", price, "매수잔량: ", quant)

for ask in asks:
    price = ask['price']
    quant = ask['quantity']
    print("매도호가: ", price, "매도잔량: ", quant)

# 5-1-5. 여러 가상화폐에 대한 정보 한번에 얻기
## API는 1초에 95회 요청 가능
import pybithumb

# ALL로 한 번에 모든 암호 화폐의 가격을 가져옴
all = pybithumb.get_current_price("ALL")
for k, v in all.items():
    print(k, v)

# opening_price: 시가 00시 기준
# closing_price: 종가 00시 기준
# min_price: 저가 00시 기준
# max_price: 고가 00시 기준
# acc_trade_value: 거래량 00시 기준
# units_traded: 거래량 00시 기준
# prev_closing_price: 전일종가
# units_traded_24H: 최근 24시간 거래량
# acc_trade_value_24H: 최근 24시간 거래금액
# fluctate_24H: 최근 24시간 변동가
# fluctate_rate_24H: 최근 24시간 변동률

import pybithumb

tickers = pybithumb.get_tickers()
all = pybithumb.get_current_price("ALL")

for ticker in tickers:
    print(ticker, all[ticker]['closing_price'])

# 5-1-6. 예외 처리
## KeyError: 'open1' 에러 상황
price = {"open": 100, "high": 150, "low": 90, "close": 130}
print("point-1")
open = price["open1"]
print("point-2")

## KeyError: 'open1' 에러 해결
price = {"open": 100, "high": 150, "low": 90, "close": 130}
print("point-1")
try:
    open = price["open1"]
except:
    pass
print("point-2")

## get_current_price() 메서드가 None 값을 리턴하는 경우 에러 발생
import pybithumb
import time

while True:
    price = pybithumb.get_current_price("BTC")
    print(price/10)
    time.sleep(0.2)

## get_current_price() 메서드가 None 값을 리턴하는 경우 에러 해결
### 1. if문
import pybithumb
import time
while True:
    price = pybithumb.get_current_price("BTC")
    if price is not None:
        print(price/10)
    time.sleep(0.2)

### 2. try-except문
import pybithumb
import time
while True:
    price = pybithumb.get_current_price("BTC")
    try:
        print(price/10)
    except:
        print("에러 발생", price)
    time.sleep(0.2)

# [연습문제] 모든 가상화폐의 24시간 변동률을 출력하세요.
import pybithumb

tickers = pybithumb.get_tickers()
all = pybithumb.get_current_price("ALL")

for ticker in tickers:
    print(ticker, all[ticker]['fluctate_rate_24H'])