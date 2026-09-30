class calculator:
    """This is calculator class that has 3 methods."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """This calculate the dotproduct of 2 vecters."""

        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]

        print(f"Dot product is :{result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """This calculate the addtion of 2 vecters."""

        result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """This calculate the subtraction of 2 vecters."""

        result = [float(a * b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is : {result}")
