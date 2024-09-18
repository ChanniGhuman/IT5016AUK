def Requisition_approval():
    total_amount=float(input("Total: $"))
    if total_amount>500:
        Status="pending"
        Approval_Refference_Number= "FN19001"

    else:
        Status= "Approved"
        Approval_Refference_Number ="FN19001"

        print(f"Status:{Status}")
        print(f"Approval Refference Number:{Approval_Refference_Number}")
def main():
        Requisition_approval()
main()