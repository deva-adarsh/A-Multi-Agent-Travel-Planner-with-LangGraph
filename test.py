from tools.tavily_tool import tavily_search
from  tools.flight_tool import search_flights
from backend import run_travel_agent

# res=tavily_search("Best hotels in Banglore")

# res = search_flights("plan a 6 days trip to US")
# print(res)


user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])