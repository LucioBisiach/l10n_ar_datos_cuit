from odoo import fields, models

import requests
import urllib
import json

import logging
_logger = logging.getLogger(__name__)

class inheritResPartnerTms(models.Model):
    _inherit = 'res.partner'

    API_TANGO_URL = 'https://afip.tangofactura.com/Rest/GetContribuyenteFull?cuit='

    def get_data_afip(self):
        res = requests.get(self.API_TANGO_URL + self.vat)
        _logger.info("RESPUESTA %s", res)

        if res.status_code == 200:
            _logger.info("Respuesta 200, OK")
            jsonObject = res.json()
            _logger.info(jsonObject)
            for dato in jsonObject['Contribuyente']:
                _logger.info("CUIT ", str(dato['idPersona']))
            
