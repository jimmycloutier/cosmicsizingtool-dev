import { combineReducers } from 'redux'

import { projectList } from './reducers/projectList';
import { organizationList } from './reducers/organizationList';
import { uiState } from './reducers/uiState';



const rootReducer = combineReducers({
  projectList,
  organizationList,
  uiState
})

export default rootReducer
