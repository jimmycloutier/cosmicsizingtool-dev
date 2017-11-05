import { combineReducers } from 'redux'
var C = require('../constants')

export function functionalProcessesDataMovesDisplay(state = {

}, action) {
    switch (action.type) {
        case C.SHOW_FUNCTPROCESSESDATAMOVES_GRID:
            return Object.assign({}, state, {

            })
        default:
            return state
    }
}