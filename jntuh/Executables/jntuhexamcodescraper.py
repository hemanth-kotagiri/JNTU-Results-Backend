# Import necessary libraries
import requests
from bs4 import BeautifulSoup


# Define a function to extract the exam code from the result link
def extract_exam_code(result_link):
    exam_code_index = result_link.find("examCode")
    exam_code = result_link[exam_code_index + 9:exam_code_index + 13]
    return exam_code


# Define a function to categorize the exam code based on the year and semester
def categorize_exam_code(result_text, exam_code):
    if " I Year I " in result_text:
        return "1-1"
    elif " I Year II " in result_text:
        return "1-2"
    elif " II Year I " in result_text:
        return "2-1"
    elif " II Year II " in result_text:
        return "2-2"
    elif " III Year I " in result_text:
        return "3-1"
    elif " III Year II " in result_text:
        return "3-2"
    elif " IV Year I " in result_text:
        return "4-1"
    elif " IV Year II " in result_text:
        return "4-2"
    else:
        return None


# Define a function to get the exam codes from JNTUH website
def exam_codes():
    # URL of the website containing exam codes
    url = "http://results.jntuh.ac.in/jsp/home.jsp"

    # Send a request to the website and get the response
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the tables in the HTML content and select the first one
    btech_results = soup.find_all("table")[0].find_all("tr")

    # Initialize an empty dictionary to store the exam codes
    exam_codes = {
        "1-1": [],
        "1-2": [],
        "2-1": [],
        "2-2": [],
        "3-1": [],
        "3-2": [],
        "4-1": [],
        "4-2": [],
    }

    # Loop through each row of the table and extract the exam code for R18 batch
    for result in btech_results:
        result_link = result.find_all("td")[0].find_all("a")[0]["href"]
        result_text = result.get_text()

        if "R18" in result_text:
            exam_code = extract_exam_code(result_link)
            category = categorize_exam_code(result_text, exam_code)

            if category is not None:
                exam_codes[category].append(exam_code)

    # Sort the exam codes in each category and return the dictionary
    for category, codes in exam_codes.items():
        exam_codes[category] = sorted(codes)
    return exam_codes

