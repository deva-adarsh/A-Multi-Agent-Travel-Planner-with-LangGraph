from tools.tavily_tool import tavily_search
from  tools.flight_tool import search_flights
# res=tavily_search("Best hotels in Banglore")

res = search_flights("plan a 6 days trip to US")
print(res)