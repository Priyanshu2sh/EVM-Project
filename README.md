# EVM-Project

## Overview

This project is a demonstration of how Electronic Voting Machines (EVMs) can be manipulated if the program logic is tampered with. It is built using the Django framework and showcases a voting system with four parties. The project transfers three votes from the first three parties to the fourth party every ten votes, illustrating potential vulnerabilities.

## Features

- Voting functionality for four parties
- Automatic transfer of votes from the first three parties to the fourth party every ten votes
- Frontend implemented with Django templates
- Backend logic demonstrating the manipulation of votes

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Priyanshu2sh/EVM-Project.git
   cd evm-project
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Make migrations:

   ```bash
   python manage.py makemigrations
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. Visit the homepage where you will see the four parties with buttons to vote for them.
2. Click on the buttons to cast votes for the respective parties.
3. Observe the vote counts. After every 10 votes cast for the first three parties, 3 votes will be automatically transferred to the fourth party.

## Disclaimer

This project is for educational purposes only. It is intended to demonstrate potential vulnerabilities in EVM systems and should not be used for any malicious activities.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.