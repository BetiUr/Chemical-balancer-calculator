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
    git clone https://github.com/BetiUr/Chemical-balancer-calculator.git
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

To build and run the Docker container these steps were done:
1. The working directory of my project was set
   cd C:/Users/Beatrice/PycharmProjects/PythonProject2/.venv

2. The Docker image was built:
    docker build -t reaction_balancer_calculator .

3. Run the container interactively:
    docker run -it reaction_balancer_calculator
   
4. Expected output
   🔬 Welcome to the Chemical Reaction Balancer and Molar Mass Calculator!
Enter a chemical reaction (e.g., H2 + O2 = H2O):

If the reaction given in the example is used, the expected output is:

✅ Balanced Reaction:
2 H2 + 1 O2 = 2 H2O

📦 Molar Masses:
H2: 2.016 g/mol (coefficient: 2)
O2: 31.998 g/mol (coefficient: 1)
H2O: 18.015 g/mol (coefficient: 2)

Some examples for trying out the calculator:
- C3H8+O2=CO2+H2O
- N2O5=NO2+O2
- CaCl2+AgNO3=AgCl+Ca(NO3)2

---

Docker Hub Details

- The Docker image for this project has been pushed to Docker Hub.

Docker Image Tag:
    betiur/reaction_balancer_calculator:v1.0

You can pull and run the image using the following command:

    docker pull betiur/reaction_balancer_calculator:v1.0
    docker run -it betiur/reaction_balancer_calculator:v1.0

---

Author

Beatrice Urbaite
beatrice.urbaite@mif.stud.vu.lt
