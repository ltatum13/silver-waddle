#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

struct Order {
    int youth;
    int xl; 
    int doubleXl;
    int colorAmount; 
};

void addCustomerInputs(int amountOfOrders, vector<Order>* listOfAmountOrders) {
    vector<Order> listOfOrders; 
    Order orders_vec;                

    for (int i = 0; i < amountOfOrders; i++) {
        cout << "Order " << i + 1 << endl;

        cout << "How many colors? ";
        cin >> orders_vec.colorAmount;

        cout << "How many youth sizes? ";
        cin >> orders_vec.youth;

        cout << "How many XL sizes? ";
        cin >> orders_vec.xl;

        cout << "How many Double XL sizes? ";
        cin >> orders_vec.doubleXl;

        listOfOrders.push_back(orders_vec);
    }
    *listOfAmountOrders = listOfOrders; 
}

struct CustomerPrice {
    int totalShirts;
    int colorAmount;
    string size;
    double price;
};

double getPricePerShirt(int totalShirts, int colorAmount, const string& size) {
    const int priceTableSize = 5;
    double youthPrices[4][priceTableSize] = {
        {19.69, 20.69, 21.69, 22.69, 23.69},
        {9.69, 11.69, 12.69, 13.69, 14.69},
        {7.70, 9.70, 10.70, 11.70, 12.70},
        {6.70, 8.70, 9.70, 10.70, 11.70}
    };
    double sToXlPrices[4][priceTableSize] = {
        {19.99, 21.99, 22.99, 23.99, 24.99},
        {9.99, 11.99, 12.99, 13.99, 14.99},
        {8.00, 10.00, 11.00, 12.00, 13.00},
        {7.00, 9.00, 10.00, 11.00, 12.00}
    };
    double xlTo5xlPrices[4][priceTableSize] = {
        {21.64, 22.64, 23.64, 24.64, 25.64},
        {11.64, 12.64, 13.64, 14.64, 15.64},
        {9.65, 11.65, 12.65, 13.65, 14.65},
        {8.65, 10.65, 11.65, 12.65, 13.65}
    };

    double (*prices)[5] = nullptr;

    if (size == "youth") {
        prices = youthPrices;
    } else if (size == "S-XL") {
        prices = sToXlPrices;
    } else if (size == "2XL-5XL") {
        prices = xlTo5xlPrices;
    } else {
        return 0; // Default return if no conditions match
    }

    int index = -1;
    if (totalShirts >= 12 && totalShirts <= 24) {
        index = 0;
    } else if (totalShirts >= 25 && totalShirts <= 49) {
        index = 1;
    } else if (totalShirts >= 50 && totalShirts <= 199) {
        index = 2;
    } else if (totalShirts >= 200 && totalShirts <= 299) {
        index = 3;
    } else if (totalShirts >= 300) {
        cout << "Call for quote" << endl;
        return -1; // Placeholder for custom quote
    }

    if (index != -1 && colorAmount >= 1 && colorAmount <= 5) {
        return prices[index][colorAmount - 1];
    }

    return 0; // Default return if no conditions match
}

void printCustomerPrices(const vector<CustomerPrice>& customerPrices) {
    for (const auto& customerPrice : customerPrices) {
        cout << "Total Shirts: " << customerPrice.totalShirts
             << ", Color Amount: " << customerPrice.colorAmount
             << ", Size: " << customerPrice.size
             << ", Price: $" << customerPrice.price << endl;
    }
}

void calculateAndPrintCustomerPrices(const vector<Order>& orders) {
    vector<CustomerPrice> customerPrices;

    for (const auto& order : orders) {
        int colorAmount = order.colorAmount;

        // Process each size category
        if (order.youth > 0) {
            double price = getPricePerShirt(order.youth, colorAmount, "youth");
            if (price != -1) { // Ensure price is valid
                customerPrices.push_back({order.youth, colorAmount, "youth", price});
            }
        }
        if (order.xl > 0) {
            double price = getPricePerShirt(order.xl, colorAmount, "S-XL");
            if (price != -1) { // Ensure price is valid
                customerPrices.push_back({order.xl, colorAmount, "S-XL", price});
            }
        }
        if (order.doubleXl > 0) {
            double price = getPricePerShirt(order.doubleXl, colorAmount, "2XL-5XL");
            if (price != -1) { // Ensure price is valid
                customerPrices.push_back({order.doubleXl, colorAmount, "2XL-5XL", price});
            }
        }
    }

    printCustomerPrices(customerPrices);
    
    // Calculate final price
    vector<double> totalAmount;
    for (auto& order : customerPrices) {
        double variableONE = order.totalShirts * order.price;
        totalAmount.push_back(variableONE);
    }
    
    float finalPrice = 0;
    for(size_t order = 0; order < totalAmount.size(); order++) {
        finalPrice += totalAmount[order];
    }
    
    cout << endl;
    cout << fixed << setprecision(2);
    cout << "Final Price: $" << finalPrice << endl;
}

int main() {
    vector<Order> amountOrdersList;
    int amountOfOrders;

    cout << "Welcome to Tshirt-Co." << endl;

    cout << "How many orders will you be making today? ";
    cin >> amountOfOrders;

    addCustomerInputs(amountOfOrders, &amountOrdersList);

    // Print first order's youth sizes as an example
    if (!amountOrdersList.empty()) {
        cout << "First order youth sizes: " << amountOrdersList[0].youth << endl;
    }

    calculateAndPrintCustomerPrices(amountOrdersList);

    return 0;
}