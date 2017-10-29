import fetch from 'isomorphic-fetch'

var C = require('../constants')

function askShowFPDM(idPrj) {
    return {
        type: C.SHOW_FUNCTPROCESSESDATAMOVES_GRID,
        idPrjCurrentToDisplay: idPrj
    }
}

export function displayFPDMGrid(idPrj) {
        return (dispatch,getState) => {
            dispatch(askShowFPDM(idPrj))
        }
}



