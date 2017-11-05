
var C = require('../constants')

function askShowFPDM(idOrg, idPrj) {
    return {
        type: C.SHOW_FUNCTPROCESSESDATAMOVES_GRID
    }
}

export function displayFPDMGrid(idOrg, idPrj) {
        return (dispatch,getState) => {
            dispatch(askShowFPDM(idOrg, idPrj))
        }
}



