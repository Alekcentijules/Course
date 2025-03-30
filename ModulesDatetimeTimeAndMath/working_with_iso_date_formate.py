from datetime import datetime

now = datetime.now()
iso_format = now.isoformat()

print(f"ISO format: {iso_format}")