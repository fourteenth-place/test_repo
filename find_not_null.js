var wktField = 'wkt';
var wkbField = 'wkb';

function determineGeometryField(wktField, wkbField) {
    // Validate - check if both null
    if ((wktField || wkbField) == null) {
        console.log('No geometry field specified. Must be specified as one of wktField or wkbField.')
        geometryField = null
    }
    // Validate - check if both set
    else if (wktField && wkbField) {
        console.log('Both wktField and wkbField specified. Can only specify one.')
        geometryField = null
    }
    // Determine which field is set
    else {
        geometryField = wktField || wkbField
    }
    return geometryField, 
}

// console.log(wktField)
// console.log(wktField || wkbField)
console.log(determineGeometryField(wktField, wkbField))