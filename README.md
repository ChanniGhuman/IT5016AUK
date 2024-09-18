# IT5016


User Data Collection Program
This program collects user data, calculates the total amount for items, categorizes the request, and generates a detailed report. The design adheres to several software design principles: KISS, DRY, and YAGNI.

Principles Applied:

KISS (Keep It Simple, Stupid):
Simplicity: The code is structured into small, clear functions, each performing a single task. This makes it easy to read, understand, and maintain.
User Interaction: Input prompts are straightforward, allowing users to easily enter their data without unnecessary complexity.

DRY (Don't Repeat Yourself):
Reusability: Functions are defined to avoid code duplication. For example, the calculate_total_amount() function can be reused whenever item prices need to be summed, promoting code reuse.
Clear Separation of Concerns: Each function is responsible for a distinct part of the process (data collection, calculation, categorization, report generation), reducing redundancy in code logic.

YAGNI (You Aren't Gonna Need It):
Focus on Current Requirements: The program implements only the functionality necessary for the task at hand. There are no unnecessary features or over-engineering, ensuring that the code remains lean and focused.
Scalability Consideration: While the current version of the program meets the basic requirements, it avoids implementing features that may not be needed in the future, allowing for easier maintenance.

Code Overview:

Functions:

collect_user_data(id_counter)

Gathers user information (name, age, email) and generates a unique ID.

Returns the collected data and the updated ID counter.

calculate_total_amount()

Prompts the user to enter item names and prices until they choose to finish.

Returns the total amount of the entered items.

categorize_request(total_amt)

Categorizes the total amount into "Low" or "High" based on a threshold (150).

Returns the category and a recommendation.

create_detailed_report(user_age, user_email, user_name, id_counter, total_amt, category, recommendation)

Generates and displays a detailed report based on user input and calculations.
main()

#The main driver function that orchestrates the flow of the program.

Usage:

To run the program, simply execute the main() function. Users will be prompted to enter their name, age, and email, followed by item names and prices. The program will then output a detailed report based on the collected information.

#Improvements and Future Considerations:

Input Validation: Adding further validation for user inputs (e.g., ensuring age is a valid number) to enhance robustness.

Error Handling: Implementing better error handling for unexpected inputs.

Extensibility: While the current design avoids unnecessary complexity, future features (like saving reports) can be added without impacting existing functionality.

#Conclusion:

This program serves as a simple yet effective solution for user data collection and processing. By adhering to KISS, DRY, and YAGNI principles, it remains maintainable and easy to understand.



