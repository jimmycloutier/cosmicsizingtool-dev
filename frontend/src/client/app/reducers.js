import { combineReducers } from 'redux'

import { projectList } from './reducers/projectList';
import { organizationList } from './reducers/organizationList';
import { uiState } from './reducers/uiState';
import { functionalProcessesDataMovesDisplay } from './reducers/functionalProcessesDataMovesDisplay'



const rootReducer = combineReducers({
    functionalProcessesDataMovesDisplay,
    projectList,
  organizationList,
  uiState
})

export default rootReducer
