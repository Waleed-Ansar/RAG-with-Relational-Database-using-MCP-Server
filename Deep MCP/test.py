# import psycopg2

# def get_all_people() -> list[dict]:
#     data = []
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             dbname="postgres",
#             port=5432,
#             user="postgres",
#             password=12345
#         )
#         cur = conn.cursor()
#         cur.execute(
#             "SELECT * FROM mcp_test" 
#         )

#         rows = cur.fetchall()
#         conn.close()
#         if rows:
#             for row in rows:
#                 info = {
#                         "name": row[1],
#                         "age": row[2],
#                         "gender": row[3],
#                         "profession": row[4],
#                         "about": row[5],
#                         "contact": row[6]
#                     }
#                 data.append(info)
        
#             return data

#         else:
#             return {"error": "No users found"}

#     except Exception as e:
#         return {"error": str(e)}

# print(get_all_people())

import psycopg2


def get_all_people() -> list[dict]:
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
            return [
                {
                    "name": row[1],
                    "age": row[2],
                    "gender": row[3],
                    "profession": row[4],
                    "about": row[5],
                    "contact": row[6]
                }
                for row in rows
            ]
        else:
            return {"error": "No users found"}

    except Exception as e:
        return {"error": str(e)}

print(get_all_people())