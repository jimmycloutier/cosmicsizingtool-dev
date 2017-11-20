
import fetch from 'isomorphic-fetch'

var C = require('../constants')



function askOrganization() {
    return {
        type: C.ASK_ORG
    }
}

function receiptOrganization(json) {
    return {
        type: C.RECEIPT_ORG,
        organizations: json,
        receivedAt: Date.now()
    }
}

function getOrganizations() {
    return (dispatch,getState) => {
        dispatch(askOrganization())
        return fetch(`http://127.0.0.1:5000/v1.0/organizations`)
            .then(response => response.json())
            .then(json => {
                dispatch(receiptOrganization(json.Organizations));
                /*if(getState().uiState.idCatEnCours==-1){
                    dispatch(selectOrg(json[0].id));
                }*/
            })
    }
}

function checkOrganization(state) {
    const listOrganization = state.organizationList
    if (listOrganization.organizations.length === 0) {
        return true
    } else if (listOrganization.isFetching) {
        return false
    } else {
        return listOrganization.didInvalidate
    }
}

export function giveOrganization() {
    return (dispatch, getState) => {
        if (checkOrganization(getState())) {
            return dispatch(getOrganizations())
        }
    }
}

export function selectOrg(idOrg) {
    return {
        type: C.SELECT_ORG,
        idOrg
    }
}