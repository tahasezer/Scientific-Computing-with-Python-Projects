class Category:
  def __init__(self, name):
    # Initialize a new Category object with a given name.
    # It also initializes an empty ledger to store transactions.
    self.name = name
    self.ledger = []  # List to store the transactions

  def deposit(self, amount, description=""):
    # Add a deposit transaction to the ledger.
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    # Add a withdrawal transaction to the ledger.
    # If there are not enough funds, the withdrawal is not added to the ledger.
    # Returns True if the withdrawal is successful, False otherwise.
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
      
  def get_balance(self):
    # Calculate and return the current balance of the category.
    balance = 0
    for item in self.ledger:
        balance += item["amount"]
    return balance

  def check_funds(self, amount):
    # Check if there are enough funds in the category for a given amount.
    # Returns True if there are enough funds, False otherwise.
    return amount <= self.get_balance()

  def transfer(self, amount, category):
    # Transfer funds from one category to another.
    # If there are not enough funds, the transfer is not performed.
    # Returns True if the transfer is successful, False otherwise.
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  def __str__(self):
    # Return a string representation of the category object.
    # The string includes a title line, individual transactions, and the total balance.
    title = f"{self.name:*^30}\n"  # Title line with category name centered
    items = ""
    total = 0
    for item in self.ledger:
      description = item["description"][:23]  # Limit description to 23 characters
      amount = format(item["amount"], ".2f")  # Format amount to 2 decimal places
      items += f"{description:<23}{amount:>7}\n"  # Left align description, right align amount
      total += item["amount"]
    output = title + items + f"Total: {total:.2f}"  # Display the total balance
    return output



def create_spend_chart(categories):
    # Create a spending chart based on the percentage spent in each category.
    # The chart is returned as a string.
    category_names = []
    spent = []
    spent_percentages = []

    # Calculate the total withdrawals and store category names
    for category in categories:
        total_withdrawals = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total_withdrawals += abs(item["amount"])
        spent.append(total_withdrawals)
        category_names.append(category.name)

    # Calculate the percentage spent for each category
    for amount in spent:
        spent_percentages.append(round(amount / sum(spent), 2) * 100)

    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)

    # Construct the spending chart
    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percentage in spent_percentages:
            if percentage >= label:
                graph += "o  "  # Display 'o' for each percentage level reached
            else:
                graph += "   "  # Display empty space if not reached
        graph += "\n"

    graph += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_category_name_length = max(len(name) for name in category_names)

    # Add category names vertically below the bars
    for i in range(max_category_name_length):
        graph += "     "
        for name in category_names:
            if i < len(name):
                graph += name[i] + "  "  # Display each character vertically
            else:
                graph += "   "  # Display empty space if name length is shorter
        if i < max_category_name_length - 1:
            graph += "\n"

    return graph




  
    