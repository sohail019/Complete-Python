# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Place Your Order ('Small', 'Medium', 'Large): ")
extra_shot = False

if extra_shot:
    coffee = order_size + ' coffee with an extra shot'
else:
    coffee = order_size + ' coffee'

print("Order", coffee)
