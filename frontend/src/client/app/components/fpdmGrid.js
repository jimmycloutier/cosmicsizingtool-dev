import React from 'react';
import ReactDOM from 'react-dom';
import { connect } from 'react-redux';

import JqxGrid from 'jqwidgets-framework/jqwidgets-react/react_jqxgrid';
import JqxButton from 'jqwidgets-framework/jqwidgets-react/react_jqxbuttons.js';

class FuncProcesesDataMovesGrid extends React.Component {
    constructor() {
        super();

        let source =
            {
                datatype: 'json',
                datafields: [
                    { name: 'Name' }
                ],
                id: 'ID',
                url: '',
                async: false,
                root: 'FunctionalProcesses',
                addrow: (rowid, rowdata, position, commit) => {
                    // synchronize with the server - send insert command
                    // call commit with parameter true if the synchronization with the server is successful
                    //and with parameter false if the synchronization failed.
                    // you can pass additional argument to the commit callback which represents the new ID if it is generated from a DB.
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

        let sourceDG =
            {
                datatype: 'json',
                datafields: [
                    { name: 'Name' },
                    {move: 'Move'}
                ],
                id: 'ID',
                url: '',
                async: false,
                root: 'DataMovements',
                addrow: (rowid, rowdata, position, commit) => {
                    // synchronize with the server - send insert command
                    // call commit with parameter true if the synchronization with the server is successful
                    //and with parameter false if the synchronization failed.
                    // you can pass additional argument to the commit callback which represents the new ID if it is generated from a DB.
                    console.log('Add row');
                    commit(true);
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

        this.state = {
            source: source,
            sourceDG: sourceDG
        };
    }

    refreshView(idOrg, idProj){
        let temp = this.state.source;
        let tempDG = this.state.sourceDG;
        temp.url = 'http://127.0.0.1:5000/fp/v1.0/organizations/' + idOrg+ '/projects/' + idProj + '/funcprocesses';
        this.setState({
            source: temp
        });
        // passing 'cells' to the 'updatebounddata' method will refresh only the cells values when the new rows count is equal to the previous rows count.
        this.refs.myGrid.updatebounddata('cells');
    }

    componentWillReceiveProps(nextProps){
        if (nextProps.idPrjCurrent !== this.props.idPrjCurrent && nextProps.idPrjCurrent!=-1) {
            this.refreshView(nextProps.idOrgCurrent, nextProps.idPrjCurrent)
        }
    }

    componentDidMount() {

        this.refs.refreshBtn.on('click', () => {
                this.refreshView(this.props.idOrgCurrent, this.props.idPrjCurrent)
        });
        this.refs.clearBtn.on('click', () => {
            this.refs.myGrid.clear();
        });
    }

      render() {

          let dataAdapter = new $.jqx.dataAdapter(this.state.source, { autoBind: true });
          let dataAdapterDG = new $.jqx.dataAdapter(this.state.sourceDG, { autoBind: true });
          let datamoves = dataAdapterDG.records;

          let rendertoolbar = (toolbar) => {
              let container = document.createElement('div');
              container.style.margin = '5px';

              let buttonContainer1 = document.createElement('div');

              container.appendChild(buttonContainer1);

              toolbar[0].appendChild(container);

              let addRowButton = ReactDOM.render(<JqxButton value='Refresh' style={{ float: 'left' }}/>, buttonContainer1);


              addRowButton.on('click', () => {
                  this.refs.myGrid.refresh();
                  this.refs.myGrid.refreshdata();
                  this.refs.myGrid.clear();

                  this.refs.myGrid.updatebounddata();

              });

          };

          let nestedGrids = new Array();
          let rowdetailstemplate = { rowdetails: '<div id="grid" style="margin: 10px;"></div>', rowdetailsheight: 220, rowdetailshidden: true };
          let initrowdetails = (index, parentElement, gridElement, record) => {
              let id = record.uid.toString();
              let grid = $($(parentElement).children()[0]);
              nestedGrids[index] = grid;

              /*
              let filtergroup = new $.jqx.filter();
              let filter_or_operator = 1;
              let filtervalue = id;
              let filtercondition = 'equal';
              let filter = filtergroup.createfilter('stringfilter', filtervalue, filtercondition);
              let ordersbyid = [];
              for (let m = 0; m < orders.length; m++) {
                  let result = filter.evaluate(orders[m]['EmployeeID']);
                  if (result)
                      ordersbyid.push(orders[m]);
              }
              let orderssource = {
                  datafields: [
                      { name: 'EmployeeID', type: 'string' },
                      { name: 'ShipName', type: 'string' },
                      { name: 'ShipAddress', type: 'string' },
                      { name: 'ShipCity', type: 'string' },
                      { name: 'ShipCountry', type: 'string' },
                      { name: 'ShippedDate', type: 'date' }
                  ],
                  id: 'OrderID',
                  localdata: ordersbyid
              }*/

              let nestedGridAdapter = dataAdapterDG;
              if (grid != null) {
                  grid.jqxGrid({
                      source: nestedGridAdapter, width: 780, height: 200,
                      columns: [
                          { text: 'DG Name', datafield: 'Name', width: 200 },
                          { text: 'DG Move', datafield: 'Move', width: 200 }
                      ]
                  });
              }
          }


          let columns =
              [
                  { text: 'Fnc Name', dataField: 'Name', width: 200 }
              ];

          return (
              <div>
              <JqxGrid ref='myGrid'
                width={850} source={dataAdapter} columns={columns}
                editable={true} rendertoolbar={rendertoolbar} showtoolbar={true} rowdetails={true} initrowdetails={initrowdetails} rowdetailstemplate={rowdetailstemplate} rowsheight={35}
                />
                <div style={{ marginTop: 10 }}>
                    <JqxButton ref='refreshBtn' value='Refresh Data' style={{ float: 'left' }}/>
                    <JqxButton ref='clearBtn' value='Clear' style={{ float: 'left' }}/>
                </div>
              </div>

          )
      }
}



//import React, { Component, PropTypes } from 'react';
//import { connect } from 'react-redux';

//class FuncProcessesDataMovesGrid extends React.Component {
  //  render() {
  //      return <h1>Dans le simple</h1>;
  //  }
//}



export default connect(null)(FuncProcesesDataMovesGrid)