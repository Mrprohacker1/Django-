from django.http import HttpResponse

def multiplication_table(request):
    if request.method == 'GET':
        # Render an HTML form to take input from the user
        form = f"""
        <form method="post">
            <label for="number">Enter a number:</label>
            <input type="number" id="number" name="number" required>
            <button type="submit">Generate Table</button>
        </form>
        """
        return HttpResponse(form)

    elif request.method == 'POST':
        # Get the input number from the request
        number = int(request.POST.get('number'))

        # Generate the multiplication table as an HTML string
        table_rows = []
        for i in range(1, 11):
            table_rows.append(f"<tr><td>{number} x {i}</td><td>{number * i}</td></tr>")
        table = "<table border='1'>" + "".join(table_rows) + "</table>"

        # Render the multiplication table as an HTML response
        response = f"""
        <html>
            <body>
                <h1>Multiplication Table for {number}</h1>
                {table}
            </body>
        </html>
        """
        return HttpResponse(response)
