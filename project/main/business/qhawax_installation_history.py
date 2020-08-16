from flask import jsonify, make_response, request
from project.database.models import Qhawax
import project.main.same_function_helper as same_helper
import project.main.business.get_business_helper as get_business_helper
import project.main.business.post_business_helper as post_business_helper
from project import app

@app.route('/api/newQhawaxInstallation/', methods=['POST'])
def newQhawaxInstallation():
    """
    To create a qHAWAX in Field 
    
    Json input of following fields:
    
    :type  qhawax_id: integer
    :param qhawax_id: qHAWAX ID

    :type  lat: double
    :param lat: latitude of qHAWAX location

    :type  lon: double
    :param lon: longitude of qHAWAX location

    :type  instalation_date: timestamp
    :param instalation_date: qHAWAX Installation Date

    :type  link_report: string
    :param link_report: link of installation report

    :type  observations: string
    :param observations: installation detail

    :type  district: string
    :param district: district where qHAWAX is located

    :type  comercial_name: string
    :param comercial_name: qHAWAX comercial name

    :type  address: string
    :param address: address where qHAWAX is located

    :type  company_id: integer
    :param company_id: company ID to which qHAWAX belongs

    :type  eca_noise_id: integer
    :param eca_noise_id: ID of type of qHAWAX zone

    :type  qhawax_id: integer
    :param qhawax_id: qHAWAX ID

    :type  connection_type: string
    :param connection_type: Type of qHAWAX connection

    :type  index_type: string
    :param index_type: Type of qHAWAX index

    :type  measuring_height: integer
    :param measuring_height: Height of qHAWAX in field

    :type  season: string
    :param season: season of the year when the module was deployed

    """
    try:
        data_json = request.get_json()
        qhawax_id = data_json['qhawax_id']
        post_business_helper.storeNewQhawaxInstallation(data_json)
        post_business_helper.setOccupiedQhawax(qhawax_id)
        post_business_helper.setModeCustomer(qhawax_id)
        qhawax_name = same_helper.getQhawaxName(qhawax_id)
        description="Se registró qHAWAX en campo"
        observation_type="Interna"
        person_in_charge = data_json['person_in_charge']
        post_business_helper.writeBinnacle(qhawax_name,observation_type,description,person_in_charge)
        return make_response('OK', 200)
    except Exception as e:
        print(e)
        return make_response('Invalid format', 400)


@app.route('/api/saveEndWorkField/', methods=['POST'])
def saveEndWorkField():
    """
    Save last date of qHAWAX in field
    
    Json input of following fields:

    :type  qhawax_id: integer
    :param qhawax_id: qHAWAX ID

    :type  end_date: timestamp
    :param end_date: end date of qHAWAX installation

    """
    try:
        data_json = request.get_json()
        qhawax_id = data_json['qhawax_id']
        installation_id = helper.getInstallationId(qhawax_id)
        post_business_helper.saveEndWorkFieldDate(installation_id, data_json['end_date'])
        post_business_helper.setAvailableQhawax(qhawax_id)
        qhawax_name = same_helper.getQhawaxName(qhawax_id)
        post_business_helper.changeMode(qhawax_name, "Stand By")
        description="Se registró fin de trabajo en campo"
        observation_type="Interna"
        person_in_charge = data_json['person_in_charge']
        post_business_helper.writeBinnacle(qhawax_name,observation_type,description,person_in_charge)
        return make_response('OK', 200)
    except Exception as e:
        print(e)
        return make_response('Invalid format', 400)


@app.route('/api/AllQhawaxInMap/', methods=['GET'])
def getQhawaxInMap():
    """
    Get list of qHAWAXs filter by company ID

    Filter by company ID, the response will refer to the modules of that company

    :type  company_id: integer
    :param company_id: company ID

    """
     
    qhawax_in_field = get_business_helper.queryQhawaxInFieldInPublicMode()
    if qhawax_in_field is not None:
        qhawax_in_field_list = [installation._asdict() for installation in qhawax_in_field]
        return make_response(jsonify(qhawax_in_field_list), 200)
    else:
        return make_response(jsonify('qHAWAXs not found'), 404)


@app.route('/api/GetInstallationDate/', methods=['GET'])
def getInstallationDate():
    """
    Get installation date of qHAWAX in field

    :type  qhawax_id: integer
    :param qhawax_id: qHAWAX ID
    
    """
    try:
        qhawax_id = request.args.get('qhawax_id')
        installation_date = get_business_helper.getInstallationDateByQhawaxID(qhawax_id)
        if installation_date != None:
            installation_id = same_helper.getInstallationId(qhawax_id)
            first_timestamp = get_business_helper.getFirstTimestampValidProcessed(installation_id)
            if(first_timestamp!=None):
                if(first_timestamp>installation_date):
                    return first_timestamp
                else:
                    return installation_date
            else:
                return installation_date
        else:
            return make_response(jsonify("qHAWAX is not in field"), 200)
    except Exception as e:
        print(e)
        return make_response('No Installation Date', 400)

