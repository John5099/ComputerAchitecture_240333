def add(A, B):
    """Add two binary strings of equal length."""
    carry = 0
    result = ""

    for i in range(len(A) - 1, -1, -1):
        temp = int(A[i]) + int(B[i]) + carry
        result = str(temp % 2) + result
        carry = temp // 2

    return result[-len(A):]


def complement(binary):
    """Return the 2's complement of a binary string."""
    # Flip the bits
    flipped = "".join("1" if bit == "0" else "0" for bit in binary)

    # Add 1
    one = "0" * (len(binary) - 1) + "1"
    return add(flipped, one)


def non_restoring_division(dividend, divisor):
    """
    Perform Non-Restoring Division.

    Parameters:
        dividend (int): Dividend
        divisor (int): Divisor
    """

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    # Number of bits required (+1 for sign bit)
    bits = max(dividend.bit_length(), divisor.bit_length()) + 1

    Q = format(dividend, f"0{bits}b")
    M = format(divisor, f"0{bits}b")
    A = "0" * bits
    minus_M = complement(M)

    positive = True

    print("\nInitial Values")
    print("-" * 65)
    print(f"A = {A}")
    print(f"Q = {Q}")
    print(f"M = {M}")
    print("-" * 65)

    print(f"{'Step':<5} {'Operation':<22} {'A':<12} {'Q':<12}")
    print("-" * 65)

    for step in range(1, bits + 1):

        # Left Shift
        combined = A + Q
        combined = combined[1:] + "0"

        A = combined[:bits]
        Q = combined[bits:]

        # Perform operation
        if positive:
            A = add(A, minus_M)
            operation = "Shift Left & A-M"
        else:
            A = add(A, M)
            operation = "Shift Left & A+M"

        # Set Q0
        if A[0] == "1":
            Q = Q[:-1] + "0"
            positive = False
        else:
            Q = Q[:-1] + "1"
            positive = True

        print(f"{step:<5} {operation:<22} {A:<12} {Q:<12}")

    # Final Correction
    if A[0] == "1":
        print("-" * 65)
        print("Final Correction: A = A + M")
        A = add(A, M)

    print("-" * 65)
    print("Result")
    print("-" * 65)
    print(f"Quotient  = {Q}  (Decimal: {int(Q,2)})")
    print(f"Remainder = {A}  (Decimal: {int(A,2)})")


def main():
    print("=" * 45)
    print("     Non-Restoring Division Algorithm")
    print("=" * 45)

    try:
        dividend = int(input("Enter Dividend : "))
        divisor = int(input("Enter Divisor  : "))

        non_restoring_division(dividend, divisor)

    except ValueError:
        print("Please enter valid integers.")


if __name__ == "__main__":
    main()