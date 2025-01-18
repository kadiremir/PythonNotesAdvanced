"""S: Single Responsibility Principle (SRP)

Definition:
    A class should have only one reason to change, meaning it should have only one responsibility.

Tip:
    If a class is handling multiple tasks, consider dividing those tasks into separate classes to improve maintainability and reduce coupling.
"""

####################################################################################################
# Bad example
####################################################################################################

class UserRegistration:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_user(self):
        # Logic to register a user
        print(f"Registering user: {self.username}")

    def log(self, message):
        # Logic to log a message
        print(f"Log entry for {self.username}: {message}")
    
    def send_email(self, email):
        # Logic to send an email
        print(f"Sending email to {email}")
    
# Why is this bad?
# The UserRegistration class has multiple responsibilities:
# 1. Registering a user
# 2. Logging activities
# 3. Sending emails
# This violates the Single Responsibility Principle, as each of these tasks is unrelated and could
# evolve independently.


####################################################################################################
# Good example (Refactored for SRP)
####################################################################################################

class RegisterUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_user(self):
        # Logic to register a user
        print(f"User '{self.username}' registered successfully.")

class UserLogger:
    @staticmethod
    def log(username, message):
        # Logic to log user-related activities
        print(f"Log for {username}: {message}")

class EmailSender:
    @staticmethod
    def send_email(email, subject, body):
        # Logic to send an email
        print(f"Email sent to {email} with subject: {subject}")


# Example usage:

if __name__ == "__main__":
    # Register a user
    user = RegisterUser("john_doe", "secure_password")
    user.register_user()

    # Log an activity
    UserLogger.log("john_doe", "User registered successfully.")

    # Send an email
    EmailSender.send_email("john_doe@example.com", "Welcome!", "Thank you for registering.")
