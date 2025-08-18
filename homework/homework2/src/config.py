import dotenv
import os
from typing import Optional
dotenv.load_dotenv()



def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

def get_data_dir() -> str:
    return os.getenv("DATA_DIR")

API_KEY = get_key("API_KEY", False)
DATA_DIR = get_data_dir()

if API_KEY:
    print(f"API_KEY is present")
else:
    print(f"API_KEY is not present")


    