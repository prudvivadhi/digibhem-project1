# visualization.py
import matplotlib.pyplot as plt

class Visualization:
    def plot_expenses(self, expenses):
        categories = [expense[2] for expense in expenses]
        amounts = [expense[3] for expense in expenses]
        plt.bar(categories, amounts)
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.title("Spending Patterns")
        plt.show()
