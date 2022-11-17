text = input()
N, all_summ = int(text[:4]), int(text[4:])
cheque = []
cheque_summs = []
prices = []

for _ in range(N):
    cheque.append(input())

for i in cheque:
    product_price = i[:7]
    product_count = i[8:12]
    prices.append(int(i[13:]))

    char_index = 6
    while char_index > -1:
        if product_price[char_index] == ' ':
            product_price = product_price[:len(product_price) - 1]
        else:
            break
        char_index -= 1

    char_index = 3
    while char_index > -1:
        if product_count[char_index] == ' ':
            product_count = product_count[:len(product_count) - 1]
        else:
            break
        char_index -= 1

    cheque_summs.append(int(product_price) * int(product_count))

print(all_summ - sum(cheque_summs))
for i in range(N):
    if cheque_summs[i] != prices[i]:
        print(i + 1, end=" ")
