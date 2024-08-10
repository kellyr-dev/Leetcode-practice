package Design

class Bank(
    balance: LongArray

) {
    private var tableAccount : HashMap<Int, Long> = HashMap<Int, Long>()

    init {
        for (i in 0..balance.size-1){
            tableAccount.put(i, balance[i])
        }
    }

    fun transfer(account1: Int, account2: Int, money: Long): Boolean {

        if (tableAccount.containsKey(account1-1) && tableAccount.containsKey(account2-1)){

            var newMoney : Long = 0
            if (tableAccount.get(account1-1)!! >= money){
                newMoney = tableAccount.get(account1-1)!! - money
                tableAccount.replace(account1-1, newMoney)

                var addMoney : Long = tableAccount.get(account2-1)!! + money
                tableAccount.replace(account2-1, addMoney)

                return true

            }else {
                return false
            }
        }
        return false
    }

    fun deposit(account: Int, money: Long): Boolean {

        if (tableAccount.containsKey(account-1)){

            var newMoney = tableAccount.get(account-1)!! + money
            tableAccount.replace(account-1, newMoney)
            return true
        }
        return false

    }

    fun withdraw(account: Int, money: Long): Boolean {

        if (tableAccount.containsKey(account-1)){

            if (tableAccount.get(account-1)!! >= money){

                var newMoney = tableAccount.get(account-1)!! - money
                tableAccount.replace(account-1, newMoney)
                return true
            }else{
                return false
            }
        }
        return false
    }

}

fun main(){

    // bank = new Bank([10, 100, 20, 50, 30]);

    var bank = Bank(longArrayOf(10,100,20,50,30))

    println("withdraw: ${bank.withdraw(3,10)}")
    println("transfer: ${bank.transfer(5,1, 20)}")
    println("deposit: ${bank.deposit(5,20)}")
    println("transfer: ${bank.transfer(3,4,15)}")
    println("withdraw: ${bank.withdraw(10,50)}")


}