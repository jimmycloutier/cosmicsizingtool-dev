import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import FuncProcessesDataMovesGrid from '../components/fpdmGrid'

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

                <div className =  "row">
                    <h1>Functional Processes and Datamovements</h1>
                    <h2>Org: {this.props.idOrgCurrent} / Proj: {this.props.idPrjCurrent}</h2>
                </div>
                <div>
                    <FuncProcessesDataMovesGrid idOrgCurrent={ this.props.idOrgCurrent} idPrjCurrent={this.props.idPrjCurrent} />
                </div>

            </div>

        );
    }
}

FunctionalProcessesDataMovementsFrame.propTypes = {
    idPrjCurrent: PropTypes.number.isRequired,
    idOrgCurrent: PropTypes.number.isRequired
}

//Mapping vars with the store
function mapStateToProps(state) {
    const { uiState } = state;
    const {
        idOrgCurrent,
        idPrjCurrent,
    } = uiState || { idOrgCurrent:-1, idPrjCurrent:-1};

    /* const {functionalProcessesDataMovesDisplay } = state;

     const {
         idPrjCurrent,
         idOrgCurrent
     } = functionalProcessesDataMovesDisplay || { idPrjCurrent: -1, idOrgCurrent: -1};

    */
    return {
        idPrjCurrent,
        idOrgCurrent
    }
}

export default connect(mapStateToProps)(FunctionalProcessesDataMovementsFrame)