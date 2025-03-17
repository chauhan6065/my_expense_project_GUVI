from sqlalchemy import create_engine

# Database connection details
HOST = "localhost"
USER = "root"  # Replace with your MySQL username
PASSWORD = "12345"  # Replace with your MySQL password
DATABASE = "expense_tracker"

# Create an SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")
