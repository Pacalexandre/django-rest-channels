from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


def notifica_tela(serial):
    async_to_sync(channel_layer.group_send)(
        'processo', {'type': 'create_processo', 'text': serial.data})
