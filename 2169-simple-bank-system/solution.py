class Bank:

#Our balance array is 0 indexed, but accounts are numbered from 1->n, keep this in mind, as indicies coorespond to 0 --> n-1 in array, where n = len(balance)
    def __init__(self, balance: List[int]):
        self.accounts = balance
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        a1, a2 = account1 - 1, account2 - 1
        if self.isValid(a1, money) and self.isValid(a2):
            self.accounts[a1] -= money
            self.accounts[a2] += money
            return True
        return False



    def deposit(self, account: int, money: int) -> bool:
        account-=1
        if self.isValid(account):
            self.accounts[account] += money
            return True
        else:
            return False

        

    def withdraw(self, account: int, money: int) -> bool:
        account-=1
        if self.isValid(account, money):
            self.accounts[account] -= money
            return True
        else:
            return False

    def isValid(self, account: int , money: int = -1):
        if account in range(0, len(self.accounts)) and money <= self.accounts[account]:
            return True
        return False

        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
