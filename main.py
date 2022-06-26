from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

host = "http://127.0.0.1:6666"
app = Ariadne(
    connection=config(
        114514,
        "114514_key",
        HttpClientConfig(host),
        WebsocketClientConfig(host),
    ),
)


@app.broadcast.receiver(GroupMessage)
async def main(app: Ariadne, group: Group, message: MessageChain):
    ans = (
        message.display.replace("你", "我")
        .replace("吗", "")
        .replace("?", "!")
        .replace("？", "！")
    )
    if ans != message.display:
        await app.send_message(
            group,
            MessageChain(),
        )


app.launch_blocking()
