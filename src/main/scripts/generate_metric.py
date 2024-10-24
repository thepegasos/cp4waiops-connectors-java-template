import json
import uuid
import time

def generate_metric(metric_name, value):
    metric = {
        "id": str(uuid.uuid4()),
        "resourceID": "database01.bigblue.com",
        "timestamp": int(time.time() * 1000),  # Current timestamp in milliseconds
        "metrics": {
            metric_name: value
        },
        "attributes": {
            "group": "CPU",
            "node": "database01.bigblue.com"
        }
    }
    return metric

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python generate_metric.py <metric_name> <value>")
        sys.exit(1)

    metric_name = sys.argv[1]
    value = float(sys.argv[2])

    metric = generate_metric(metric_name, value)
    print(json.dumps(metric))
