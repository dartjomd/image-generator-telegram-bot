import os
from dotenv import load_dotenv

load_dotenv()
AMOUNT_OF_FREE_IMAGES = int(os.getenv("AMOUNT_OF_FREE_IMAGES"))
COST_PER_CUSTOM_GENERATION = os.getenv("COST_PER_CUSTOM_GENERATION")
COST_PER_REGULAR_GENERATION = os.getenv("COST_PER_REGULAR_GENERATION")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")

# --- Interface Texts ---
UNLOCK_IMAGE = "Unlock Image"
GENERATION_TIME = "Your masterpiece is being crafted, usually takes about 20 sec ⏳"
PICTURE_REQUEST_ERROR = "🚨 AI Server Error! Please try your request again"
PAYMENT_ERROR = "🚨 Payment was unsuccessful"
TYPE_CUSTOM_CATEGORY = "Tell us what you want to see. Type your preferences below 👇"
PREVIOUS_PICTURE_IS_LOCKED = "It looks like you have a pending image! Please finalize your previous generation before starting a new one. 😉"
CUSTOM_PROMPT_TITLE = "✨ CUSTOM PROMPT"

# --- Categories & Prompts ---
CATEGORIES = {
    "🌿 NATURE": "masterpiece, photorealistic, 8k, majestic landscape, untouched nature, deep forest, mountains or crystal clear ocean, cinematic lighting, hyper-detailed, vibrant colors, wide angle lens, high resolution",
    "🏎️ CARS": "masterpiece, photorealistic, 8k, luxury exotic sports car, sleek aerodynamic design, motion blur background, studio lighting, metallic reflections, hyper-detailed textures, carbon fiber accents, aggressive stance",
    "🏙️ CITY": "masterpiece, photorealistic, 8k, futuristic cyberpunk city or modern metropolis, neon lights, rainy street reflections, high-tech architectural detail, cinematic atmosphere, hyper-detailed, urban night life",
    "🍕 FOOD": "masterpiece, photorealistic, 8k, gourmet dish, professional food photography, macro shot, rising steam, studio lighting, appetizing textures, wooden table background, high contrast, culinary art",
    CUSTOM_PROMPT_TITLE: "",
}

CONTENT_OPTIONS = list(CATEGORIES.keys())
IMAGE_CAPTION = "✨ Your masterpiece is ready ✨"
PICUTRE_IS_ALREADY_GENERATING = "⚠️ Artist at Work! We are already busy painting your request. Please wait for the final render before placing a new order."
OHTER_CATEGORY = f"I can only generate images for the {len(CONTENT_OPTIONS)} categories below. Please select a button."
GO_TO_REFUND = (
    "❌ Sadly we couldn't resolve it automatically. Please go to <b>/refund</b>"
)

# --- Descriptions ---
DESCRIBED_CATEGORIES = """
1. <b>🌿 NATURE:</b> Breathtaking landscapes, mountains, and forests in 8K.
2. <b>🏎️ CARS:</b> The speed and elegance of luxury automotive engineering.
3. <b>🏙️ CITY:</b> The vibrant energy of metropolises and neon-lit streets.
4. <b>🍕 FOOD:</b> Mouth-watering gourmet photography and textures.
5. <b>✨ CUSTOM PROMPT:</b> Total creative freedom for your imagination."""

WELCOME_MESSAGE = f"""
<b>Welcome to the AI Art Forge</b>—your private studio for <u>photorealistic 8K art</u>.

Your mission is to generate high-resolution visuals across {len(CONTENT_OPTIONS)} premium categories. Our AI filters are tuned for realism and detail.

---

<b>Choose your Creative Direction:</b>

{DESCRIBED_CATEGORIES}

Hit one of the buttons below to <b>instantly generate</b> your first 8K masterpiece!
<i>Reminder: Only one generation can be pending at a time 🤫</i>

As a gift, we give <b>YOU</b> {AMOUNT_OF_FREE_IMAGES} free trial attempts!

<b>Pricing (After Trial Attempts):</b>
<b>Standard Categories:</b> Only <b>{COST_PER_REGULAR_GENERATION}⭐</b> per generation!
<b>{CUSTOM_PROMPT_TITLE}:</b> Full creative freedom for <b>{COST_PER_CUSTOM_GENERATION}⭐</b>!
"""

HELP_MESSAGE = f"""
👑 The <b>Art Forge</b> Codex
Welcome! I am your AI-powered image generator, ready to craft exclusive 8K masterpieces.

💰 Charges & Credits
Starter Kit: Your journey begins with {AMOUNT_OF_FREE_IMAGES} FREE CHARGES.

Cost: Once trial charges are spent, unlocking each new 8K Artifact costs {COST_PER_REGULAR_GENERATION} ⭐ (Telegram Stars).

The Active Task Rule: You can only have ONE pending generation at a time. To start a new one, you must first Unlock (Pay) or Discard the current preview.

🔮 The Vault Categories
Initiate your creation by selecting a theme:

{DESCRIBED_CATEGORIES}

🛡️ Security Guarantee
Your funds are safe: If the Forge encounters a server error or failed render, any Stars spent are automatically returned to your account.

Support: For technical glitches or payment issues, contact us via {SUPPORT_EMAIL}."""

SUPPORT_MESSAGE = f"""
📜 Forge Support Scroll
Greetings! If your quest has encountered a digital anomaly, we are here to assist.

👑 Have an idea?
Send your suggestions to {SUPPORT_EMAIL} to help us improve the Forge!

🆘 When to Seek Help
- Failed payments or missing Stars.
- Stuck generations that cannot be cleared.

🛠️ How to Contact Support
Include the following for a faster resolution:
1. Your Telegram ID (get it via <b>/myid</b>).
2. A brief description of the issue.
3. Approximate time of the incident.

Contact: {SUPPORT_EMAIL}"""

PRIVACY_POLICY_MESSAGE = f"""
🛡️ Privacy Policy
We collect minimal data to ensure service stability:
- Your Telegram User ID: To track your free limits and prevent abuse.
- Your Prompts: Shared with our Graphics Engine to generate images (your ID remains private).
We do not sell your data or share it with third parties."""

TERMS_OF_USE_MESSAGE = f"""
⚔️ Terms of Service
By using the Art Forge, you agree to these rules:
1. Ownership: You own the generated image once it is unlocked. You are granted full rights to use and commercialize your creations.
2. Responsibility: You are solely responsible for the prompts you provide and the content generated.
3. Age Requirement: You must be 18 years of age or older to use this service."""

REFUND_MESSAGE = f"""
💰 Refund Policy
Art generation is a digital, instant process.
- We do not offer refunds for successful generations once the image is unlocked.
- Technical Failures: If a payment was processed but the image was not delivered due to a crash, you may request a manual review for a refund.
To request a review, email {SUPPORT_EMAIL} with your ID and proof of purchase."""
