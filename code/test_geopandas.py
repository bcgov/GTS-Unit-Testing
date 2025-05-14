'''
test_arcgis_api.py
description: methods for testing arcgis python api

Copyright 2023 Province of British Columbia

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at 

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

'''

import unittest


class TestGeopandas(unittest.TestCase):
    ''' Class to test geopandas'''

    @classmethod
    def setUpClass(self):
        print('setupClass')
    
    def setUp(self):
        # setup to keep your code DRY
        print ('setUp')
        self.data_dir = 'test-data'
    
    def test_import_basic_gdf(self):
        ''' Test geopandas import and required operations'''
        try:
            import geopandas
            import_success = True
        except ImportError:
            import_success  = False
        if import_success:
            gdf = geopandas.read_file('test_data/bcairzones.geojson')
            self.assertGreater(gdf.to_crs(3005).area[0],167098831500)
        self.assertTrue(import_success)
    
if __name__=='__main__':
    unittest.main()