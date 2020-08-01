# Use the official lightweight Python image.

FROM python:3.7-slim
EXPOSE 8080
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install pandas Pillow tensorflow numpy streamlit

# Run the web service on container startup. 
CMD streamlit run --server.port 8080 --server.enableCORS false app.py
