
def central_difference(f: Any, *vals: Any, arg: int = 0, epsilon: float = 1e-06) -> Any:
    return (f(vals[0]+epsilon)-f(vals[0]-epsilon))/2*epsilon