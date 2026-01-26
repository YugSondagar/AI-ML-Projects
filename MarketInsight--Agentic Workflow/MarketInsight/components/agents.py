from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from MarketInsight.utils.tools import *
from MarketInsight.utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,
    temperature=0
)

agent = create_react_agent(
    model=model,
    tools=[
        get_stock_price, get_historical_data, get_stock_news,
        get_balance_sheet, get_income_statement, get_cash_flow,
        get_company_info, get_dividends, get_splits,
        get_institutional_holders, get_major_shareholders,
        get_mutual_fund_holders, get_insider_transactions,
        get_analyst_recommendations,
        get_analyst_recommendations_summary,
        get_ticker
    ],
    checkpointer=MemorySaver()
)

logger.info("MarketInsight Agent initialized successfully")
