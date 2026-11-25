import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Training data
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
marks = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Machine Learning Model
model = LinearRegression()
model.fit(hours, marks)


def predict_marks():
    name = name_entry.get()
    study_hours = hours_entry.get()

    if not name or not study_hours:
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        study_hours = float(study_hours)

        if study_hours < 0 or study_hours > 9:
            messagebox.showerror("Error", "Enter hours between 0 and 9")
            return

        prediction = model.predict([[study_hours]])

        result_label.config(
            text=f"{name}, Your Predicted Marks: {prediction[0]:.2f}"
        )

        plt.figure(figsize=(7, 5))
        plt.scatter(hours, marks, label="Training Data")
        plt.plot(hours, model.predict(hours), label="Prediction Line")
        plt.scatter(study_hours, prediction[0], label="Your Prediction")
        plt.xlabel("Study Hours")
        plt.ylabel("Marks")
        plt.title("Student Marks Prediction")
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Enter valid study hours")


# GUI Window
root = tk.Tk()
root.title("Student Marks Prediction")
root.geometry("500x400")
root.configure(bg="#eaf2f8")

title = tk.Label(
    root,
    text="Student Marks Prediction",
    font=("Arial", 20, "bold"),
    bg="#eaf2f8",
    fg="#17365d"
)
title.pack(pady=25)

tk.Label(root, text="Student Name", bg="#eaf2f8").pack()
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=8)

tk.Label(root, text="Study Hours", bg="#eaf2f8").pack()
hours_entry = tk.Entry(root, font=("Arial", 12))
hours_entry.pack(pady=8)

predict_button = tk.Button(
    root,
    text="Predict Marks",
    font=("Arial", 12, "bold"),
    bg="#17365d",
    fg="white",
    command=predict_marks
)
predict_button.pack(pady=20)

result_label = tk.Label(
    root,
    text="Your result will appear here",
    font=("Arial", 12, "bold"),
    bg="#eaf2f8",
    fg="#13804b"
)
result_label.pack(pady=10)

root.mainloop()