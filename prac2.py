# from dotenv import load_dotenv
# from pydantic_settings import SettingsConfigDict, BaseSettings

# # from langchain_openai import ChatOpenAI
# from langchain.agents import create_agent

# # from langchain.messages import HumanMessage
# from langchain.agents.middleware import PIIMiddleware
# from hashlib import sha256

# load_dotenv(dotenv_path=r"C:\Projects\ragas_eval\folder\.env")


# class Settings(BaseSettings):
#     OPENAI_API_KEY: str
#     OPENROUTER_API_KEY: str
#     TAVILY_API_KEY: str
#     DATABASE_URL: str
#     ASYNC_DATABASE_URL: str
#     LANGSMITH_API_KEY: str
#     model_config = SettingsConfigDict(
#         env_file=r"C:\Projects\ragas_eval\folder\.env",
#         extra="ignore",
#         case_sensitive=False,
#         env_file_encoding="utf-8",
#     )


# settings = Settings()
# hs = sha256(settings.OPENAI_API_KEY.encode("utf-8"))
# print(hs.hexdigest())

# agent = create_agent(
#     "gpt-4o",
#     middleware=[
#         PIIMiddleware("email", strategy="redact", apply_to_input=True),
#         PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),
#         PIIMiddleware(
#             "api_key",
#             detector=r"sk-[a-zA-Z0-9]{32}",
#             strategy="block",
#             apply_to_input=True,
#         ),
#     ],
# )

# # res = agent.invoke({"messages": [HumanMessage(content="Hello")]})
# # for i in res["messages"]:
# #     i.pretty_print()


# # C:\Projects\ragas_eval\folder\.env
# import asyncio
# import json
# import websockets


# async def receive_response(websocket):

#     while True:

#         response = await websocket.recv()

#         data = json.loads(response)

#         print(data)

#         if data.get("message") == "Done":
#             break


# async def main():

#     uri = "ws://localhost:8012/chat"

#     async with websockets.connect(uri) as websocket:

#         # -------------------------
#         # First request
#         # -------------------------

#         await websocket.send(json.dumps({"message": "Hello"}))

#         await receive_response(websocket)

#         print("\n\nFirst request completed\n\n")

#         # -------------------------
#         # Second request
#         # -------------------------

#         await websocket.send(json.dumps({"message": "Hello again"}))

#         await receive_response(websocket)

#         print("\n\nSecond request completed\n\n")


# if __name__ == "__main__":
#     asyncio.run(main())

# from decimal import Decimal
# from termcolor import colored

# n1: str = input(colored("Enter the first number: ", "yellow"))
# n2: str = input(colored("Enter the second number: ", "yellow"))

# if "." in n1 and "." in n2:
#     n3: Decimal = Decimal(n1) + Decimal(n2)
#     print(colored("Decimal sum is: ", "green"), n3)
#     n4: float = float(n1) + float(n2)
#     print(colored("Float sum is: ", "red"), n4)
# else:
#     print(int(n1) + int(n2))
from langchain_core.runnables import RunnableLambda, RunnableSequence


def add(numbers: list):
    a, b = numbers
    return a + b


def mul(numbers: int):
    # a, b = numbers
    return numbers * 10


r = RunnableLambda(add)
r2 = RunnableLambda(mul)
seq = RunnableSequence(first=r, last=r2)
res = r.invoke([12, 13])
print(res)

res2 = seq.invoke([12, 13])
print(res2)
