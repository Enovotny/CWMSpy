from .utils import queryCDA
import pandas as pd
import json


class CwmsTsMixin:

    def retreive_ts_group(self,p_group_id,p_category_id,p_office_id, output = 'dataframe'):

        endPoint = f'timeseries/group/{p_group_id}'

        params = {
            "office": p_office_id,
            "category-id": p_category_id
        }

        headerList={
            "Accept": "application/json"
        }

        responce = queryCDA(self, endPoint, params, headerList, output, dict_key = 'assigned-time-series')

        #if dataframe:
        #    responce = pd.DataFrame(responce['assigned-time-series'])

        return responce

    def retrieve_ts(self, p_tsId, p_office_id=None, p_unit=None, p_datum=None, p_start_date=None, p_end_date=None, p_timezone=None, p_page_size=500, output='dataframe'):


        #creates the dataframe from the timeseries data
        endPoint = 'timeseries'
        if p_start_date is not None: p_start_date = p_start_date.strftime('%Y-%m-%dT%H:%M:%S')

        if p_end_date is not None: p_end_date = p_end_date.strftime('%Y-%m-%dT%H:%M:%S') 

        params = {
            "office": p_office_id,
            "name": p_tsId,
            "unit": p_unit,
            "begin": p_start_date,
            "end": p_end_date,
            "page-size" : p_page_size
        }

        headerList={
            "Accept": "application/json;version=2"
        }
        responce = queryCDA(self,endPoint,params,headerList,output, dict_key = 'values')

        return responce

    def write_ts(self, data, version_date = None, timezone = None, create_as_ltrs = False, store_rule = None, override_protection = None):
        params = {
                'version-date': version_date,
                'timezone': timezone,
                'create-as-lrts' : create_as_ltrs, 
                'store-rule' : store_rule,
                'override-protection' : override_protection
            }
        headerList={
                'accept': '*/*',
                'Content-Type': 'application/json;version=2',
            }
        if isinstance(data, pd.DataFrame):
            data.values.tolist()
            ts_dict = {"name": data.tsId,
                       "office-id": data.office,
                        "units": data.units,
                        "values": data.values.tolist()
                       }
        elif isinstance(data, dict): 
            ts_dict = data
        #print(ts_dict)
        response = self.s.post('timeseries', headers = headerList, data = json.dumps(ts_dict))    
        return response

