def main():
    #write your code below this line
    acct = Account("Matthews account", 1000)
    acct.withdraw(100)
    print(acct.balance)
    acct = Account("My account", 0)
    acct.deposit(100)
    print(acct.balance)
    


if __name__ == '__main__':
    from account import Account
    main()
else:
    from src.account import Account