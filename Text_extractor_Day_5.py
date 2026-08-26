import re
import json

# Read Text File

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return ""

# Extract Emails
def extract_emails(text):
    pattern = r"[\w.-]+@[\w.-]+\.\w+"
    return re.findall(pattern, text)

# Extract Phone Numbers
def extract_phone_numbers(text):
    pattern = r"\b\d{10}\b"
    return re.findall(pattern, text)

# Extract URLs
def extract_urls(text):
    pattern = r"https?://[^\s]+"
    return re.findall(pattern, text)

# Save Results
def save_results(data, filename):
    with open(filename, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )
    print(f"\nResults saved to {filename}")

# Main Program
def main():
    filename = "data.txt"
    text = read_file(filename)
    if not text:
        return
    emails = extract_emails(text)
    phone_numbers = extract_phone_numbers(text)
    urls = extract_urls(text)
    results = {
        "emails": emails,
        "phone_numbers": phone_numbers,
        "urls": urls
    }
    print("\n========== EXTRACTED DATA ==========")
    print("\nEmails:")
    for email in emails:
        print("-", email)
    print("\nPhone Numbers:")
    for phone in phone_numbers:
        print("-", phone)
    print("\nURLs:")
    for url in urls:
        print("-", url)
    save_results(
        results,
        "extracted_data.json"
    )

main()