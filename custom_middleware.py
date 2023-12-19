class CustomMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http':
            async def wrapped_send(response):
                response_headers = [
                    (b'Content-Type', b'text/plain'),
                    # Add any additional headers here
                ]
                await send({
                    'type': 'http.response.start',
                    'status': response['status'],
                    'headers': response_headers,
                })
                await send({
                    'type': 'http.response.body',
                    'body': response['body'],
                    'more_body': False  # This tells Uvicorn there is no more body to send
                })

            await self.app(scope, receive, wrapped_send)
        else:
            await self.app(scope, receive, send)
