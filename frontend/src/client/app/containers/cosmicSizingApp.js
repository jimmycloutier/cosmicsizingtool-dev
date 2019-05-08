import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { giveOrganization } from '../actions/organizationAction';
import Organization from '../components/organization'
import Projects from '../components/projects'
import FunctionalProcessesDataMovements from './functionalProcessesDataMovementsFrame'

//import '../../../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../../../../style/styles-less.less';
//import './style/styles.less';

class cosmicSizingApp extends Component {

    constructor(props) {
        super(props);
    }

    componentDidMount() {
        const { dispatch } = this.props;
        dispatch(giveOrganization());
    }

    componentWillReceiveProps(nextProps){
    }

    render() {

        return (
        <div>
        <div>
            <div id="organizations">
                <Organization/>
            </div>
            <div id="projects">
                <Projects/>
            </div>
            <div id ="functionalProcessesDataMovements">
                <FunctionalProcessesDataMovements/>

            </div>

        </div>
        </div>
    )

    }
}

cosmicSizingApp.propTypes = {
    dispatch: PropTypes.func.isRequired
}


export default connect(null)(cosmicSizingApp)
