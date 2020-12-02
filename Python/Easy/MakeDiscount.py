def MakeDiscount(prices,discount):
    max_prices = int(max(prices)*(100-discount)/100)
    prices.remove(max(prices))
    prices.append(max_prices)
    print(prices)
    return sum(prices)


prices = [int(input(str("Saisir prix "+ str(i) + " : "))) for i in range(int(input("saisir le nombre de prix : ")))]
discount= int(input())
print(MakeDiscount(prices,discount))