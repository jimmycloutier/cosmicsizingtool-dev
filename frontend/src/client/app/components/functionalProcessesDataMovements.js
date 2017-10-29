import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import HelloWorldComponentWithValue from './simple'

class FunctionalProcessesDataMovements extends Component {

    constructor(props) {
        super(props)

    }

    componentWillReceiveProps(nextProps){
        if (nextProps.idPrjCurrentToDisplay !== this.props.idPrjCurrentToDisplay && nextProps.idPrjCurrentToDisplay!=-1) {
            const { dispatch, idPrjCurrentToDisplay } = nextProps;
        }
    }

    render() {
        return (
            <div className =  "row">
                <h1>Functional Processes and Datamovements{this.props.idPrjCurrentToDisplay}</h1>
                <HelloWorldComponentWithValue />
            </div>

        );
    }
}

FunctionalProcessesDataMovements.propTypes = {
    idPrjCurrentToDisplay: PropTypes.number.isRequired,
}

//Mapping vars with the store
function mapStateToProps(state) {
    const {functionalProcessesDataMovesDisplay } = state;

    const {
        idPrjCurrentToDisplay
    } = functionalProcessesDataMovesDisplay || { idPrjCurrentToDisplay: 0};


    return {
        idPrjCurrentToDisplay
    }
}

export default connect(mapStateToProps)(FunctionalProcessesDataMovements)