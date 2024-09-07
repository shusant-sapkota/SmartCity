# Use the base image
FROM bitnami/spark:latest

# Copy the requirements file into the container
COPY requirements.txt /opt/bitnami/spark/requirements.txt

# Install Python dependencies
RUN pip install -r /opt/bitnami/spark/requirements.txt

# Set the default command to start Spark Master
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]