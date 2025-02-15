# Step-1: Use a lightweight Python image
FROM python:3.11-slim

# Step-2: Set up a working directory in the container
WORKDIR /app

# Step-3: Copy the requirements.txt file from backend to the container first (for caching)
# At this point, we're already inside app/ in the container
COPY ./requirements.txt .

# Step-4: Install all the dependencies inside requirements.txt and fastapi & uvicorn
RUN pip3 install --no-cache-dir -r requirements.txt
# Installing fastapi and uvicorn
RUN pip install fastapi uvicorn

# Step-5: Copy all the backend files into the working directory /app inside the container
COPY . .

# Step-6: Expose port 8000 for FastAPI
# Remember that this is the port for the container. The container is running FastAPI backend in its port 8000.
EXPOSE 8000

# Step 7: Define the command to start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]