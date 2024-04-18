from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data
        email = request.form['email']
        password = request.form['password']

        # Perform login logic (e.g., check the user's credentials against a database)
        # Here, we'll just print the details for demonstration purposes
        print(f'Email: {email}, Password: {password}')

        # Redirect the user to the dashboard or any other desired page
        return redirect('/dashboard')

    # Render the login page
    return render_template('login.html')

if __name__ == '__main__':
    app.run()