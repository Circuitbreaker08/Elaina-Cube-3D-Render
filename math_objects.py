from __future__ import annotations

class Vector3:
    def __init__(self, position: tuple | list [int, int, int]):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

    def __str__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __add__(self, other: Vector3):
        return Vector3(
            (
                self.x + other.x,
                self.y + other.y,
                self.z + other.z
            )
        )
    
    def __sub__(self, other: Vector3):
        return Vector3(
            (
                self.x - other.x,
                self.y - other.y,
                self.z - other.z
            )
        )
    
    def __mul__(self, other: int):
        match other:
            case other if type(other) == int:
                return Vector3(
                    (
                        self.x * other,
                        self.y * other,
                        self.z * other
                    )
                )
            case other if type(other) == Vector3:
                raise NotImplementedError("Multiplying vectors by vectors is not currently supported")

class Rotation3:
    def __init__(self, rotations: tuple | list [int, int, int]):
        self.x = rotations[0]
        self.y = rotations[1]
        self.z = rotations[2]

    def __add__(self, other: Rotation3):
        return Rotation3(
            (
                (self.x + other.x) % 360,
                (self.y + other.y) % 360,
                (self.z + other.z) % 360
            )
        )

    def __sub__(self, other: Rotation3):
        return Rotation3(
            (
                (self.x - other.x) % 360,
                (self.y - other.y) % 360,
                (self.z - other.z) % 360
            )
        )

if __name__ == "__main__":
    print(Vector3((1, 1, 1)) * 2)