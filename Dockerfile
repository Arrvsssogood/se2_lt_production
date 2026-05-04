FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app (main.py and templates)
COPY . .

EXPOSE 5027

# Command to run the app
CMD ["gunicorn", "--bind", "0.0.0.0:5027", "app.main:app"]