import requests
from core.settings import API_BASE_URL

def main():
    response = requests.get(f"{API_BASE_URL}/programs")
    response.raise_for_status()

    programs = response.json()
    for p in programs:
        print(f"[{p['region']}] {p['title']} — {p['amount']} руб")

if __name__ == "__main__":
    main()
