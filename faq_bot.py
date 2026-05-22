import nltk
import time
from colorama import Fore, init
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize colorama
init()

# Download NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# FAQ DATA
faqs = [

    {"question": "hi hello hey good morning good evening",
     "answer": "Hello! Welcome to our support chatbot."},

    {"question": "How do I reset my password?",
     "answer": "Click Forgot Password on the login page. We will email you a reset link."},

    {"question": "What payment methods do you accept how can i pay payment options",
     "answer": "We accept Visa, Mastercard, and PayPal."},

    {"question": "refund policy refund money",
     "answer": "Refunds are processed within 5-7 business days."},

    {"question": "delivery time shipping",
     "answer": "Orders are delivered within 3-5 working days."},

    {"question": "change password update password",
     "answer": "Go to settings and choose Change Password."},

    {"question": "How do I cancel my subscription?",
     "answer": "Go to Settings, then Billing, then click Cancel Subscription."},

    {"question": "Is there a free trial?",
     "answer": "Yes! 14 days free, no credit card needed."},

    {"question": "How do I contact support?",
     "answer": "Email us at support@example.com or use live chat."},
]

# Convert FAQ text into vectors
vectorizer = TfidfVectorizer()

faq_texts = [
    f["question"] + " " + f["answer"]
    for f in faqs
]

faq_matrix = vectorizer.fit_transform(faq_texts)

# Find best matching FAQ
def find_best_faq(user_question):

    user_vector = vectorizer.transform([user_question])

    scores = cosine_similarity(user_vector, faq_matrix)

    best_index = scores.argmax()

    best_score = scores[0][best_index]

    return faqs[best_index], best_score


# CHATBOT LOOP
print(Fore.GREEN + "\n🤖 FAQ Chatbot Ready!")
print(Fore.GREEN + "Type 'quit' to exit.\n")

while True:

    user_input = input(Fore.CYAN + "You: ").strip()

    # Exit condition
    if user_input.lower() == "quit":
        print(Fore.RED + "Bot: Goodbye! 👋")
        break

    # Ignore empty input
    if not user_input:
        continue

    # Find best FAQ
    faq, score = find_best_faq(user_input)

    # Low confidence
    if score < 0.1:
        print(Fore.RED + "Bot: I don't have an answer for that. Try rephrasing!\n")

    else:
        # Typing effect
        print(Fore.YELLOW + "Bot is typing...", end="")
        time.sleep(1)

        # Show answer
        print(Fore.YELLOW + f"\rBot: {faq['answer']}")

        # Show confidence
        print(Fore.MAGENTA + f"(confidence: {round(score * 100)}%)\n")