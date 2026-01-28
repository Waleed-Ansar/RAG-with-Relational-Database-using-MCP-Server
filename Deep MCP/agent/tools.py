from langchain.tools import tool
from mcp_client.mcp_client import MCPClient
import os


SERVER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "mcp_server",
    "server.py"
)

mcp = MCPClient(SERVER_PATH)

@tool
def get_person_details(name: str):
    """Get details of a person from MCP server based on name
        The name parameter is case insensitive and will be capitalized before sending to server.
    """
    result = mcp.call_tool(
        name="get_person_details",
        arguments={"name": name.capitalize()}
    )
    return f"Details are {result}"

@tool
def get_all_people():
    """Get details of all people in database from MCP server based on name
        There are no parameters, just fetch all people data from database.
    """
    result = mcp.call_tool(
        name="get_all_people",
        arguments={}
    )

    return result