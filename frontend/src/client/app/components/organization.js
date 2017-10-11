import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import {selectOrg} from '../actions/organizationAction';
import { giveProjectList } from '../actions/projectAction';

class Organization extends Component {

    constructor(props) {
        super(props);
        this.handleOrgChange = this.handleOrgChange.bind(this);
    }

    componentWillReceiveProps(nextProps){
        if (nextProps.idOrgCurrent !== this.props.idOrgCurrent) {
            const { dispatch, idOrgCurrent } = nextProps;
            dispatch(giveProjectList(idOrgCurrent));
        }
    }

    handleOrgChange(event) {
        const { dispatch } = this.props;
        let idOrg=parseInt(event.currentTarget.getAttribute("data-idOrg"));
        dispatch(selectOrg(idOrg));
    }

    render() {
        const { idOrgCurrent, organizations } = this.props

        return (
            <div>
                <div className =  "row">
                    Add Organization
                </div>
          {organizations.map(organization =>
              <div className = {idOrgCurrent===organization.ID ? "selected row organization" : "row organization"} data-idOrg={organization.ID} key={organization.ID} onClick={this.handleOrgChange}>
                  {organization.Name}
              </div>)
          }
        </div>

        )
    }
}

Organization.propTypes = {
    organizations:PropTypes.array.isRequired,
    idOrgCurrent: PropTypes.number.isRequired,
    isFetchingOrg: PropTypes.bool.isRequired
}

//Mapping vars with the store
function mapStateToProps(state) {
    const { uiState, organizationList } = state;
    const {
        idOrgCurrent,
    } = uiState || { idOrgCurrent:-1};
    const {
        isFetching:isFetchingOrg,
        organizations
    } = organizationList || { isFetching: true,organizations: []};


    return {
        idOrgCurrent,
        organizations,
        isFetchingOrg
    }
}

export default connect(mapStateToProps)(Organization)