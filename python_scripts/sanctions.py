#Check which brothers need to be sanctioned and update the amount
#in the master list, no return value, just update balance

def update_sanctions(master_list, sanction_list, sanction_amt):
    for brother in master_list:
        if brother[0] in sanction_list:
            brother[1] = str(int(brother[1]) + sanction_amt)