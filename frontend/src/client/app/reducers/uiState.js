import { combineReducers } from 'redux'
var C = require('../constants')

export function uiState(state = {
    idOrgCurrent: -1,
    idPrjCurrent: -1,
    idSectionCurrent:-1
}, action) {
    switch (action.type) {
        case C.SELECT_ORG:
            return Object.assign({}, state, {
                idOrgCurrent: action.idOrg,
                idPrjCurrent: -1,
                idSectionCurrent: -1
            })
        case C.SELECT_PRJ:
            return Object.assign({}, state, {
                idPrjCurrent: action.idPrj,
                idSectionCurrent: -1
            })
        case C.SELECT_SECTION:
            return Object.assign({}, state, {
                idSectionCurrent: action.section
            })
        default:
            return state
    }
}