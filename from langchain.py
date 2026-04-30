from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import datetime

# -------- LLM Setup --------
llm = ChatOpenAI(temperature=0.5)

# -------- Tools --------
def search_news(topic):
    # Mocked data (can replace with API like NewsAPI)
    return [
        "OpenAI releases new autonomous agents framework",
        "Google Gemini agents improve reasoning",
        "AI agents used in healthcare automation",
        "Multi-agent systems gaining popularity",
        "LangGraph enables better agent workflows"
    ]

def summarize_news(news_list):
    prompt = PromptTemplate.from_template(
        "Summarize these news into short bullet points:\n{news}"
    )
    return llm.predict(prompt.format(news=news_list))

def generate_newsletter(summary):
    return f"""
# 📰 Weekly AI Newsletter

## Top Updates
{summary}

---
Generated on {datetime.date.today()}
"""

def review_newsletter(content):
    prompt = PromptTemplate.from_template(
        "Review this newsletter and improve clarity:\n{content}"
    )
    return llm.predict(prompt.format(content=content))

def send_newsletter(content):
    print("\n📧 EMAIL SENT\n")
    print("Subject: Weekly AI Newsletter\n")
    print(content)

# -------- Agent --------
def run_newsletter_agent(goal, mode="auto"):
    print(f"\n🎯 Goal: {goal}")

    # Step 1: Plan
    print("\n🧠 Planning...")
    steps = [
        "Search news",
        "Summarize",
        "Generate newsletter",
        "Review",
        "Send"
    ]

    # Step 2: Research
    print("\n🔎 Researching...")
    news = search_news("AI agents")

    # Step 3: Summarize
    print("\n✍️ Summarizing...")
    summary = summarize_news(news)

    # Step 4: Generate
    print("\n📰 Generating newsletter...")
    newsletter = generate_newsletter(summary)

    # Human-in-loop option
    if mode == "human":
        print("\n👀 Review this before sending:\n")
        print(newsletter)
        approve = input("Send? (yes/no): ")
        if approve.lower() != "yes":
            print("❌ Stopped by user")
            return

    # Step 5: Self Review
    print("\n🔍 Self-reviewing...")
    final_newsletter = review_newsletter(newsletter)

    # Step 6: Send
    send_newsletter(final_newsletter)

# -------- Run --------
if __name__ == "__main__":
    goal = "Create a weekly newsletter on latest AI agent news and send it to subscribers"
    run_newsletter_agent(goal, mode="auto")  # change to "human" if needed