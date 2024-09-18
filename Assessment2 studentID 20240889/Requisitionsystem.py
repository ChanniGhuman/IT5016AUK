"""
Assessment2: Software program development to professional working brief.
Part B: Software Project
Student Id:20240889
Author: Charanpreet Singh
"""
class RequestSystem:
    def __init__(self):
        self.Date = input("Please enter Date: ")
        self.Staff_id = input("Please enter Staff Id: ")
        self.Staff_Name = input("Please enter Staff Name: ")
        self.uniqueid = 1000
        self.products = []
        self.total = 0
        self.approved_request = 0
        self.pending_request = 0
        self.notapproved_request = 0
        self.requests = []  # List to store all requests

    def userinfo(self):
        self.uniqueid += 1  # Increment unique ID for each request

    def request_details(self):
        self.products = []  # Clear previous products
        self.total = 0      # Reset total for new request
        while True:
            item = input("Enter the item (Enter 'exit' when finished): ")
            if item.lower() == 'exit':
                break
            try:
                price = float(input("Enter the price of the item: "))
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                continue
            self.products.append((item, price))  # Store item and price as a tuple
            self.total += price

        self.referenceid =self.Staff_id[-4:]+str(self.uniqueid)[-3:] # Generate unique reference ID
        self.userinfo()  # Increment unique ID for next request
        return self.total, self.products, self.referenceid

    def request_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approved_request += 1
        else:
            self.status = "Pending"
            self.pending_request += 1

        print(f"Total: ${self.total}")
        print(f"Request Status: {self.status}")

        # Store the request with all relevant details
        request = {
            "Date": self.Date,
            "Staff Id": self.Staff_id,
            "Staff Name": self.Staff_Name,
            "Requisition ID": self.referenceid,
            "Total": self.total,
            "Status": self.status,
            "Approval Ref": self.referenceid if self.status == "Approved" else None
        }
        self.requests.append(request)  # Add the request to the list

    def respond_request(self, manager_respond,uniqueid, requisition_id):
        for req in self.requests:
            if req['Requisition ID'] == self.uniqueid:
                if manager_respond.lower() == "approved":
                    req['Status'] = "Approved"
                    req['Approval Ref'] = f"AP-{requisition_id}"
                    self.approved_request += 1
                else:
                    req['Status'] = "Not Approved"
                    self.notapproved_request += 1
                self.update_statistics()
                return req['Status']
        return 'Requisition not found'

    def display_requests(self):
        if not self.requests:
            print("No requests have been submitted yet.")
        else:
            print("Printing Requisitions:")
            for req in self.requests:
                print(f"Date: {req['Date']}")
                print(f"Staff ID: {req['Staff Id']}")
                print(f"Staff Name: {req['Staff Name']}")
                print(f"Requisition ID: {req['Requisition ID']}")
                print(f"Total: ${req['Total']}")
                print(f"Status: {req['Status']}")
                print(f"Approval Ref: {req.get('Approval Ref', 'N/A')}")

    def statistics(self):
        self.update_statistics()  # Ensure statistics are updated before displaying
        print(f"Approved Requests: {self.approved_request}")
        print(f"Pending Requests: {self.pending_request}")
        print(f"Not Approved Requests: {self.notapproved_request}")

    def update_statistics(self):
        # Update statistics based on current requests
        self.approved_request = sum(1 for req in self.requests if req['Status'] == 'Approved')
        self.pending_request = sum(1 for req in self.requests if req['Status'] == 'Pending')
        self.notapproved_request = sum(1 for req in self.requests if req['Status'] == 'Not Approved')

# Main program loop
def main():
    system = RequestSystem()

    while True:
        choice = input("\n1. Submit Request\n2. Display Requests\n3. View Statistics\n4. Exit\nChoose an option: ")
        if choice == "1":
            system.request_details()
            system.request_approval()
        elif choice == "2":
            system.display_requests()
        elif choice == "3":
            system.statistics()
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
