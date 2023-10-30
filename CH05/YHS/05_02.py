## shift+alt+e로 특정 라인만 실행 가능

# 5.2. 상승장 알리미 (1)
# 5-2-1. 이동평균을 사용한 상승장/하락장 구분
## 종가의 이동평균보다 현재가가 높다면 상승장, 그렇지 않다면 하락장


# 5-2-2. 거래소 과거 시세 얻어오기
import pybithumb

## get_ohlcv는 웹스크래핑으로 일봉 데이터를 가져옴
btc = pybithumb.get_ohlcv("BTC")
print(btc)

## 데이터프레임에서 종가('close')를 가져옴
close = btc['close']
print(close)


# 5-2-3. 이동평균 계산하기
import pybithumb

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']

## 5일 이동평균선 세 개
print((close[0] + close[1] + close[2] + close[3] + close[4])/5)
print((close[1] + close[2] + close[3] + close[4] + close[5])/5)
print((close[2] + close[3] + close[4] + close[5] + close[6])/5)

## 데이터프레임 메서드로 이동평균 자동 계산
import pybithumb

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']

## 5일씩 모든 데이터를 그룹화
window = close.rolling(5)

## 그룹화된 값의 평균을 구함
ma5 = window.mean()
print(ma5)


# 5-2-4. 상승장/하락장 구분하는 함수 구현하기
import pybithumb

df = pybithumb.get_ohlcv("BTC")
ma5 = df['close'].rolling(window=5).mean()
last_ma5 = ma5[-2]

cur_price = pybithumb.get_current_price('BTC')

if cur_price > last_ma5:
    print("상승장")
else:
    print("하락장")


# 5-2-5. 가상화폐별 상승장/하락장 판단하기
## 비트코인 상승장/하락장 판단
import pybithumb

def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(5).mean()
    last_ma5 = ma5[-2]
    cur_price = pybithumb.get_current_price(ticker)

    if cur_price > last_ma5:
        return True
    else:
        return False

is_bull = bull_market("BTC")
if is_bull:
    print("비트코인 상승장")

## 모든 가상화폐 상승장/하락장 판단
import pybithumb

def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(5).mean()
    last_ma5 = ma5[-2]
    cur_price = pybithumb.get_current_price(ticker)

    if cur_price > last_ma5:
        return True
    else:
        return False

tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = bull_market(ticker)
    if is_bull:
        print(ticker, " 상승장")
    else:
        print(ticker, " 하락장")

