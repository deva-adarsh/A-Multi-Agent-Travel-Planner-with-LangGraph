# from tools.tavily_tool import tavily_search
#vfrom  tools.flight_tool import search_flights
# from backend import run_travel_agent
import asyncio
from mcp_client_test import get_all_tools, tavily_mcp_search
# res=tavily_search("Best hotels in Banglore")

# res = search_flights("plan a 6 days trip to US")
# print(res)


# user_input = input("Enter travel request: ")

'''response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])'''


if __name__=="__main__":
    query="latest news about AI"
    asyncio.run(get_all_tools())
  #  asyncio.run(tavily_mcp_search(query))


