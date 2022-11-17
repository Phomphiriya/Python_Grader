all_student = 30
money = 500

money_boy = 30
money_girl = 20
money_child = 10

count = 0

for boy in range(1,int(money/money_boy)+1):
    for girl in range(1,int(money/money_girl)+1):
        for child in range(int(money/money_child)+1):
            if boy+girl+child == all_student: ## x + y + z = 30
                if money_boy*boy + money_girl*girl + money_child*child == money: ## 30x + 20y + 10z = 500
                    count += 1
print(count)