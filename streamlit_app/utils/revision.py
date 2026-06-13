import numpy as np

def calculate_revision_time(
    memory_strength,
    threshold=80
):

    hours = (
        -memory_strength
        * np.log(threshold / 100)
    )

    days = hours / 24

    return hours, days