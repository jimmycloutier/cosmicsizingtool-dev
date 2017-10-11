import { combineReducers } from 'redux'
var C = require('../constants')

export function organizationList(state = {
    isFetching: false,
    didInvalidate: false,
    organizations: []
}, action) {
    switch (action.type) {
        case C.INVALIDATE_ORG:
            return Object.assign({}, state, {
                didInvalidate: true
            })
        case C.ASK_ORG:
            return Object.assign({}, state, {
                isFetching: true,
                didInvalidate: false
            })
        case C.RECEIPT_ORG:
            return Object.assign({}, state, {
                isFetching: false,
                didInvalidate: false,
                organizations: action.organizations,
                lastUpdated: action.receivedAt
            })
        default:
            return state
    }
}