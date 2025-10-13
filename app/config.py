import os
from dotenv import load_dotenv


load_dotenv()
AMOUNT_OF_FREE_IMAGES = int(os.getenv("AMOUNT_OF_FREE_IMAGES"))
COST_PER_CUSTOM_GENERATION = os.getenv("COST_PER_CUSTOM_GENERATION")
COST_PER_REGULAR_GENERATION = os.getenv("COST_PER_REGULAR_GENERATION")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")

UNLOCK_IMAGE = "Unlock her"
GENERATION_TIME = "Your waifu is coming, usually takes 20 sec ⏳"
PICTURE_REQUEST_ERROR = "🚨 AI Server Down! Please try your request again"
PAYMENT_ERROR = "🚨 Payment was unsuccessful"
TYPE_CUSTOM_CATEGORY = "🤫 We will not tell anybody. Type your preferences below"
PREVIOUS_PICTURE_IS_LOCKED = "Looks like you have a ready image waiting for you! Just a quick reminder: please finalize the previous generation before starting a new one. 😉"
CUSTOM_PROMPT_TITLE = "✨ COMPLETE FREEDOM"
CATEGORIES = {
    "💦 WET SKIN": "adult, masterpiece, photorealistic, highly detailed, ultra-realistic skin texture, natural sunlight, sharp focus, 1girl, young woman, full body in shot, facing viewer, eye contact, (hips thrust up legs wide on sand | legs parted exposing pussy | wet kneeling ass up | leaning back hands spreading thighs | sitting cross-legged fingering self | seductive beach pose bent over), (blonde | light blue | pink) hair wet and tousled, nude with torn transparent clothing, expressive aroused face flushed, looking at viewer seductively, perfect natural anatomy, micro thong pulled aside, micro bikini top off, soaking wet body with water droplets, exposed breasts nipples erect, deep cleavage, sunlight shimmering on oiled skin, 8k, beach setting, lifelike proportions",
    "🖤 LATEX PLAY": "adult, masterpiece, photorealistic, ultra-detailed, realistic skin, natural lighting, 1girl, full body, facing viewer, eye contact, (hips thrust up legs spread | arching back | legs apart on bed | leaning forward knees ass up | looking over shoulder | hands on bare breasts), random hair color flowing, nude in torn wet latex bunny suit, fabric ripped open, zipper unzipped exposing all, torn fishnets, loose garter, revealing labia, nipples visible, oiled sweaty skin, large natural bust, aroused expression, dramatic backlighting, soft shadows, 8k, lifelike proportions",
    "🦵 THIGH-HIGH": "masterpiece, photorealistic, ultra-detailed, realistic skin, natural lighting, sharp focus, clean lines, 1girl, full body shot, facing viewer, eye contact, (reclining on back legs spread | sitting on bed edge knees apart | legs up spread on bed | wide leg spread on sheets | prone on stomach ass up | seductive sitting with open legs), thigh-high stockings, (blonde | black | purple | brown) hair flowing naturally, garter belt loose, nude with exposed breasts and pussy, above average natural bust with sag, legs bent aroused, shy aroused gaze, intricate natural face, gentle flushed expression, intimate lighting, soft shadows, luxury bedroom, 8k, lifelike proportions",
    "🛁 BATHROOM INTIMACY": "adult, masterpiece, ultra-detailed, 1girl, full body shot, facing viewer, eye contact, (leaning forward on sink | sitting on edge of tub with legs spread | wet kneeling pose in shower | wet hair draped forward), (no clothing | nude | bare breasts | exposed pussy), transparent water droplets on skin, soaking wet body, steamy atmosphere, soft focus, bathroom, intimate lighting, sharp focus, 8k",
    CUSTOM_PROMPT_TITLE: "",
}
CONTENT_OPTIONS = list(CATEGORIES.keys())
IMAGE_CAPTION = "✨ Here she is ✨"
PICUTRE_IS_ALREADY_GENERATING = "⚠️ Artist at Work! We are already busy painting your masterpiece. Please wait for the final render before placing a new order."
OHTER_CATEGORY = f"I can only generate images for the {len(CONTENT_OPTIONS)} categories below. Please select a button."
EXCLUDE = "child, nsfw, naked, boring, dull expression, lowres, jpeg artifacts, blurry, bad art, red oversaturation, bad color, monochromatic red, gross, blurry background, out of focus, hazy, low detail, low quality, watermark, text, out of frame"
GO_TO_REFUND = (
    "❌ Sadly we couldn't resolve it automatically. Please go to <b>/refund</b>"
)


DESCRIBED_CATEGORIES = """
1.  <b>💦 WET SKIN:</b> The raw, wet aesthetic of the beach and micro bikini.
2.  <b>🖤 LATEX PLAY:</b> The high shine, stockings, and full freedom of the bunny suit.
3.  <b>🦵 THIGH-HIGH:</b> Intimate scenes, focusing on seductive stockings and pose.
4.  <b>🛁 BATHROOM INTIMACY:</b> The wet, steamy atmosphere of a luxury bathroom or shower.
5.  <b>✨ COMPLETE FREEDOM:</b> Be the creator of your dreams."""


