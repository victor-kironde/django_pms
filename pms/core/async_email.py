import asyncio
from aiohttp import ClientSession
from django.core.mail import send_mail


# async def send_email(subject, message, from_email, to_emails, fail_silently):
#     async with ClientSession() as session:
#         async with send_mail(subject, message, from_email, to_emails, fail_silently=False) as response:
#             response = await response.read()
#             print(response)

# loop = asyncio.get_event_loop()
#
# loop.run_until_complete(send_emai("http://httpbin.org/headers"))

async def send_email(subject, message, from_email, to_emails, fail_silently):
    # tasks = []
    # task = asyncio.ensure_future(
    #     send_mail(subject, message, from_email, to_emails, fail_silently=False))
    # tasks.append(task)
    await send_mail(subject, message, from_email, to_emails, fail_silently=False)
