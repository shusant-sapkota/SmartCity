from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
print(find_dotenv())

configuration = {
    "AWS_ACCESS_KEY": os.getenv('AWS_ACCESS_KEY'),
    "AWS_SECRET_KEY": os.getenv('AWS_SECRET_KEY')
}

