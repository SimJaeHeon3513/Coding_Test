# 브리지 카드 게임 (Bridge)

## 문제 설명

카드 게임의 일종인 브리지 게임은 52장의 표준 카드 덱을 4명의 플레이어에게 공평하게 나눠 준다.  
즉, 각 플레이어는 13장의 카드를 받는다.

숙련된 플레이어는 나눠진 카드를 그대로 가지고 플레이할 수 있지만, 대부분의 일반 플레이어는 카드를 먼저 **슈트별로**, 그리고 **슈트 내 순위별로** 정렬한다.

---

## 카드 순서

슈트의 고정된 순위는 없지만, 색상을 번갈아 배치하는 것이 유용하므로 다음과 같은 순서를 가정한다.

$$♣ < ◇ < ♠ < ♡$$

> 이제부터 클럽, 다이아몬드, 스페이드, 하트에 대해 각각 `C`, `D`, `S`, `H`를 사용한다.

슈트 내에서 에이스는 가장 높으므로 순서는 다음과 같다.

$$2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < T < J < Q < K < A$$

---

## 플레이어 구성 및 카드 배분

네 명의 플레이어는 `North`, `West`, `South`, `East`의 첫 글자, 즉 **나침반의 방위**로 이름을 붙여 구분한다.

```
        N
        |
  W ----+---- E
        |
        S
```

- 한 명의 플레이어가 **딜러**로 지정된다.
- **딜러의 왼쪽(시계 방향)** 플레이어부터 각 플레이어에게 한 장씩 카드를 나눠준다.
- 마지막 카드는 딜러 자신이 가지게 된다.
- 이 과정을 **13번 반복**한다.

각 플레이어는 받은 13장의 카드를 정렬한 후, 자기의 카드를 순서대로 출력한다.

---

## 입력

- 표준 입력을 통해 데이터를 읽어온다.
- 입력은 **일련의 카드 딜**로 구성된다.
- 입력의 첫째 줄에는 **딜러를 나타내는 문자** (`N`, `E`, `S`, `W`)가 주어진다.
- 52장의 카드 덱에 대한 정보가 **두 줄**에 걸쳐 주어진다.  
  *(52장의 카드를 한 줄로 인쇄하기엔 용지 폭이 너무 좁아 두 줄로 인쇄한 것)*
- 입력의 마지막은 `#`이 적힌 줄로 표시된다.

---

## 출력

- 입력의 각 딜에 대해 출력은 **네 줄**로 구성된다.
- 각 줄은 각 플레이어가 받은 카드를 정렬한 것이다.
- 각 입력에 대해, 플레이어 **`S`, `W`, `N`, `E` 순**으로 자기가 받은 카드를 정렬된 순서로 출력한다.

---

## 제한 조건

- 프로그램 언어는 `C`, `C++`, `Java`, `Python`으로 한다.

---

## 예제

### 입력
```
N
CQDTC4D8S7HTDAH7D2S3D6C6S6D9S4SAD7H2CKH5D3CTS8C9H3C3
DQS9SQDJH8HAS2SKD4H4S5C7SJC8DKC5C2CAHQCJSTH6HKH9D5HJ
E
SQDJH8HAS2SKD4H4S5C7SJC8DKC5C2CAHQCJSTH6HKH9D5HJDQS9
D8S7HTDAH7D2S3D6C6S6D9S4SAD7H2CKH5D3CTS8C9H3C3CQDTC4
#
```

### 출력
```
S: C3 C5 C7 CT CJ D9 DT DJ S3 SK H2 H9 HT
W: C2 C4 CK D4 D5 D6 DQ DA S4 S8 ST SJ H8
N: C6 C8 C9 CA D8 S9 SA H4 H5 H6 H7 HJ HA
E: CQ D2 D3 D7 DK S2 S5 S6 S7 SQ H3 HQ HK
S: C3 CT D9 DQ DK S2 S3 S5 SQ H2 HT HQ HK
W: C5 C7 CJ CQ CK D6 DJ DA S4 S8 S9 SK H9
N: C2 C6 C9 D4 D5 D8 DT ST SJ SA H5 H7 H8
E: C4 C8 CA D2 D3 D7 S6 S7 H3 H4 H6 HJ HA
```

---

## 풀이 (Python)

```python
SUITS = "CDSH"
CLOCKWISE = "NESW"
RANK = "23456789TJQKA"

def card_key(card):
    return SUITS.index(card[0]) * 100 + RANK.index(card[1])

while True:
    d = input().strip()
    if d == "#":
        break

    raw = ""
    while len(raw) < 104:
        raw += input().strip()

    cards = [raw[i:i+2] for i in range(0, 104, 2)]

    hands = {p: [] for p in "NESW"}
    start = (CLOCKWISE.index(d) + 1) % 4

    for i, card in enumerate(cards):
        hands[CLOCKWISE[(start + i) % 4]].append(card)

    for p in ["S", "W", "N", "E"]:
        hands[p].sort(key=card_key)
        print(f'{p}: {" ".join(hands[p])}')
```
