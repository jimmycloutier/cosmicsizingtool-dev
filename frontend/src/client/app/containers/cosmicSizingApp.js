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

                <div className="col-xs-2" id="organizations">
                    <Organization/>
                </div>
                <div className="col-xs-2" id="projects">
                    <Projects/>
                </div>
                <div className="col-xs-8"  id ="functionalProcessesDataMovements">
                    <FunctionalProcessesDataMovements/>
                </div>

        </div>
    )

    }
}

cosmicSizingApp.propTypes = {
    dispatch: PropTypes.func.isRequired
}


export default connect(null)(cosmicSizingApp)
