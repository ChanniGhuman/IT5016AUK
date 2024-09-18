def staff_info (id_counter):
    Date=input("Please enter Date :")
    staff_id=input("Please enter your id :")
    staff_name=input("Please enter your name:")
    
    unique_id = id_counter+1
    id_counter=unique_id
    print("Printing staff Information:")
    print(f"Date: {Date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Requisition id: {id_counter}")
    
    return Date,id_counter,staff_id,staff_name

def Requisitions_total():
    total_amount=0.0
    while True:
        price_input=input(": (or type 'finish' to end):")

        if price_input.lower()=='finish':
            break

        try:
            price=float(input(f"$ '{price_input}':"))
            total_amount+=price
        except ValueError:
            print("Invalid input, Please enter a value number.")

    return total_amount

def Requisition_approval(total_amount):
    if total_amount>500:
        Status="pending"
        Approval_Refference_Number= "FN19001"

    else:
        Status= "Approved"
        Approval_Refference_Number ="FN19001"

    return Status,Approval_Refference_Number

def Display_reqisitons( Date,id_counter,staff_id,staff_name,total_amount,Status,Approval_Refference_Number):
    print("Printing Requisition:")
    print(f"Date:{Date}")
    print(f"Requisition ID:{id_counter}")
    print(f"Staff ID:{staff_id}")
    print(f"Staff Name:{staff_name}")
    print(f"Total:$ {total_amount}")
    print(f"Status:{Status}")
    print(f"Approval Refference Number:{Approval_Refference_Number}")

def main():
    id_counter=10000
    Date,id_counter,staff_id,staff_name=staff_info(id_counter)
    total_amount=Requisitions_total()
    Status,Approval_Refference_Number=Requisition_approval(total_amount)
    Display_reqisitons(Date,id_counter,staff_id,staff_name,total_amount,Status,Approval_Refference_Number)
main()
