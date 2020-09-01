import unittest
import datetime
from datetime import timedelta
import project.main.business.get_business_helper as get_business_helper

class TestGetBusinessHelper(unittest.TestCase):
	"""
	Test of Get Business Functions

	"""
	def test_query_time_qhawax_history_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getTimeQhawaxHistory)
		self.assertRaises(TypeError,get_business_helper.getTimeQhawaxHistory,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.getTimeQhawaxHistory,4.33)
		self.assertRaises(TypeError,get_business_helper.getTimeQhawaxHistory,5)
		self.assertRaises(TypeError,get_business_helper.getTimeQhawaxHistory,None)
		self.assertRaises(TypeError,get_business_helper.getTimeQhawaxHistory,True)

	def test_query_qhawax_mode_customer_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,4.33)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,5)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,None)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,True)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,10,None)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,"String_")

	def test_query_get_areas_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,4.33)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,5)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,None)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,True)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,10,None)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,"String_")

	def test_query_get_areas_valid(self):
		area_list = [(4, 'Zona Industrial'),(3, 'Zona Comercial'),(2, 'Zona Residencial'), \
					 (1, 'Zona de Protección Especial')]
		self.assertAlmostEqual(get_business_helper.queryGetAreas(),area_list)

	def test_query_get_eca_noise_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise)
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,{"eca_noise_id":1})
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,True)
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,None)
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,4.33)
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,"PUCP")
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,1, True)

	def test_query_get_eca_noise(self):
		e1 = (1, 'Zona de Protección Especial', 50, 40)
		e2 = (2, 'Zona Residencial', 60, 50)
		self.assertAlmostEqual(get_business_helper.queryGetEcaNoise(1),e1)
		self.assertAlmostEqual(get_business_helper.queryGetEcaNoise(2),e2)

	def test_query_get_offsets_from_productID_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getOffsetsFromProductID)
		self.assertRaises(TypeError,get_business_helper.getOffsetsFromProductID,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.getOffsetsFromProductID,4.33)
		self.assertRaises(TypeError,get_business_helper.getOffsetsFromProductID,None)
		self.assertRaises(TypeError,get_business_helper.getOffsetsFromProductID,True)
		self.assertRaises(TypeError,get_business_helper.getOffsetsFromProductID,"qH001",1)

	def test_query_get_offsets_from_productID(self):
		qhawax_name= 'qH001'
		offset_sensor ={'CO': {'WE': 0.0, 'AE': 0.0, 'sensitivity': 0.0, 'sensitivity_2': 0.0}, 
					   'SO2': {'WE': 0.0, 'AE': 0.0, 'sensitivity': 0.0, 'sensitivity_2': 0.0}, 
		               'H2S': {'WE': 0.0, 'AE': 0.0, 'sensitivity': 0.0, 'sensitivity_2': 0.0}, 
		                'O3': {'WE': 0.0, 'AE': 0.0, 'sensitivity': 0.0, 'sensitivity_2': 0.0}, 
		                'NO': {'WE': 0.0, 'AE': 0.0, 'sensitivity': 0.0, 'sensitivity_2': 0.0}, 
		               'NO2': {'WE': 0.0, 'AE': 0.0, 'sensitivity': 0.0, 'sensitivity_2': 0.0}}
		self.assertAlmostEqual(get_business_helper.getOffsetsFromProductID(qhawax_name),offset_sensor)

	def test_query_get_controlled_offsets_from_productID_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getControlledOffsetsFromProductID)
		self.assertRaises(TypeError,get_business_helper.getControlledOffsetsFromProductID,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.getControlledOffsetsFromProductID,4)
		self.assertRaises(TypeError,get_business_helper.getControlledOffsetsFromProductID,None)
		self.assertRaises(TypeError,get_business_helper.getControlledOffsetsFromProductID,True)
		self.assertRaises(TypeError,get_business_helper.getControlledOffsetsFromProductID,"qH001",1)

	def test_query_get_controlled_offsets_from_productID(self):
		qhawax_name= 'qH004'
		offset_sensor ={'CO': {'C2': 0.0, 'C1': 0.0, 'C0': 1.0}, 
		                'SO2': {'C2': 0.0, 'C1': 0.0, 'C0': 0.0}, 
		                'H2S': {'C2': 0.0, 'C1': 0.0, 'C0': 2.0}, 
		                'O3': {'C2': 0.0, 'C1': 0.0, 'C0': 0.0}, 
		                'NO': {'C2': 0.0, 'C1': 0.0, 'C0': 4.0}, 
		                'NO2': {'C2': 0.0, 'C1': 0.0, 'C0': 4.0}}
		self.assertAlmostEqual(get_business_helper.getControlledOffsetsFromProductID(qhawax_name),offset_sensor)

	def test_query_get_non_controlled_offsets_from_productID_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getNonControlledOffsetsFromProductID)
		self.assertRaises(TypeError,get_business_helper.getNonControlledOffsetsFromProductID,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.getNonControlledOffsetsFromProductID,4)
		self.assertRaises(TypeError,get_business_helper.getNonControlledOffsetsFromProductID,None)
		self.assertRaises(TypeError,get_business_helper.getNonControlledOffsetsFromProductID,True)
		self.assertRaises(TypeError,get_business_helper.getNonControlledOffsetsFromProductID,"qH001",1)

	def test_query_get_non_controlled_offsets_from_productID(self):
		qhawax_name= 'qH001'
		offset_sensor ={'CO': {'NC1': 0.0, 'NC0': 0.0}, 
		               'SO2': {'NC1': 0.0, 'NC0': 1.0}, 
		               'H2S': {'NC1': 0.0, 'NC0': 0.0}, 
		                'O3': {'NC1': 0.0, 'NC0': 2.0}, 
		                'NO': {'NC1': 0.0, 'NC0': 0.0}, 
		               'NO2': {'NC1': 0.0, 'NC0': 0.0}}
		self.assertAlmostEqual(get_business_helper.getNonControlledOffsetsFromProductID(qhawax_name),offset_sensor)

	def test_query_inca_qhawax_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax)
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,4)
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,None)
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,True)
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,"qH001",1)

	def test_query_inca_qhawax(self):
		e1 = "green"
		self.assertAlmostEqual(get_business_helper.queryIncaQhawax("qH001"),e1)

	def test_get_installation_date_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getInstallationDate)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,True)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,4.5)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,None)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,"342")

	def test_get_first_time_valid_processed_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed)
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed,True)
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed,4.5)
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed,None)
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed,"342")

	def test_get_last_qhawax_id_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,40)
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,True)
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,4.5)
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,None)
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,"342")

	def test_get_last_gas_sensor_id_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,40)
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,True)
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,4.5)
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,None)
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,"342")

	def test_qhawax_in_field_valid(self):
		self.assertAlmostEqual(get_business_helper.isItFieldQhawax("qH002"),False)
		self.assertAlmostEqual(get_business_helper.isItFieldQhawax("qH004"),True)

	def test_qhawax_in_field_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,40)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,True)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,4.5)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,None)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,{"name":"qH001"})

	def test_get_qhawax_latest_timestamp_processed_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,40)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,True)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,4.5)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,None)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,{"name":"qH001"})

	def test_get_qhawax_latest_timestamp_valid_processed_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInValidProcessed)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInValidProcessed,40)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInValidProcessed,True)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInValidProcessed,4.5)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInValidProcessed,None)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInValidProcessed,{"name":"qH001"})

	def test_get_qhawax_in_field_public_mode_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,40)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,True)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,4.5)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,None)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,{"name":"qH001"},1)

	def test_get_qhawax_mode_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getQhawaxMode)
		self.assertRaises(TypeError,get_business_helper.getQhawaxMode,40)
		self.assertRaises(TypeError,get_business_helper.getQhawaxMode,True)
		self.assertRaises(TypeError,get_business_helper.getQhawaxMode,4.5)
		self.assertRaises(TypeError,get_business_helper.getQhawaxMode,None)
		self.assertRaises(TypeError,get_business_helper.getQhawaxMode,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.getQhawaxMode,{"name":"qH001"},1)

if __name__ == '__main__':
    unittest.main(verbosity=2)