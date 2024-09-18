# IT5016

This project is a simple customer data collection and order processing system. It consists of four main functions:

collect_user_data: collects user information (name, age, email) and assigns a unique ID.
calculate_total_amount: calculates the total amount of an order by prompting the user to input item names and prices.
categorize_request: categorizes the order based on the total amount and provides a recommendation.
create_detailed_report: generates a detailed report containing user information, order details, and recommendations.
Code Structure

The code is structured into five functions:

collect_user_data(id_counter): collects user information and assigns a unique ID.
Parameters: id_counter (initial unique ID)
Returns: user_age, user_email, user_name, id_counter (updated unique ID)
calculate_total_amount(): calculates the total amount of an order.
Returns: total_amt (total amount of the order)
categorize_request(total_amt): categorizes the order based on the total amount.
Parameters: total_amt (total amount of the order)
Returns: category, recommendation
create_detailed_report(user_age, user_email, user_name, id_counter, total_amt, category, recommendation): generates a detailed report.
Parameters: user information, order details, and recommendations
main(): calls the above functions in sequence to execute the program.
Usage

To run the program, simply execute the main() function. The program will prompt the user to input their information, order details, and then generate a detailed report.
