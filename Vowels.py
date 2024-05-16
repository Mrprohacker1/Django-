from django.http import HttpResponse

def count_vowels_consonants(request):
    if request.method == 'GET':
        # Render an HTML form to take input from the user
        form = """
        <form method="post">
            <label for="input_string">Enter a string:</label>
            <input type="text" id="input_string" name="input_string" required>
            <button type="submit">Count Vowels and Consonants</button>
        </form>
        """
        return HttpResponse(form)

    elif request.method == 'POST':
        # Get the input string from the request
        input_string = request.POST.get('input_string')

        # Define a set of vowels
        vowels = set('aeiou')

        # Initialize counters for vowels and consonants
        vowel_count = 0
        consonant_count = 0

        # Loop through each character in the string
        for char in input_string.lower():
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

        # Render the result as an HTML response
        response = f"""
        <html>
            <body>
                <h1>Vowels and Consonants in "{input_string}"</h1>
                <p>Vowels: {vowel_count}</p>
                <p>Consonants: {consonant_count}</p>
            </body>
        </html>
        """
        return HttpResponse(response)
