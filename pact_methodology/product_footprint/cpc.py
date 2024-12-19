import csv
import os


class CPC:
    """Represents a Central Product Classification (CPC) code.

    Attributes:
        code (str): The CPC code.
        title (str): The title of the CPC code.
        section (str): The section of the CPC code.
        division (str): The division of the CPC code.
        group (str): The group of the CPC code.
        class_ (str): The class of the CPC code.
        subclass (str): The subclass of the CPC code.

    Example:
        >>> cpc = CPC("0111", "Wheat")
        >>> cpc.code
        '0111'
        >>> cpc.title
        'Wheat'
        >>> cpc.section
        '0'
    """

    def __init__(self, code: str, title: str):
        """Initializes a CPC object.

        Args:
            code (str): The CPC code.
            title (str): The title of the CPC code.
        """
        self.code = code
        self.title = title
        self.section = code[0]
        self.division = code[:2]
        self.group = code[:3]
        self.class_ = code[:4]
        self.subclass = code[:5]

    def __eq__(self, other):
        """Checks equality with another CPC object.

        Example:
            >>> cpc1 = CPC("0111", "Wheat")
            >>> cpc2 = CPC("0111", "Wheat")
            >>> cpc3 = CPC("0112", "Maize (corn)")
            >>> cpc1 == cpc2
            True
            >>> cpc1 == cpc3
            False
        """
        if not isinstance(other, CPC):
            return False
        return self.code == other.code


class CPCCodeLookup:
    """A lookup table for CPC codes.

    Attributes:
        filename (str): The name of the CSV file containing the CPC codes.
        cpc_codes (dict[str, CPC]): A dictionary mapping CPC codes to CPC objects.

    Example:
        >>> lookup = CPCCodeLookup()
        >>> cpc = lookup.lookup("0111")
        >>> cpc.title
        'Wheat'
    """

    def __init__(self):
        """Initializes a CPCCodeLookup object."""
        self.filename = os.path.join(os.path.dirname(__file__), "cpc_v21.csv")
        self.cpc_codes = {}
        self.load_cpc_codes()

    def load_cpc_codes(self) -> None:
        """Loads the CPC codes from the CSV file.

        Raises:
            FileNotFoundError: If the CSV file does not exist.
            csv.Error: If there is an error reading the CSV file.
        """
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    code = row["CPC21code"]
                    title = row["CPC21title"]
                    self.cpc_codes[code] = CPC(code, title)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.filename}")
        except csv.Error as e:
            raise RuntimeError(f"Error reading CSV file: {e}")

    def lookup(self, cpc_code: str) -> CPC | None:
        """Looks up a CPC code.

        Args:
            cpc_code (str): The CPC code to look up. Must be a string of 2-5 digits.

        Returns:
            CPC | None: The CPC object corresponding to the CPC code, or None if not found.

        Raises:
            ValueError: If the CPC code is not a numerical string with a maximum length of 5.

        Example:
            >>> lookup = CPCCodeLookup()
            >>> cpc = lookup.lookup("0111")
            >>> cpc.title
            'Wheat'
            >>> lookup.lookup("99999") is None
            True
        """
        if not cpc_code:
            raise ValueError("CPC code cannot be empty")
        if len(cpc_code) > 5:
            raise ValueError("CPC code cannot be longer than 5 digits")
        if not cpc_code.isdigit():
            raise ValueError("CPC code must contain only digits")
        return self.cpc_codes.get(cpc_code, None)