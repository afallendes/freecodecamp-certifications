import numpy as np


def calculate(lst: list) -> dict:
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    def calculation(method_name: str, *args, **kwargs):
        if method_name == "mean":
            return np.mean(*args, **kwargs)
        elif method_name == "variance":
            return np.var(*args, **kwargs)
        elif method_name == "standard deviation":
            return np.std(*args, **kwargs)
        elif method_name == "max":
            return np.max(*args, **kwargs)
        elif method_name == "min":
            return np.min(*args, **kwargs)
        elif method_name == "sum":
            return np.sum(*args, **kwargs)
        else:
            raise NotImplementedError("Provide an implemented method.")

    mtx = np.array(lst).reshape(3, 3)

    return {
        method_name: [
            list(calculation(method_name, mtx, axis=0)),
            list(calculation(method_name, mtx, axis=1)),
            calculation(method_name, lst),
        ]
        for method_name in [
            "mean",
            "variance",
            "standard deviation",
            "max",
            "min",
            "sum"
        ]
    }