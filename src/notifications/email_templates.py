"""
==========================================================
IntentIQ

File: email_templates.py

Description:
Contains reusable email templates for notifications.

Author: Arjun S Nair
==========================================================
"""

def generate_price_drop_subject(notification):
    """
    Generates the subject for a price drop email.
    """

    return (
        f"🎉 Price Drop Alert - "
        f"{notification['product_name']}"
    )



def generate_price_drop_text(notification):
    """
    Generates the body for a price drop email.
    """

    return f"""
Hi,

Good news!

The product you are tracking has reached your target price.

--------------------------------------------------------

Product:
{notification['product_name']}

Store:
{notification['store_name']}

Current Price:
₹{notification['price']:,.0f}

Your Target Price:
₹{notification['current_target_price']:,.0f}

Product Link:
{notification['product_url']}

--------------------------------------------------------

Happy shopping!

- IntentIQ

"""


def generate_price_drop_html(notification):

    return f"""
<html>

<body
style="
font-family:Arial;
background:#f4f4f4;
padding:40px;
">

<div
style="
max-width:600px;
margin:auto;
background:white;
padding:30px;
border-radius:10px;
">

<h1 style="color:#2563eb;">
🎯 IntentIQ
</h1>

<h2>
Price Drop Alert!
</h2>

<p>

Good news!

Your tracked product has reached your target price.

</p>

<hr>

<p>

<b>Product</b><br>

{notification['product_name']}

</p>

<p>

<b>Store</b><br>

{notification['store_name']}

</p>

<p>

<b>Current Price</b><br>

<span
style="
font-size:28px;
color:#16a34a;
font-weight:bold;
">

₹{notification['price']:,.0f}

</span>

</p>

<p>

<b>Your Target</b><br>

₹{notification['current_target_price']:,.0f}

</p>

<p>

<a
href="{notification['product_url']}"
style="
display:inline-block;
padding:14px 22px;
background:#2563eb;
color:white;
text-decoration:none;
border-radius:8px;
">

Buy Now

</a>

</p>

<hr>

<p
style="
font-size:13px;
color:#777;
">

Thank you for using IntentIQ.

</p>

</div>

</body>

</html>
"""