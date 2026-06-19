#=================  Digital Billing Cart ====================
# accept : product name ,Quantity , Price for 5 products.
# Calculations : grand total ,item total ,gst (18%) , final bill 
# output : Laptop 1*10000 = 10000
#          Mouse   2* 500 = 1000
#          keyboard  1* 50000 = 50000
#           grandtotal/subtotal : ,gst :, total :

#extension : apply discounts : above 50,000-> 10% ,,,, above 25000 -> 5%

def billing_cart ():
    for i in range (0,3):
        price_cart = []
        product_name = str(input("enter your product name :"))
        qty = int(input("enter your product Quantity :"))
        price = float(input("enter the price for the products :"))

        item_total = qty * price
        price_cart.append(item_total)
        print(f"{product_name}   {qty}* {price} = {item_total}")
        
billing_cart()













