import fetch from 'isomorphic-fetch'

var C = require('../constants')




export function selectPrj(idPrj, idOrg) {
    return {
        type: C.SELECT_PRJ,
        idPrj,
        idOrg
    }
}


function askProject() {
    return {
        type: C.ASK_PRJ_LIST
    }
}

function receiptProjectList(idOrg,prjList) {
    return {
        type: C.RECEIPT_PRJ_LIST,
        idOrg,
        projects: prjList,
        receivedAt: Date.now()
    }
}
function getProjects(idOrg) {
    return (dispatch,getState) => {
        dispatch(askProject(idOrg))
        return fetch(`http://127.0.0.1:5000/prj/v1.0/organizations/${idOrg}/projects`)
            .then(response => response.json())
            .then(json => {
                dispatch(receiptProjectList(idOrg, json.Projects));
                if(getState().uiState.idPrjCurrent==-1){
                    let idPrj = json.Projects[0].ID;
                    dispatch(selectPrj(idPrj, idOrg))
                }
            })
    }
}

function checkProjectList(state, idOrg) {
    const projects = state.projectList[idOrg]
    if (!projects) {
        return true
    } else if (projects.isFetching) {
        return false
    } else {
        return projects.didInvalidate
    }
}

export function giveProjectList(idOrg) {
    return (dispatch, getState) => {
        if (checkProjectList(getState(), idOrg)) {
            dispatch(getProjects(idOrg));
        }else{
            if(getState().uiState.idPrjCurrent==-1){
                let idPrj = getState().projectList[idOrg].selectedPrj;
                dispatch(selectPrj(idPrj, idOrg))
            }
        }
    }
}



