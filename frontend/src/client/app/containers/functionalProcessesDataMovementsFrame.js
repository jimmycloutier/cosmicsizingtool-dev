import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import FuncProcessesDataMovesGrid from '../components/fpdmGrid';

class FunctionalProcessesDataMovementsFrame extends Component {

    constructor(props) {
        super(props)

    }

    componentWillReceiveProps(nextProps){
        if (nextProps.idPrjCurrent !== this.props.idPrjCurrent && nextProps.idPrjCurrent!=-1) {
            const { dispatch, idPrjCurrent } = nextProps;
        }
    }

    render() {
        return (
            <div>

                <div className = "headerL">
                    Functional Process and Data movement
                    {/*
                    <h2>Org: {this.props.idOrgCurrent} / Proj: {this.props.idPrjCurrent} / CFP : {JSON.stringify(this.props.projects, ['CFP']) || 0}  / Info : {this.props.projects.values() || 0}  </h2>
                    */}
                </div>
                {/*
                <div>
                    {this.props.projects.map((project) => {
                            return (<div className = {"selected"} key={project.ID} data-idPrj={project.ID}>
                                {project.Name} ({project.CFP} CFP)
                            </div>)
                        }
                    )
                    }
                </div>*/}
                <div>
                    <FuncProcessesDataMovesGrid idOrgCurrent={ this.props.idOrgCurrent} idPrjCurrent={this.props.idPrjCurrent} />
                </div>

            </div>

        );
    }
}

FunctionalProcessesDataMovementsFrame.propTypes = {
    idPrjCurrent: PropTypes.number.isRequired,
    idOrgCurrent: PropTypes.number.isRequired,
    projects:PropTypes.array.isRequired,
    selectedPrj: PropTypes.number.isRequired
}

//Mapping vars with the store
function mapStateToProps(state) {
    const { uiState,projectList } = state;
    const {
        idOrgCurrent,
        idPrjCurrent,
    } = uiState || { idOrgCurrent:-1, idPrjCurrent:-1};

    const {
        isFetching:isFetchingPrj,
        projects,
        selectedPrj
    } = projectList[idOrgCurrent] || { isFetching: true,projects: [],  selectedPrj: -1};

    /* const {functionalProcessesDataMovesDisplay } = state;

     const {
         idPrjCurrent,
         idOrgCurrent
     } = functionalProcessesDataMovesDisplay || { idPrjCurrent: -1, idOrgCurrent: -1};

    */

    return {
        idOrgCurrent,
        isFetchingPrj,
        projects,
        idPrjCurrent,
        selectedPrj
    }
}

export default connect(mapStateToProps)(FunctionalProcessesDataMovementsFrame)