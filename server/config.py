import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/your_db")
FLIPP_API_URL = "https://flipp-undocumented/api/flyers"
