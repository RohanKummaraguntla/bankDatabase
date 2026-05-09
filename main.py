import sqlite3

def setup_database():
    set = sqlite3.connect('bank.db')
    cursor = set.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        username TEXT, 
        password TEXT, 
        job TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts( 
        accountId INTEGER PRIMARY KEY AUTOINCREMENT,
        userId INTEGER,
        balance REAL
    )
    '''
    )

    set.commit()
    set.close()
def testinginfo():
    set = sqlite3.connect('bank.db')
    cursor = set.cursor()
    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM accounts")
    cursor.execute("INSERT INTO users (username, password, job) VALUES ('admin', '1234', 'admin')")
    cursor.execute("INSERT INTO users (username, password, job) VALUES ('user', '1111', 'customer')")
    cursor.execute("INSERT INTO accounts (userId, balance) VALUES (1, 1000)")
    cursor.execute("INSERT INTO accounts (userId, balance) VALUES (2, 500)")
    #cursor.execute("SELECT * FROM accounts")
    #print("Accounts table:", cursor.fetchall())
    set.commit()
    set.close()

def check_balance(accountId):
    set=sqlite3.connect('bank.db')
    cursor=set.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE accountId = ?", (accountId,))
    result=cursor.fetchone()
    set.close()
    #return result[0]

    if result is not None:
        return result[0]
    else:
        return None


def deposit(accountId, amount):
    set=sqlite3.connect('bank.db')
    cursor=set.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE accountId = ?", (amount, accountId))
    set.commit()
    set.close()


def withdraw(accountId, amount):
    set=sqlite3.connect('bank.db')
    cursor=set.cursor()
    cursor.execute("UPDATE accounts SET balance = balance - ? WHERE accountId = ?",(amount, accountId))
    set.commit()
    set.close()



def create_account(userId):
    set=sqlite3.connect('bank.db')
    cursor=set.cursor()
    cursor.execute("INSERT INTO accounts (userId, balance) VALUES (?, ?)",(userId, 0))
    set.commit()
    set.close()

def delete_account(accountId):
    set=sqlite3.connect('bank.db')
    cursor=set.cursor()
    cursor.execute("DELETE FROM accounts WHERE accountId = ?", (accountId,))
    set.commit()
    set.close()

def modify_account(accountId, new_balance):
    set = sqlite3.connect('bank.db')
    cursor = set.cursor()
    cursor.execute( "UPDATE accounts SET balance = ? WHERE accountId = ?", (new_balance, accountId) )
    set.commit()
    set.close()


#testing
def get():
    set=sqlite3.connect('bank.db')
    cursor=set.cursor()
    cursor.execute("SELECT accountId FROM accounts LIMIT 1")
    result =cursor.fetchone()
    set.close()
    return result[0]
if __name__ == "__main__":
    setup_database()
    #res = get()
    testinginfo()
    res = get()
    print("Before money ", check_balance(res))
    deposit(res, 100)
    print("After money", check_balance(res))
    withdraw(res, 50)
    print("After taken money out ", check_balance(res))
