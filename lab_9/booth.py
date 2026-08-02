def to_signed(value, width):
    """Convert an unsigned binary value to a signed integer."""
    if value & (1 << (width - 1)):
        value -= (1 << width)
    return value


def booths_algorithm(multiplicand, multiplier, bits=8):
    """
    Perform Booth's multiplication algorithm.

    Parameters:
        multiplicand (int): First number
        multiplier (int): Second number
        bits (int): Number of bits (default = 8)

    Returns:
        int: Product of multiplicand and multiplier
    """

    mask = (1 << bits) - 1

    # Registers
    A = 0
    Q = multiplier & mask
    Q_1 = 0
    M = multiplicand & mask

    print("\nBooth's Algorithm Steps")
    print("-" * 72)
    print(f"{'Step':<5} {'Q0Q-1':<7} {'Operation':<18} {'A':<10} {'Q':<10} {'Q-1'}")
    print("-" * 72)
    print(f"{'Init':<5} {'-':<7} {'-':<18} {A:0{bits}b}   {Q:0{bits}b}   {Q_1}")

    for step in range(1, bits + 1):

        # Store Q0Q-1 before operation
        q_pair = f"{Q & 1}{Q_1}"

        # Decide operation
        if (Q & 1, Q_1) == (1, 0):
            A = (A - M) & mask
            operation = "A = A - M"

        elif (Q & 1, Q_1) == (0, 1):
            A = (A + M) & mask
            operation = "A = A + M"

        else:
            operation = "No Operation"

        # Combine registers
        combined = (A << (bits + 1)) | (Q << 1) | Q_1

        # Arithmetic right shift
        sign = (A >> (bits - 1)) & 1
        combined >>= 1
        combined |= sign << (2 * bits)

        # Separate registers
        Q_1 = combined & 1
        Q = (combined >> 1) & mask
        A = (combined >> (bits + 1)) & mask

        print(f"{step:<5} {q_pair:<7} {operation:<18} {A:0{bits}b}   {Q:0{bits}b}   {Q_1}")

    result = (A << bits) | Q
    return to_signed(result, 2 * bits)


def get_input(name, bits=8):
    """Get valid signed integer input."""

    lower = -(1 << (bits - 1))
    upper = (1 << (bits - 1)) - 1

    while True:
        try:
            value = int(input(f"Enter {name} ({lower} to {upper}): "))
            if lower <= value <= upper:
                return value
            print(f"Please enter a value between {lower} and {upper}.")
        except ValueError:
            print("Invalid input! Please enter an integer.")


def main():
    bits = 8

    print("=" * 50)
    print("        Booth's Algorithm Multiplication")
    print("=" * 50)

    multiplicand = get_input("Multiplicand", bits)
    multiplier = get_input("Multiplier", bits)

    result = booths_algorithm(multiplicand, multiplier, bits)

    print("\n" + "=" * 50)
    print(f"Multiplicand : {multiplicand}")
    print(f"Multiplier   : {multiplier}")
    print(f"Product      : {result}")
    print(f"Verification : {multiplicand * multiplier}")
    print("=" * 50)


if __name__ == "__main__":
    main()