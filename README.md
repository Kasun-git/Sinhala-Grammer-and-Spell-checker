Sinhala Spell and Grammar Checker
This project is a Sinhala Spell and Grammar Checker that leverages approximate string matching and custom grammar rules to identify and correct spelling and grammatical errors in Sinhala text. It is designed to handle labeled datasets and applies preprocessing techniques to remove labels for efficient text correction.

Features
Spell Checking: Uses rapidfuzz for fast and accurate approximate string matching based on Levenshtein distance.
Grammar Correction: Implements Sinhala-specific grammar rules, such as:
Sentences with "මම" as the subject must end with "මී."
Sentences with "අපි" as the subject must end with "මු."
Batch Processing: Processes paragraphs sentence by sentence for both spelling and grammar corrections.
Customizable Dictionary: Accepts a user-defined Sinhala word dictionary in JSON format.
Detailed Feedback: Provides a list of incorrect words and their corrections.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/sinhala-spell-checker.git
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Add your custom Sinhala word dictionary in JSON format (e.g., sinhala_words.json).
Usage
Load your dictionary file:
python
Copy code
sinhala_dictionary = load_dictionary("sinhala_words.json")
Provide an input paragraph for correction:
python
Copy code
paragraph = "මම සෑම පෝය දිනකම පන්සල් යන්නෙය."
incorrect_words, corrected_words, corrected_paragraph = correct_paragraph(paragraph, sinhala_dictionary)
print(corrected_paragraph)
View the corrected paragraph along with identified and corrected words.
Example Output
Input Paragraph
plaintext
Copy code
මම සෑම පෝය දිනකම පන්සල් යන්නෙය. 
අපි වන්දනා චාරිකාව සදහා ගියෙය.
Corrected Paragraph
plaintext
Copy code
මම සෑම පෝය දිනකම පන්සල් යන්නෙමී. 
අපි වන්දනා චාරිකාව සදහා ගියමු.
Incorrect Words
plaintext
Copy code
["යන්නෙය", "ගියෙය"]
Corrected Words
plaintext
Copy code
["යන්නෙමී", "ගියමු"]
Contribution
Contributions are welcome! Please open an issue or submit a pull request for suggestions or improvements.

License
This project is licensed under the MIT License.
