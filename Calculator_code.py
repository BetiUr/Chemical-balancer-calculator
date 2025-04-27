import re
import sympy as sp
import periodictable
import subprocess


# Creating a file called requirements.txt with dependencies, versions, and important user instructions
def create_requirements_txt():
    dependencies = {
        'sympy': sp.__version__,
        'periodictable': periodictable.__version__,
    }

    with open('requirements.txt', 'w') as f:
        # Important rules for the user
        f.write('# All element symbols must be written correctly (e.g., copper is Cu, not CU or cu) \n')
        f.write('# Reactants and products must be separated by +, and sides separated by = \n')
        f.write('# Have fun learning chemistry with this simple app! \n')
        # Write dependencies
        for package, version in dependencies.items():
            f.write(f"{package}=={version}\n")
    print("\n✅ requirements.txt has been created with dependencies and instructions.")


# A function for splitting input chemical formulas into elements and number of them
def parse_compound(compound):
    # Expand elements in parentheses to number of elements without parentheses, like (OH)2 -> O2H2
    def expand(match):
        group = match.group(1)
        multiplier = int(match.group(2))
        expanded = ''
        tokens = re.findall(r'([A-Z][a-z]?)(\d*)', group)
        for (element, count) in tokens:
            count = int(count) if count else 1
            expanded += f"{element}{count * multiplier}"
        return expanded

    # Expand all parentheses
    while '(' in compound:
        compound = re.sub(r'\(([^()]*)\)(\d+)', expand, compound)

    # Parse flattened formula into a dictionary
    tokens = re.findall(r'([A-Z][a-z]?)(\d*)', compound)
    composition = {}
    for (element, count) in tokens:
        count = int(count) if count else 1
        composition[element] = composition.get(element, 0) + count
    return composition


# Split chemical compounds by a +
def parse_side(side):
    compounds = side.split('+')
    return [compound.strip() for compound in compounds]


# Create a matrix of element counts for reactants and products (negative values for products)
def build_matrix(reactants, products):
    all_compounds = reactants + products
    elements = sorted({elem for compound in all_compounds for elem in parse_compound(compound)})

    matrix = []
    for elem in elements:
        row = []
        for compound in reactants:
            composition = parse_compound(compound)
            row.append(composition.get(elem, 0))
        for compound in products:
            composition = parse_compound(compound)
            row.append(-composition.get(elem, 0))
        matrix.append(row)

    # Return the matrix of element counts and the list of elements
    return sp.Matrix(matrix), elements


# Function for balancing the reaction
def balance_reaction(equation):
    # Split sides by ->
    left_side, right_side = equation.split('=')
    reactants = parse_side(left_side)
    products = parse_side(right_side)

    # Create matrix and list of elements
    matrix, elements = build_matrix(reactants, products)
    num_reactants = len(reactants)
    num_products = len(products)

    # Create variables x0, x1, ...
    variables = sp.symbols(' '.join(f'x{i}' for i in range(num_reactants + num_products)))
    eqs = list(matrix * sp.Matrix(variables))

    # Set first product variable to 1
    first_product_var = variables[num_reactants]
    eqs.append(first_product_var - 1)

    # Solve system
    sol = sp.solve(eqs, variables, dict=True)

    # Raise error if no solution
    if not sol:
        raise ValueError("No solution found")

    full_sol = {}

    # Convert all values to Rational
    for v in variables:
        value = sol[0].get(v, 0)
        full_sol[v] = sp.Rational(value)

    # Scale coefficients to whole numbers
    lcm = sp.lcm([fraction.q for fraction in full_sol.values()])
    coeffs = [abs(int(c * lcm)) for c in full_sol.values()]

    # Split into reactants and products
    reactant_coeffs = coeffs[:num_reactants]
    product_coeffs = coeffs[num_reactants:]

    # Build balanced equation string
    balanced_reactants = ' + '.join(f'{c} {r}' for c, r in zip(reactant_coeffs, reactants))
    balanced_products = ' + '.join(f'{c} {p}' for c, p in zip(product_coeffs, products))

    return balanced_reactants + ' = ' + balanced_products, reactants, products, reactant_coeffs, product_coeffs


# Function for calculating molar mass
def molar_mass(compound):
    # Parse compound
    composition = parse_compound(compound)
    mass = 0.0
    for elem, count in composition.items():
        try:
            # Look up element mass
            element = getattr(periodictable, elem)
            mass += element.mass * count
        except AttributeError:
            # Raise error if element not found
            raise ValueError(f"Unknown element: {elem}")
    return mass


# Main function
def main():
    # Create requirements.txt
    create_requirements_txt()

    # Welcome message and input
    print("🔬 Welcome to the Chemical Reaction Balancer and Molar Mass Calculator!")
    equation = input("Enter a chemical reaction (e.g., H2 + O2 = H2O): ").strip()

    try:
        # Balance reaction
        balanced_eq, reactants, products, reactant_coeffs, product_coeffs = balance_reaction(equation)
        print("\n✅ Balanced Reaction:")
        print(balanced_eq)

        # Display molar masses
        print("\n📦 Molar Masses:")
        for coeff, compound in zip(reactant_coeffs, reactants):
            mass = molar_mass(compound)
            print(f"{compound}: {mass:.3f} g/mol (coefficient: {coeff})")
        for coeff, compound in zip(product_coeffs, products):
            mass = molar_mass(compound)
            print(f"{compound}: {mass:.3f} g/mol (coefficient: {coeff})")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()