import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file (useful for API keys, etc.)
load_dotenv()

def fetch_data_from_api(url: str) -> dict:
    """
    Fetch JSON data from a public API using requests.
    Example: JSONPlaceholder fake API.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

def process_data(data: list) -> pd.DataFrame:
    """
    Convert list of dicts to a pandas DataFrame and show basic info.
    """
    df = pd.DataFrame(data)
    print("DataFrame info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())
    return df

def main():
    print("Starting my Python project...\n")
    
    # Example: Fetch fake user data from a public API
    api_url = "https://jsonplaceholder.typicode.com/users"
    print(f"Fetching data from {api_url}")
    
    try:
        data = fetch_data_from_api(api_url)
        df = process_data(data)
        
        # Save to CSV (optional)
        df.to_csv("users.csv", index=False)
        print("\nData saved to users.csv")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    # Example of using an environment variable
    api_key = os.getenv("MY_API_KEY")
    if api_key:
        print(f"\nAPI key loaded (length: {len(api_key)} characters)")
    else:
        print("\nNo API key found in .env file")

if __name__ == "__main__":
    main()