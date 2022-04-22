# If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week, how much would your $ 1000 reach at the end of the 7th day?

deposited_money = 1000
fixed_profit_rate = 0.07
number_period = 7
total_money = deposited_money * (1 + fixed_profit_rate) ** number_period
print(f"At the end of the 7th day total capital is ${total_money}")