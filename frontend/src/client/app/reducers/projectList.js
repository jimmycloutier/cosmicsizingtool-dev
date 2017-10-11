import { combineReducers } from 'redux'
var C = require('../constants')


function projects(state = {
    isFetching: false,
    didInvalidate: false,
    projects: [],
    selectedPrj : -1
}, action) {
    switch (action.type) {
        case C.INVALIDATE_PRJ:
            return Object.assign({}, state, {
                didInvalidate: true
            })
        case C.ASK_PRJ_LIST:
            return Object.assign({}, state, {
                isFetching: true,
                didInvalidate: false
            })
        case C.RECEIPT_PRJ_LIST:
            return Object.assign({}, state, {
                isFetching: false,
                didInvalidate: false,
                projects: action.projects,
                lastUpdated: action.receivedAt,
                selectedPrj: action.projects[1].ID
            })
        case C.SELECT_PRJ:
            return Object.assign({}, state, {
                selectedPrj: action.idPrj
            })
        default:
            return state
    }
}

export function projectList(state = { }, action) {
    switch (action.type) {
        case C.INVALIDATE_PRJ:
        case C.ASK_PRJ_LIST:
        case C.RECEIPT_PRJ_LIST:
        case C.SELECT_PRJ:
            return Object.assign({}, state, {
                [action.idOrg]: projects(state[action.idOrg], action)
            })
        default:
            return state
    }
}