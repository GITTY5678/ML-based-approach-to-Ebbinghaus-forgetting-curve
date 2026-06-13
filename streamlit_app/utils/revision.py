import math

def calculate_revision_time(retention):

    retention = max(
        1,
        min(retention, 99)
    )

    threshold = 80

    if retention <= threshold:

        return 1, 1/24

    hours = (
        retention - threshold
    ) * 4

    days = hours / 24

    return hours, days