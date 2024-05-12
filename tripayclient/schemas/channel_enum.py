from enum import Enum

class ChannelTypeEnum(str, Enum):
    """Channel Type 
    """
    mybva = "MYBVA"
    permataava = "PERMATAVA"
    bniva = "BNIVA"
    briva = "BRIVA"
    mandiriva = "MANDIRIVA"
    bcava = "BCAVA"
    muamalatva = "MUAMALATVA"
    cimbva = "CIMBVA"
    bsiva = "BSIVA"
    ocbcva = "OCBCVA"
    danamonva = "DANAMONVA"
    otherbankva = "OTHERBANKVA"
    alfamart = "ALFAMART"
    indomaret = "INDOMARET"
    alfamidi = "ALFAMIDI"
    ovo = "OVO"
    qris = "QRIS"
    qrisc = "QRISC"
    qris2 = "QRIS2"
    dana = "DANA"
    shopeepay = "SHOPEEPAY"
    qris_shopeepay = "QRIS_SHOPEEPAY"

class ModeEnum(str, Enum):
    sandbox = "https://tripay.co.id/api-sandbox/"
    prod = "https://tripay.co.id/api/"