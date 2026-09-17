spam_words = [
    "free",
    "winner",
    "congratulations",
    "click here",
    "act now",
    "limited time",
    "buy now",
    "order now",
    "special offer",
    "exclusive offer",
    "cash prize",
    "you have won",
    "claim your prize",
    "claim now",
    "urgent",
    "risk free",
    "guaranteed",
    "earn money",
    "make money",
    "work from home",
    "no cost",
    "credit card",
    "lowest price",
    "save big",
    "100% free",
    "double your",
    "million dollars",
    "selected winner",
    "don't miss out",
    "once in a lifetime"
]

def check_spam(email, spam_words):
    spam_score = 0
    found_words = []

    for phrase in spam_words:
        occurrences = email.count(phrase)

        if occurrences > 0:
            spam_score += occurrences
            found_words.append(phrase)

    return spam_score, found_words

def get_likelihood(spam_score):
    if spam_score == 0:
        return "Very unlikely to be spam"
    elif spam_score <= 3:
        return "Possibly spam"
    elif spam_score <= 6:
        return "Likely spam"
    else:
        return "Very likely spam"

email = input("Enter the email message: ")
email = email.lower()

score, found_words = check_spam(email, spam_words)

likelihood = get_likelihood(score)

print("\nSpam Score:", score)
print("Likelihood:", likelihood)
print("Spam words/phrases found:")

for word in found_words:
    print("-", word)