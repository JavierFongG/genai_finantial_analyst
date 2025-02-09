from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.googlesearch import GoogleSearch
from phi.tools.yfinance import YFinanceTools

import os 
from dotenv import load_dotenv  

load_dotenv()   

retriever_agent =  Agent(  
    name="Finance Data Agent",  
    model=Groq(id="llama-3.3-70b-versatile"),  
    role="Analyze financial data for the long run",  
    tools=[  
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),  
    ],  
    instructions=["Use bullet points to display the data and add a summary"] 
)  

agent_team = Agent(
      model=Groq(id="deepseek-r1-distill-llama-70b"),  
      team = [retriever_agent], 
      intructions = ["Present the finantial data, summarise it and give advice accordingly"],  
)

def agents_response(query : str = None)-> str : 
    response = agent_team.run(query)
    return (response.content)

