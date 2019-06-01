import json

from ttdclient.models.base import Base


class SiteList(Base):

    obj_name = "sitelist"

    def getId(self):
        if self.data:
            return self.data.get("SiteListId")
        else:
            return None

    def find_by_name(self, advertiser_id, name):
        payload = { "AdvertiserId": advertiser_id,
                    "SearchTerms": [name],
                    "PageStartIndex": 0,
                    "PageSize": None }

        method = "POST"
        url = '{0}/{1}'.format(self.get_url(), 'query/advertiser')

        response = self._execute(method, url, json.dumps(payload))
        objects = self._get_response_objects(response)

        return objects
        
    def set_domains(self, domains):
        to_add = []
        domains_and_adjustments = {} 

        loader = SiteList(Base.connection)

        if self.data is not None:
            if 'SiteListId' in self.data:
                a = json.loads(loader.find(self.data['SiteListId']))
                for ttd_domain in a.get('data').get('SiteListLines'):
                    domains_and_adjustments[ttd_domain['Domain']] = ttd_domain['Adjustment']

        for domain in list(set(domains)):
            the_adjustment = 1.0
            if domain in domains_and_adjustments:
                the_adjustment = domains_and_adjustments[domain]
            to_add.append({'Domain': domain, 'adjustment': the_adjustment})

        self['SiteListLines'] = to_add
        return to_add

