from agent.deep_agent import agent_executor

while True:
    q = input("Ask: ")
    if q == "x":
        break

    result = agent_executor.invoke({"input": q})
    print("\nAnswer:", result["output"])
