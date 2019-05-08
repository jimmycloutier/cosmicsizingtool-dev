import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux';
import {selectPrj } from '../actions/projectAction';
import {displayFPDMGrid} from '../actions/functionalProcessesDataMovementsAction'

class Projects extends Component {


    constructor(props) {
        super(props);
        //Association des fonctions à notre objet
        this.handlePrjChange = this.handlePrjChange.bind(this);
    }

    handlePrjChange(event) {
        const { dispatch,idOrgCurrent } = this.props;
        let idPrj=parseInt(event.currentTarget.getAttribute("data-idPrj"));
        dispatch(selectPrj(idPrj, idOrgCurrent));
    }

    componentWillReceiveProps(nextProps){
        if (nextProps.idPrjCurrent !== this.props.idPrjCurrent && nextProps.idPrjCurrent!=-1) {
            const { dispatch, idPrjCurrent } = nextProps;
            dispatch(displayFPDMGrid(nextProps.idOrgCurrent, nextProps.idPrjCurrent));

        }
    }

    render() {
        const { idPrjCurrent, projects } = this.props;
        return (

        <div>
            <div className =  "headerL">
                Project
            </div>
          {projects.map((project) => {
                  return (<div className = {idPrjCurrent === project.ID ? "selected" : ""} key={project.ID} data-idPrj={project.ID} onClick={this.handlePrjChange} >
                      {project.Name} ({project.CFP} CFP)
                  </div>)
                }
              )
          }
        </div>

        )
    }
}

Projects.propTypes = {
    projects:PropTypes.array.isRequired,
    idPrjCurrent: PropTypes.number.isRequired,
    idOrgCurrent: PropTypes.number.isRequired
}

function mapStateToProps(state) {
    const { uiState,projectList } = state;
    const {
        idOrgCurrent,
        idPrjCurrent,
    } = uiState || { idOrgCurrent:-1, idPrjCurrent:-1};

    const {
        isFetching:isFetchingPrj,
        projects,
    } = projectList[idOrgCurrent] || { isFetching: true,projects: [] };


    return {
        idOrgCurrent,
        isFetchingPrj,
        projects,
        idPrjCurrent
    }
}

export default connect(mapStateToProps)(Projects)
