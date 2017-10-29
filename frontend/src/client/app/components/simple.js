import React from 'react';
import ReactDOM from 'react-dom';
import { connect } from 'react-redux';

import JqxBarGauge from 'jqwidgets-framework/jqwidgets-react/react_jqxbargauge';
import JqxGrid from 'jqwidgets-framework/jqwidgets-react/react_jqxgrid';
import JqxButton from 'jqwidgets-framework/jqwidgets-react/react_jqxbuttons.js';

class HelloWorldComponentWithValue extends React.Component {
      render() {

          let source =
              {
                  datatype: 'json',
                  datafields: [
                      { name: 'Name' },
                      { name: 'Org' },
                      { name: 'org_ID', type: 'int' }
                  ],
                  id: 'ID',
                  url: 'http://127.0.0.1:5000/prj/v1.0/organizations/1/projects',
                  root: 'Projects',
                  addrow: (rowid, rowdata, position, commit) => {
                      // synchronize with the server - send insert command
                      // call commit with parameter true if the synchronization with the server is successful
                      //and with parameter false if the synchronization failed.
                      // you can pass additional argument to the commit callback which represents the new ID if it is generated from a DB.
                      console.log('Add Row');
                      console.log(rowdata);
                      console.log(rowdata.Name);
                      fetch("http://127.0.0.1:5000/prj/v1.0/organizations/1/projects", {
                          method: "POST",
                          headers: {
                              'Accept': 'application/json',
                              'Content-Type': 'application/json'
                          },

                          //make sure to serialize your JSON body
                          body: JSON.stringify({
                              Name: rowdata.Name
                          })
                      })
                          .then( (response) => {
                              //do something awesome that makes the world a better place
                              console.log('Saved!');
                              commit(true);
                          });


                  },
                  deleterow: (rowid, commit) => {
                      // synchronize with the server - send delete command
                      // call commit with parameter true if the synchronization with the server is successful
                      //and with parameter false if the synchronization failed.
                      console.log('Delete Row');
                      commit(true);
                  },
                  updaterow: (rowid, newdata, commit) => {
                      // synchronize with the server - send update command
                      // call commit with parameter true if the synchronization with the server is successful
                      // and with parameter false if the synchronization failed.
                      console.log('Update Row');
                      commit(true);
                  }
              };

          let dataAdapter = new $.jqx.dataAdapter(source);

          let columns =
              [
                  { text: 'Pj Name', dataField: 'Name', width: 200 },
                  { text: 'Or Name', dataField: 'Org', width: 200 }
              ];
          return (

              <JqxGrid
                width={850} source={dataAdapter} columns={columns}
                showeverpresentrow={true}
                everpresentrowactions={'add reset'} everpresentrowactionsmode={'columns'}
                editable={true} filterable={true}
                />

          )
      }
}



//import React, { Component, PropTypes } from 'react';
//import { connect } from 'react-redux';

//class HelloWorldComponentWithValue extends React.Component {
  //  render() {
  //      return <h1>Dans le simple</h1>;
  //  }
//}

export default connect(null)(HelloWorldComponentWithValue)