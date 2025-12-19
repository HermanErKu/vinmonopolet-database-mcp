from fastmcp import FastMCP
import sqlite3
import os

mcp = FastMCP("Vinmonopolet")

db_path = os.path.join(os.path.dirname(__file__), "vinmonopolet.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

@mcp.tool
def sql(statement: str):
    """Execute a SELECT SQL statement on the Vinmonopolet products database.

    This is an MCP tool for querying the Vinmonopolet products database.
    IMPORTANT: Only SELECT statements should be used with this function.
    Do not use INSERT, UPDATE, DELETE, DROP, or any other modifying statements.

    Database Schema:
        Table: Products
        Columns:
            - Id (INT): Internal database ID
            - ProductId (TEXT): Vinmonopolet product identifier
            - ProductShortName (TEXT): Short name/description of the product
            - Percentage (REAL): Alcohol percentage
            - CostPerLiter (REAL): Price per liter

    Args:
        statement (str): A SELECT SQL statement to query the Products table.
                        Example: "SELECT * FROM Products WHERE Percentage > 10 LIMIT 5"

    Returns:
        list: A list of tuples containing the query results, where each tuple 
              represents a row from the database.

    Example:
        >>> sql("SELECT ProductShortName, Percentage FROM Products LIMIT 3")
        [('Wine Name 1', 12.5), ('Beer Name 2', 4.7), ('Spirit Name 3', 40.0)]
    """
    cursor.execute(statement)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    mcp.run()