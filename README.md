
# Number Classification API

## Overview
The Number Classification API is a RESTful service built using Django REST Framework (DRF). It takes an integer as input and returns interesting mathematical properties along with a fun fact about the number.

## Features
- Determines if a number is prime
- Checks if a number is perfect
- Identifies Armstrong numbers
- Classifies numbers as odd or even
- Calculates the sum of digits
- Fetches a fun fact from the Numbers API

## Technologies Used
- Python
- Django REST Framework (DRF)
- Requests library


## API Endpoint

### Classify Number
- **URL:** `/api/classify-number`
- **Method:** `GET`
- **Query Parameter:** `number` (required)

### Example Request
```bash
GET /api/classify-number?number=371
```

### Successful Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\\Scripts\\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start the Server
```bash
python manage.py runserver
```

## Deployment

1. **Choose a Deployment Platform:**  
   You can deploy the API on platforms like:
   - Railway
   - Render
   - Heroku
   - Vercel (with a Django adapter)

2. **Prepare for Deployment:**  
   - Ensure `ALLOWED_HOSTS` is configured in `settings.py`.
   - Install and configure `django-cors-headers`:
     ```bash
     pip install django-cors-headers
     ```
     Add `'corsheaders'` to `INSTALLED_APPS` and configure CORS settings.

3. **Deploy:**  
   Follow the hosting platform’s guide to deploy Django applications.

4. **Verify Deployment:**  
   Ensure the API is publicly accessible and test using:
   ```bash
   curl <your-deployed-url>/api/classify-number?number=371
   ```

## Additional Notes
- The API handles only integer inputs. Non-integer values return a `400 Bad Request` error.
- Fast response times (< 500ms) are targeted for optimal performance.
- Ensure environment variables for deployment (like `SECRET_KEY` and `DEBUG`) are properly configured.

## Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the \"Software\"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contact
For any inquiries or support, please contact David Nduonofit at davidnduonofit47@gmail.com.


