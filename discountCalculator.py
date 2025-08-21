def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage.

  Returns:
    The final price after applying the discount, or the original price if the
    discount is less than 20%.
  """
  if discount_percent >= 20:
    final_price = price - (price * (discount_percent / 100))
    return final_price
  else:
    return price

# Prompt the user for input
try:
  original_price = float(input("Enter the original price: "))
  discount_percentage = float(input("Enter the discount percentage: "))
  
  # Calculate and print the final price
  final_price = calculate_discount(original_price, discount_percentage)
  
  if discount_percentage >= 20:
    print(f"The final price after a {discount_percentage}% discount is: {final_price:.2f}")
  else:
    print(f"The discount is less than 20%. The original price of {original_price:.2f} remains unchanged.")

except ValueError:
  print("Invalid input. Please enter a valid number for price and discount percentage.")