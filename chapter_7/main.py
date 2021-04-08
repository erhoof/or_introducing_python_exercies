import binascii
import re
from construct import Struct, Const, Int16ub
import struct

if __name__ == '__main__':
    mystery = '\U0001f4a9'
    pop_bytes = bytes(mystery.encode('utf-8'))
    print(pop_bytes)
    pop_string = pop_bytes.decode('utf-8')
    print(pop_string)
    print(mystery)
    poem = """My kitty cat likes %s
    My kitty cat likes %s
    My kitty cat fell on his %s
    And now thinks he's a %s""" % ('roast beef', 'ham', 'head', 'clam')
    print(poem)

    response = {'salutation': 'hehe',
                'name': 'pavel',
                'product': 'tv',
                'verbed': 'showed',
                'room': 'big',
                'animals': 'cats',
                'amount': 'a lot',
                'percent': '100%',
                'spokesman': 'me',
                'job_title': 'it'}
    letter = """Dear {salutation} {name},
      Thank you for your letter. We are sorry that our {product} {verbed} in your
      {room}. Please note that it should never be used in a {room}, especially
      near any {animals}.
      Send us your receipt and {amount} for shipping and handling. We will send
      you another {product} that, in our tests, is {percent}% less likely to
      have {verbed}.
      Thank you for your support.
      Sincerely,
      {spokesman}
      {job_title}""".format(**response)
    print(letter)

    mammoth = """We have seen thee, queen of cheese,
    Lying quietly at your ease,
    Gently fanned by evening breeze,
    Thy fair form no flies dare seize.
    All gaily dressed soon you'll go
    To the great Provincial show,
    To be admired by many a beau
    In the city of Toronto.
    Cows numerous as a swarm of bees,
    Or as the leaves upon the trees,
    It did require to make thee please,
    And stand unrivalled, queen of cheese.
    May you not receive a scar as
    We have heard that Mr. Harris
    Intends to send you off as far as
    The great world's show at Paris.
    Of the youth beware of these,
    For some of them might rudely squeeze
    And bite your cheek, then songs or glees
    We could not sing, oh! queen of cheese.
    We'rt thou suspended from balloon,
    You'd cast a shade even at noon,
    Folks would think it was the moon
    About to fall and crush them soon."""

    out = re.findall(r'\bs\S*', mammoth)
    print(out)

    out = re.findall(r'\bc...\b', mammoth)
    print(out)

    out = re.findall(r'\w*r\b', mammoth)
    print(out)

    out = re.findall(r'\w*[aeyiuo]{3}\S*', mammoth)
    print(out)

    gif = bytes(binascii.unhexlify('47494638396101000100800000000000ffffff21f9' +
    '0401000000002c000000000100010000020144003b'))

    fmt = Struct(
        'signature' / Const(b'GIF89a'),
        'width' / Int16ub,
        'height' / Int16ub
        )
    result = fmt.parse(gif)
    print(result)

    print(len(gif))
    print(struct.unpack('>6x2h32x', gif))





