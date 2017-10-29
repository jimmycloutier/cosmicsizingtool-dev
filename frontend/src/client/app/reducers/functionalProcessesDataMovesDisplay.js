import { combineReducers } from 'redux'
var C = require('../constants')

export function functionalProcessesDataMovesDisplay(state = {
    idPrjCurrentToDisplay: -1
}, action) {
    switch (action.type) {
        case C.SHOW_FUNCTPROCESSESDATAMOVES_GRID:
            return Object.assign({}, state, {
                idPrjCurrentToDisplay: action.idPrjCurrentToDisplay
            })
        default:
            return state
    }
}