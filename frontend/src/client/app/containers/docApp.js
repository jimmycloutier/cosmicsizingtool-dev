import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { giveOrganization } from '../actions/organizationAction';
import Organization from '../components/organization'
import Projects from '../components/projects'
//import '../../../../node_modules/bootstrap/dist/css/bootstrap.min.css';
//import '../../../../style/styles.less';
//import './style/styles.less';

class docApp extends Component {

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
        <div className="container-fluid" >
        <div className="row">
            <div className="col-xs-2" id="organizations">
                <Organization/>
            </div>
            <div className="col-xs-2" id="projects">
                <Projects/>
            </div>
            <div className="col-xs-3" >

            </div>
            <div className="col-xs-5">
            </div>

        </div>
        </div>
    )

    }
}

docApp.propTypes = {
    dispatch: PropTypes.func.isRequired
}

//Mapping des variables et du store
/*
function mapStateToProps(state) {
    const { uiState, projectList,organizationList } = state;
    const {
        idOrgCurrent: PropTypes.number.isRequired,
        idPrjCurrent: PropTypes.number.isRequired

    } = uiState || {idOrgCurrent:-1, idPrjCurrent:-1};

    return {
        idOrgCurrent,
        idPrjCurrent
    }
}*/

export default connect(null)(docApp)
