from controller.user_conntroller import UserController
from controller.product_controller import ProductController
from controller.cart_controller import CartController
from controller.order_controller import OrderController

def main():
    user_controller = UserController()
    product_controller = ProductController()
    cart_controller = CartController()
    order_controller = OrderController()

    current_user = None

    while True:
        try:
            if current_user is None:
                print("\n=== Main Menu ===")
                print("1. Register")
                print("2. Login")
                print("3. Exit")
                choice = input("Enter choice: ")

                if choice == "1":
                    user_controller.register()
                elif choice == "2":
                    current_user = user_controller.login()
                elif choice == "3":
                    break
                else:
                    print("Invalid choice.")
            else:
                role = current_user['role']
                if role == "customer":
                    print("\n=== Customer Menu ===")
                    print("1. Browse Products")
                    print("2. View Cart")
                    print("3. Add to Cart")
                    print("4. Remove from Cart")
                    print("5. Place Order")
                    print("6. View Order History")
                    print("7. Logout")
                    choice = input("Enter choice: ")

                    if choice == "1":
                        product_controller.view_all_products()
                    elif choice == "2":
                        cart_controller.view_cart(current_user['user_id'])
                    elif choice == "3":
                        cart_controller.add_to_cart(current_user['user_id'])
                    elif choice == "4":
                        cart_controller.remove_from_cart(current_user['user_id'])
                    elif choice == "5":
                        order_controller.place_order(current_user['user_id'])
                    elif choice == "6":
                        order_controller.view_order_history(current_user['user_id'])
                    elif choice == "7":
                        current_user = None
                    else:
                        print("Invalid choice.")
                elif role == "admin":
                    print("\n=== Admin Menu ===")
                    print("1. Add Product")
                    print("2. Update Product")
                    print("3. Delete Product")
                    print("4. Add Category")
                    print("5. View All Products")
                    print("6. Manage Stock")
                    print("7. View All Orders")
                    print("8. Logout")
                    choice = input("Enter choice: ")

                    if choice == "1":
                        product_controller.add_product()
                    elif choice == "2":
                        product_controller.update_product()
                    elif choice == "3":
                        product_controller.delete_product()
                    elif choice == "4":
                        product_controller.add_category()
                    elif choice == "5":
                        product_controller.view_all_products()
                    elif choice == "6":
                        product_controller.manage_stock()
                    elif choice == "7":
                        order_controller.view_all_orders()
                    elif choice == "8":
                        current_user = None
                    else:
                        print("Invalid choice.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
