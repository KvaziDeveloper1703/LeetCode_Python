'''
Initially, your bank account balance is 100 dollars.

You are given an integer purchaseAmount, which represents the cost of a purchase in dollars.

When making the purchase, the value of purchaseAmount is first rounded to the nearest multiple of 10.

Let this rounded value be called roundedAmount.

Then, roundedAmount dollars are subtracted from your bank account balance.

Return the final balance of your bank account after the purchase.

Examples:
Input: purchaseAmount = 9
Output: 90

Input: purchaseAmount = 15
Output: 80

Изначально баланс вашего банковского счёта составляет 100 долларов.

Вам дано целое число purchaseAmount, которое обозначает стоимость покупки в долларах.

При совершении покупки значение purchaseAmount сначала округляется до ближайшего числа, кратного 10.

Обозначим это значение как roundedAmount.

Затем из вашего банковского счёта вычитается roundedAmount долларов.

Необходимо вернуть итоговый баланс банковского счёта после покупки.

Примеры:
Ввод: purchaseAmount = 9
Вывод: 90

Ввод: purchaseAmount = 15
Вывод: 80
'''

def account_balance_after_purchase(purchaseAmount: int) -> int:
    roundedAmount = ((purchaseAmount + 5) // 10) * 10
    return 100 - roundedAmount