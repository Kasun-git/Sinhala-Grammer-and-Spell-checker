# Sinhala Spell and Grammar Checker

This project is a **Sinhala Spell and Grammar Checker** that leverages approximate string matching and custom grammar rules to identify and correct spelling and grammatical errors in Sinhala text. It is designed to handle labeled datasets and applies preprocessing techniques to remove labels for efficient text correction.

## Features
- **Spell Checking**: Uses `rapidfuzz` for fast and accurate approximate string matching based on Levenshtein distance.
- **Grammar Correction**: Implements Sinhala-specific grammar rules, such as:
  - Sentences with `"මම"` as the subject must end with `"මී."`
  - Sentences with `"අපි"` as the subject must end with `"මු."`
- **Batch Processing**: Processes paragraphs sentence by sentence for both spelling and grammar corrections.
- **Customizable Dictionary**: Accepts a user-defined Sinhala word dictionary in JSON format.
- **Detailed Feedback**: Provides a list of incorrect words and their corrections.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sinhala-spell-checker.git
