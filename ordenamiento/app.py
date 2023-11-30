from flask import Flask, request, render_template, redirect

app = Flask(__name__)
numbers = []

def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

@app.route('/')
def index():
    numbers_with_indices = list(enumerate(numbers))
    return render_template('index.html', numbers_with_indices=numbers_with_indices)

@app.route('/add_number', methods=['POST'])
def add_number():
    number = int(request.form['number'])
    numbers.append(number)
    return redirect('/')

@app.route('/delete_number/<int:index>')
def delete_number(index):
    if 0 <= index < len(numbers):
        del numbers[index]
    return redirect('/')

@app.route('/sort_ascending')
def sort_ascending():
    bubble_sort_ascending(numbers)
    return redirect('/')

@app.route('/sort_descending')
def sort_descending():
    bubble_sort_descending(numbers)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
