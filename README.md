## D3 Nester
This class recursively builds d3.js ready nested json for the hierarchical visuals in d3.js.
This class can nest for any number of keys input, memory permitting of course.

### Example Usage:
#### Place keys in order to nest for d3
* nestedData = Nester('JSON_key_A', 'JSON_key_B', 'JSON_key_C')  
#### Prep data 
* natNest = nestedData.useNativeNest(JSON_data)  
#### Get the d3 ready ready json
* data = nestedData.d3ReadyNest(natNest)  
