from mcp.server.fastmcp import FastMCP
import psycopg2
import json

mcp = FastMCP("Postgres MCP")

@mcp.tool()
def get_person_details(name: str):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="postgres",
            port=5432,
            user="postgres",
            password=12345
        )
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM mcp_test WHERE name = %s", 
            (name,)
        )

        row = cur.fetchone()
        conn.close()

        if row:
            return {
                "name": row[1],
                "age": row[2],
                "gender": row[3],
                "profession": row[4],
                "about": row[5],
                "contact": row[6]
            }
        else:
            return {"error": "User not found"}

    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_all_people():
    data = []
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="postgres",
            port=5432,
            user="postgres",
            password=12345
        )
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM mcp_test" 
        )

        rows = cur.fetchall()
        conn.close()
        if rows:
            for row in rows:
                info = {
                        "name": row[1],
                        "age": row[2],
                        "gender": row[3],
                        "profession": row[4],
                        "about": row[5],
                        "contact": row[6]
                    }
                data.append(info)
        
            return json.dumps(data, indent=2)

        else:
            return {"error": "No users found"}

    except Exception as e:
        return {"error": str(e)}