"""
Staff info
Author Charanpreet Singh
"""
def staff_info (id_counter):
    Date=input("Please enter Date :")
    staff_id=input("Please enter your id :")
    staff_name=input("Please enter your name:")
    
    unique_id = id_counter+1
    id_counter=unique_id
    print("Printing staff Information")
    print(f"Date: {Date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Requisition id: {id_counter}")
    
    return Date, staff_id,staff_name,id_counter
def main():
    id_counter=1000
    id_counter,Date,staff_id,staff_name=staff_info(id_counter)
main()