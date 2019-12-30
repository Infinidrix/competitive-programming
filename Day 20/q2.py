def best_buy(p, prices):
    count_items = 0
    prices.sort()
    while len(prices) >= 3:
        
        cheapest = prices[0]
        prices.pop(0)
        sec_cheapest = prices[0]
        prices.pop(0)
        thrid_cheap = prices[0]
        
        if p - (sec_cheapest) >= thrid_cheap or (p - cheapest < thrid_cheap and p - (sec_cheapest) >= 0):
            count_items += 2
            p -= sec_cheapest
        elif p >= cheapest:
            count_items += 1
            p -= cheapest
            prices.insert(0, sec_cheapest)
        else:
            break
            
    if 0 < len(prices) < 3:
        if len(prices) == 2 and p >= max(prices):
            count_items += 2
        elif p >= min(prices):
            count_items += 1
    
    return count_items


useless = int(input())
for i in range(useless):
    n, p, k = (int(i) for i in input().split())
    price_list = [int(i) for i in input().split()]
    print(best_buy(p, price_list))
