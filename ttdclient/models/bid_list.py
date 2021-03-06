import json

from ttdclient.models.base import Base

class BidList(Base):

    obj_name = "bidlist"

    def getId(self):
        return self.get("BidListId")

    def create_bid_list(self, name, target_list='TargetList', resolution_type='SingleMatchOnly'):
        self['BidList'] = { 
            "Name": name,
            "BidListAdjustmentType": target_list,
            "ResolutionType": resolution_type,
            "BidLines": []
            }

    def set_bid_lines(self, lines):
        self['BidLines'] = lines

        response = self._execute(method, url, json.dumps(payload))
        return self._get_response_objects(response)

    def get_by_object_type(self, object_type, id):
        self.obj_name = "bidlistsummary/query/{0}/available".format(object_type)

        payload = { "EntityId": id,
                    "PageStartIndex": 0,
                    "PageSize": None }
        method = "POST"
        url = self.get_url()

        response = self._execute(method, url, json.dumps(payload))
        return self._get_response_objects(response)