WELCOME_MESSAGE = f"""
<b>Welcome to Pixel Sin</b>—your private vault for <u>unfiltered 8K anime art</u>.

Your mission is to secure the <b>access key</b> to one of our {len(CONTENT_OPTIONS)} forbidden categories. Filters are off, and censorship is asleep.

---

<b>Choose your Access Level:</b>

{DESCRIBED_CATEGORIES}

Hit one of the buttons below to <b>instantly generate</b> your first 8K masterpiece!
Psss... <i>only one girl can be pending🤫</i>

<b>⚔️ Guild Master's Warning:</b>
The Forge is powerful, but even it has limits. **Overly aggressive or explicit commands** are catched by default. Keep your requests focused and creative!

As a gift we give <b>YOU</b> {AMOUNT_OF_FREE_IMAGES} trial attempts!

<b>The Price List (After Trial Attempts):</b>
<b>Standard Categories:</b> Only <b>{COST_PER_REGULAR_GENERATION}⭐</b> per girl!
<b>{CUSTOM_PROMPT_TITLE}:</b> Full creative freedom costs <b>{COST_PER_CUSTOM_GENERATION}⭐</b> per girl!
"""


HELP_MESSAGE = f"""
👑 The <b>Pixel Sin's</b> Codex
Welcome, Sinner! I am your AI-powered Artifact Forge, ready to craft exclusive 8K masterpieces. Your quest for high-detail art begins here.

💰 Charges & Artifact Quests
Starter Kit: Your journey begins with 3 FREE CHARGES (Trial Attempts) to test the Forge's power. Check your status during generation.

Artifact Cost: Once your free charges are spent, unlocking each new 8K Artifact costs just {COST_PER_REGULAR_GENERATION} ⭐ (Telegram Star). That's a Legendary Deal for a high-resolution, private masterpiece!

The Single Quest Rule: You can only have ONE active, pending Artifact at a time. To start a new creation, you must first Reveal (Pay) or Discard the current preview.

🔮 The Vault Categories
Initiate your quest by selecting your desired theme:

{DESCRIBED_CATEGORIES}

🛡️ The Guild's Guarantee
Your funds are safe:

Failed Quests: If the Forge breaks during the craft (server error, failed render), any Stars spent are automatically returned to your Telegram Stars account.

Support Scroll: For payment issues, technical glitches, or support, contact the Guild Master via {SUPPORT_EMAIL}.

👉 Commence your quest by selecting a category!"""
SUPPORT_MESSAGE = f"""
📜 The Guild Support Scroll
Greetings, Whisperer! If your quest has encountered a digital anomaly, the Guild is here to assist.

👑 You have an idea?
Send to us({SUPPORT_EMAIL}) your idea to support community of freedom seekers!

🆘 When to Seek Help
Before contacting us, please check the following:

Missing Stars/Failed Quests: Did you encounter an error during the payment or generation process? (Remember: Stars are usually auto-refunded if the AI fails the render).

Active Order: Do you have an active, pending Artifact that you cannot delete?

🛠️ How to Contact the Guild Master
For the fastest resolution, please contact us via the channel below and include ALL required details.

Contact Channel:
{SUPPORT_EMAIL}

Required Details (Must Include):

Your Telegram user ID(you can get it from <b>/myid</b>)

The Issue: A short description of the problem (e.g., "Payment went through, but image was not delivered").

Time: The approximate time (and date) the issue occurred.

Artifact ID (If applicable): If you still have the message with the receipt.

⏳ Support Response Time
The Guild Master is often busy, but we will try to respond ASAP. Please do not spam the channel; multiple messages will only reset your place in the queue.

We appreciate your patience as we maintain the Artifact Forge!"""
PRIVACY_POLICY_MESSAGE = f"""
🛡️ Privacy Policy: The Scroll of Secrecy
Welcome, Adventurer! Our quest is to generate stunning art, and to do that, we collect minimal data—just enough to keep the server running smoothly and to level up your experience.

Your Gamer Tag (User ID) and Server Join Time: We only collect your unique Telegram User ID and the time you started interacting with the Bot. We call this your "Gamer Tag" and "Server Join Time." This data is essential for tracking your free image limit, preventing abuse, and ensuring the Bot functions correctly.

Quest Details (Prompts): The text prompts you send are shared with our powerful Graphics Engine, Replicate AI, which generates the images. However, your personal Gamer Tag (User ID) is never shared with them.

Data Usage: Your data is used exclusively for the operation, security, and continuous improvement of this art generation service. We don't sell it or share it with other realms.

Data Security: Your personal information is treated as high-value loot and stored securely."""
TERMS_OF_USE_MESSAGE = f"""
⚔️ Terms of Service: The Code of Conduct
By using our Art Forge, you agree to these fundamental rules of the realm:

Ownership of Artifacts (Content): You are the Master Artist! Once an image is generated and unlocked, you own the content (the "Artifact"). You are granted full rights to use, share, and commercialize the image you created.

Responsibility for Creation: We provide the brush and the canvas, but you provide the vision (the prompt). You take full and sole responsibility for the content you generate and any consequences resulting from its creation, distribution, or storage. This Bot is simply a tool. We are not liable for any content that may be deemed offensive, illegal, or inappropriate, or for any claims arising from your use of the generated images.

The Age Requirement: To participate in the Art Forge, you must be 18 years of age or older (or the age of legal majority in your jurisdiction). By using this service, you confirm that you meet this requirement."""
REFUND_MESSAGE = f"""
💰 Refund Policy: The Scroll of Reversal
Art generation is an instantaneous and digital process—like casting a spell, once it's done, it cannot be undone.

No Automatic Reversals: We generally do not offer refunds for successful generations. When you unlock an image, the resources have been spent, and the deed is done.

Technical Failure Exception: If you paid for an image, but the Bot encountered a critical technical failure (e.g., the Bot crashed before sending the unlocked image, and your account status wasn't correctly updated), you may submit a request for a manual review and possible credit or refund.

How to Request a Review: To appeal to the High Council (our support team), send an email to [YOUR SUPPORT EMAIL HERE] with the following items:

Your full Telegram user ID(execute <b>/myid</b>).

A detailed Message explaining the technical issue.

The Proof of Purchase (Payment Receipt/Screenshot)."""
