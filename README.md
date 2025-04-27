# Chemical Reaction Balancer and Molar Mass Calculator

A Python program that balances chemical reactions and calculates the molar mass of compounds.

---

Project Description

This project:
- Automatically balances chemical equations.
- Calculates molar masses for all compounds involved.
- Helps users practice and learn chemistry.

The project also generates a `requirements.txt` file automatically if not present.

---

How to Set Up Locally

Requirements:
- Python 3.8 or higher

Installation:

1. Clone the repository:
    git clone https://github.com/yourusername/chemical-reaction-balancer.git
    cd chemical-reaction-balancer

2. Create a virtual environment and activate it:
    python -m venv venv
    On Windows, activate the virtual environment with:
        venv\Scripts\activate
    On Linux/Mac, use:
        source venv/bin/activate

3. Install dependencies:
    pip install -r requirements.txt

4. Run the program:
    python Calculator_code.py

---

How the Program Works

- You input a chemical reaction (e.g., H2 + O2 = H2O).
- The program balances the reaction automatically.
- It calculates and displays molar masses.
- It generates or updates a `requirements.txt` file automatically.

---

Important Notes for Users

- Element symbols must be typed **correctly** (e.g., Cu for Copper).
- Separate compounds using `+` and reactants/products using `=`.
- Parentheses (e.g., (OH)2) are handled properly.
- Have fun balancing equations and learning chemistry!

---

Dockerization

This project was containerized using Docker.

To build and run the Docker container:

1. Build the Docker image:
    docker build -t reaction_balancer_calculator .

2. Run the container interactively:
    docker run -it reaction_balancer_calculator

Use `-it` because the program requires user input.

---

Author

Beatrice Urbaite
beatrice.urbaite@mif.stud.vu.lt
