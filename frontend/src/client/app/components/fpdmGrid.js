import React from 'react';
import ReactDOM from 'react-dom';
import { connect } from 'react-redux';

import JqxGrid from 'jqwidgets-framework/jqwidgets-react/react_jqxgrid';
import JqxButton from 'jqwidgets-framework/jqwidgets-react/react_jqxbuttons.js';
import JqxComboBox from 'jqwidgets-framework/jqwidgets-react/react_jqxcombobox.js';
import JqxWindow from 'jqwidgets-framework/jqwidgets-react/react_jqxwindow.js';

class FuncProcesesDataMovesGrid extends React.Component {
    constructor() {
        super();

        //Source for Functional Process
        let source =
            {
                datatype: 'json',
                id: 'ID',
                url: '',
                async: false,
                root: 'FunctionalProcesses',
                addrow: (rowid, rowdata, position, commit) => {
                    // synchronize with the server - send insert command
                    // call commit with parameter true if the synchronization with the server is successful
                    //and with parameter false if the synchronization failed.
                    // you can pass additional argument to the commit callback which represents the new ID if it is generated from a DB.
                    fetch("http://127.0.0.1:5000/v1.0/organizations/" + this.props.idOrgCurrent + "/projects/" + this.props.idPrjCurrent + "/funcprocesses", {

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
                        .then((res)=>{ return res.json(); })
                        .then( (data) => {
                            //do something awesome that makes the world a better place
                            //alert( JSON.stringify( data ));
                            //alert(data.ID)
                            commit(true, data.ID);
                        });


                },
                deleterow: (rowid, commit) => {
                    console.log('Delete Row : ' + rowid);
                    fetch("http://127.0.0.1:5000/v1.0/organizations/" + this.props.idOrgCurrent + "/projects/" + this.props.idPrjCurrent + "/funcprocesses/" + rowid, {

                        method: "DELETE"
                    })
                        .then( (response) => {
                            //do something awesome that makes the world a better place
                            commit(true);
                        });
                },
                updaterow: (rowid, newdata, commit) => {
                    // synchronize with the server - send update command
                    // call commit with parameter true if the synchronization with the server is successful
                    // and with parameter false if the synchronization failed.
                    console.log('Update Row : ' + rowid);
                    fetch("http://127.0.0.1:5000/v1.0/organizations/" + this.props.idOrgCurrent + "/projects/" + this.props.idPrjCurrent + "/funcprocesses/" + rowid, {

                        method: "PUT",
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },

                        //make sure to serialize your JSON body
                        body: JSON.stringify({
                            Name: newdata.Name
                        })
                    })
                        .then(function(res){ return res.json(); })
                        .then( (data) => {
                            //do something awesome that makes the world a better place
                            //alert( JSON.stringify( data ));
                            //alert(data.ID)
                            commit(true, data.ID);
                        });
                }
            };

        //Source for DataGroup
        let sourceDG =
            {
                datatype: 'json',
                id: 'ID',
                url: '',
                async: false,
                root: 'DataMovements',
                addrow: (rowid, rowdata, position, commit) => {
                    // synchronize with the server - send insert command
                    // call commit with parameter true if the synchronization with the server is successful
                    //and with parameter false if the synchronization failed.
                    // you can pass additional argument to the commit callback which represents the new ID if it is generated from a DB.
                    console.log('Add row : ' + rowid + ' Pos:' + position);
                    fetch("http://127.0.0.1:5000/v1.0/organizations/" + this.props.idOrgCurrent + "/projects/" + this.props.idPrjCurrent + "/funcprocesses/" + this.state.idFuncProcess + "/datamoves", {
                        method: "POST",
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },

                        //make sure to serialize your JSON body
                        body: JSON.stringify({
                            Name: rowdata.Name || "",
                            Move: rowdata.Move || ""
                        })

                    })
                        .then((res)=>{ return res.json(); })
                        .then( (data) => {
                            //do something awesome that makes the world a better place
                            //alert( JSON.stringify( data ));
                            //alert(data.ID)
                            commit(true, data.ID);
                        });
                },
                deleterow: (rowid, commit) => {
                    // synchronize with the server - send delete command
                    // call commit with parameter true if the synchronization with the server is successful
                    //and with parameter false if the synchronization failed.
                    console.log('Delete Row : ' + rowid);
                    fetch("http://127.0.0.1:5000/v1.0/organizations/" + this.props.idOrgCurrent + "/projects/" + this.props.idPrjCurrent + "/funcprocesses/" + this.state.idFuncProcess + "/datamoves/" + rowid, {
                        method: "DELETE"
                    })
                        .then( (response) => {
                            //do something awesome that makes the world a better place
                            commit(true);
                        });
                },
                updaterow: (rowid, newdata, commit) => {
                    // synchronize with the server - send update command
                    // call commit with parameter true if the synchronization with the server is successful
                    // and with parameter false if the synchronization failed.
                    console.log('Update Row :' + rowid);
                    //console.log('Name :' + newdata.Name);
                    //console.log('Move :' + newdata.Move);

                    fetch("http://127.0.0.1:5000/v1.0/organizations/" + this.props.idOrgCurrent + "/projects/" + this.props.idPrjCurrent + "/funcprocesses/" + this.state.idFuncProcess + "/datamoves/" + rowid, {

                        method: "PUT",
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },

                        //make sure to serialize your JSON body
                        body: JSON.stringify({
                            Name: newdata.Name || "",
                            Move: newdata.Move || ""
                        })
                    })
                        .then( (response) => {
                            //do something awesome that makes the world a better place
                            commit(true);
                        });
                }
            };
        let sourcePtn =
            {
                datatype: 'json',
                url: 'http://127.0.0.1:5000/v1.0/patterns',
                id: 'ID',
                root: 'Patterns',
                async: false
            };

        let idFuncProcess = -1;

        this.state = {
            source: source,
            sourceDG: sourceDG,
            sourcePtn: sourcePtn,
            idFuncProcess: idFuncProcess
        };

    }

    refreshView(idOrg, idProj){
        let temp = this.state.source;
        temp.url = 'http://127.0.0.1:5000/v1.0/organizations/' + idOrg+ '/projects/' + idProj + '/funcprocesses';
        this.setState({
            source: temp
        });
        // passing 'cells' to the 'updatebounddata' method will refresh only the cells values when the new rows count is equal to the previous rows count.
        this.refs.myGrid.updatebounddata('cells');
    }

    contentHTMLdg(){
        let tempHTML = '<h1> Set datagroup name</h1> ' +
            '<br> First name: <input type="text" name="fname" id="txt_name" value="BalooneXYZ"><br><br>' +
            '<input type="button" id="ok2" value="OK" className="ok2" />' +
            '<input type="button" id="cancel2" value="Cancel" className="cancel2" />';
        //return tempHTML;

        return              '<div>' +
                'Please click "OK", "Cancel" or the close button to close the modal window. The dialog' +
                'result will be displayed in the events log12.' +
                '<input type="button" onclick="$("#jqxWindow").jqxWindow("close");" id="ok2" ref="okButton2" width={80} value="OK" style={{ display: "inline-block", marginRight: 10 }} className="ok2" />' +
                '<input type="button"  ref="cancelButton2" width={80} value="Cancel" style={{ display: "inline-block" }} className="cancel" />' +
                '</div>';
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
        this.refs.addBtn.on('click', () => {
            let datarow = {
                Name: ""
            };
            this.refs.myGrid.addrow(null, datarow);
        });
        this.refs.multiAddBtn.on('click', () => {
            this.refs.myGrid.beginupdate();
            for (let i = 0; i < 10; i++) {
                let datarow = {
                    Name: ""
                };
                this.refs.myGrid.addrow(null, datarow);
            }
            this.refs.myGrid.endupdate();
        });
        this.refs.delBtn.on('click', () => {
            let selectedcell = this.refs.myGrid.getselectedcell();
            let selectedrowindex = selectedcell.rowindex;
            let rowscount = this.refs.myGrid.getdatainformation().rowscount;
            if (selectedrowindex >= 0 && selectedrowindex < rowscount) {
                let id = this.refs.myGrid.getrowid(selectedrowindex);
                this.refs.myGrid.deleterow(id);
            };
        });
        this.refs.jqxWindow.on('close', (event) => {

            if (event.type === 'close') {

                if (event.args.dialogResult.OK) {

                    let cb = this.refs.myComboBox;
                    let item = cb.getSelectedItem();
                    if (item != null) {
                        fetch("http://127.0.0.1:5000/v1.0/organizations/" + this.props.idOrgCurrent + "/projects/" + this.props.idPrjCurrent + "/applypattern/" + item.value,
                        {
                            method: 'PATCH',
                            headers: {
                                'Accept': 'application/json',
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({
                                '<First DG>': $('#dg1').val(),
                                '<Second DG>': $('#dg2').val(),
                                '<Third DG>': $('#dg3').val(),
                            })
                        }).then((res) => {
                                return res.json();
                            })
                            .then((data) => {

                                this.refreshView(this.props.idOrgCurrent, this.props.idPrjCurrent)

                            });
                    }
                }
            }

        });
        this.refs.applyPtnBtn.on('click', () =>{
            let cb = this.refs.myComboBox;
            let item = cb.getSelectedItem();
            if (item != null) {
                /*
                fetch("http://127.0.0.1:5000/v1.0/organizations/" + this.props.idOrgCurrent + "/projects/" + this.props.idPrjCurrent + "/applypattern/" + item.value)
                    .then((res) => {
                        return res.json();
                    })
                    .then((data) => {
                        //do something awesome that makes the world a better place
                        console.log('Open windows');
                        //this.refs.jqxWindow.setContent(this.contentHTMLdg());
                        this.refs.jqxWindow.open();
                        alert($('#dg1').val());

                    });
                  */
                fetch("http://127.0.0.1:5000/v1.0/patterns/" + item.value + "/datamoves")
                    .then((res) => {
                        return res.json();
                    })
                    .then((data) => {
                        //Display datamovement
                        for(i = 0; i < 20; i++){
                            if (data.DataMovements.length > i){
                                $('#dg' + (i+1)).show();
                                $('label[for=dg' + (i+1)+ '], input#dg' + (i+1)).show();
                                $('#dg' + (i+1)).val(data.DataMovements[i].Name);
                                $('#dg' + (i+1)).attr("placeholder", data.DataMovements[i].Name);
                            }
                            else {
                                $('#dg' + (i+1)).hide();
                                $('label[for=dg' + (i+1)+ '], input#dg' + (i+1)).hide();
                            }
                        }


                        this.refs.jqxWindow.open();


                    });
            }
        });
    }

      render() {

          let dataAdapter = new $.jqx.dataAdapter(this.state.source, { autoBind: true });
          let dataAdapterDG = new $.jqx.dataAdapter(this.state.sourceDG, { autoBind: true });
          let dataAdapterPtn = new $.jqx.dataAdapter(this.state.sourcePtn, { autoBind: true });

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
          let rowdetailstemplate = {
              //rowdetails:'<div id="grid" style="margin: 10px;"></div><button class="nested-button">Add row</button><button class="nested-button">Add 10 rows</button><button class="nested-button">Delete row</button>',
              rowdetails:'<div id="grid" style="margin: 10px;"></div>',
              rowdetailsheight: 220,
              rowdetailshidden: true
          };
          let initrowdetails = (index, parentElement, gridElement, record) => {
              let id = record.uid.toString();
              let grid = $($(parentElement).children()[0]);

              //nestedGrids[index] = grid;

              let sourceTemp = this.state.sourceDG;
              sourceTemp.url =this.state.source.url + '/' + id + '/datamoves';
              console.log(sourceTemp.url);

              let nestedGridAdapter = new $.jqx.dataAdapter(sourceTemp);

              if (grid != null) {
                  /*var buttonAddRowElement = grid[0].parentElement.children[1];
                  var buttonAdd = $(buttonAddRowElement).jqxButton({});
                  buttonAdd.click(() => {
                      console.log('Add row in Nested Grid', grid[0].id);
                  });
                  var buttonAddTenRowsElement = grid[0].parentElement.children[2];
                  var buttonAddTen = $(buttonAddTenRowsElement).jqxButton({});
                  buttonAddTen.click(() => {
                      console.log('Add 10 rows in Nested Grid', grid[0].id);
                  });
                  var buttonDelRowElement = grid[0].parentElement.children[3];
                  var buttonDel = $(buttonDelRowElement).jqxButton({});
                  buttonDel.click(() => {
                      console.log('Del row in Nested Grid', grid[0].id);
                  });*/
                  grid.jqxGrid({
                      source: nestedGridAdapter, width: 780, height: 200, editable: true,editmode: 'selectedcell',
                      selectionmode: 'singlecell',
                      showstatusbar: true,
                      renderstatusbar: (statusbar) => {
                          // appends buttons to the status bar.
                          let container = $("<div style='overflow: hidden; position: relative; margin: 5px;'></div>");
                          let addButton = $("<div style='float: left; margin-left: 5px;'>Add row</div>");
                          let addTenButton = $("<div style='float: left; margin-left: 5px;'>Add 10 rows</div>");
                          let delButton = $("<div style='float: left; margin-left: 5px;'>Delete row</div>");
                          container.append(addButton);
                          container.append(addTenButton);
                          container.append(delButton);
                          statusbar.append(container);
                          addButton.jqxButton({  });
                          addTenButton.jqxButton({  });
                          delButton.jqxButton({ });
                          // add new row.
                          addButton.click( (event) => {
                              this.state.idFuncProcess = id;
                              grid.jqxGrid('addrow', null, {}, 'last');
                          });
                          addTenButton.click( (event) => {
                              this.state.idFuncProcess = id;
                              for (let i = 0; i < 10; i++) {
                                  grid.jqxGrid('addrow', null, {}, 'last');
                              }
                          });
                          delButton.click( (event) => {
                              let selectedcell = grid.jqxGrid('getselectedcell');
                              let selectedrowindex = selectedcell.rowindex;
                              let rowscount = grid.jqxGrid('getdatainformation').rowscount;
                              if (selectedrowindex >= 0 && selectedrowindex < rowscount) {
                                  let idDM = grid.jqxGrid('getrowid', selectedrowindex);
                                  let commit = grid.jqxGrid('deleterow', idDM);
                              }
                          });
                      },
                      columns: [
                          { text: 'DG Name', datafield: 'Name', width: 200 },
                          { text: 'DG Move', datafield: 'Move', width: 200 },
                          {text: 'Size', editable: false, datafield: 'size',
                            cellsrenderer: (index, datafield, value, defaultvalue, column, rowdata) => {
                                let total = 0;
                                if (rowdata.Move != null)
                                    total = rowdata.Move.length;
                                return '<div style="margin: 4px;" class="jqx-right-align">' + dataAdapter.formatNumber(total, 'n') + '</div>';
                            }
                          }
                      ]
                  });
              }
          }


          let columns =
              [
                  { text: 'Fnc Name', dataField: 'Name', width: 200 },
                  {text: 'Size', editable: false, datafield: 'size',
                      cellsrenderer: (index, datafield, value, defaultvalue, column, rowdata) => {
                          let total = 0;
                          return '<div style="margin: 4px;" class="jqx-right-align">' + dataAdapter.formatNumber(total, 'n') + '</div>';
                      }
                  }
              ];

          return (
              <div>
                  <div style={{marginBottom:'3em'}}>
                      Select Pattern
                      <JqxComboBox ref='myComboBox' style={{ float: 'left', marginTop: 20 }} autoComplete={true}
                                   width={200} height={25} source={dataAdapterPtn} selectedIndex={0} displayMember={'Name'} valueMember={'ID'}
                      />
                      <JqxButton ref='applyPtnBtn' value='Apply Pattern' style={{ float: 'left', marginTop: 20 }} />
                  </div>

                  <div style={{ marginTop: 10 }}>
                      <JqxButton ref='addBtn' value='Add Row' style={{ float: 'left' }}/>
                      <JqxButton ref='multiAddBtn' value='Add 10 Rows' style={{ float: 'left' }}/>
                      <JqxButton ref='delBtn' value='Delete Row' style={{ float: 'left' }}/>
                  </div>
                  <JqxGrid ref='myGrid'
                    width={'100%'} source={dataAdapter} columns={columns}
                    editable={true} showtoolbar={false} rowdetails={true} initrowdetails={initrowdetails}
                    rowdetailstemplate={rowdetailstemplate} rowsheight={35} editmode={'selectedcell'} selectionmode={'singlecell'} enablekeyboarddelete={true}
                  />
                  <JqxWindow ref='jqxWindow'
                             width={500} height={425}
                             showCollapseButton={false}
                             autoOpen={false}
                             resizable={false}
                             cancelButton={'.cancel'} okButton={'.ok'}
                  >
                      <div>
                          <img width="14" height="14" src="../../images/help.png" alt="" />
                          Enter DataGroup
                      </div>
                      <div>
                          <div>
                              <label htmlFor="dg1">DG1:</label> <input id="dg1" type="text" name="dg1" /> <br/>
                              <label htmlFor="dg2">DG2:</label> <input id="dg2" type="text" name="dg2" /> <br/>
                              <label htmlFor="dg3">DG3:</label> <input id="dg3" type="text" name="dg3" /> <br/>
                              <label htmlFor="dg4">DG4:</label> <input id="dg4" type="text" name="dg4" /> <br/>
                              <label htmlFor="dg5">DG5:</label> <input id="dg5" type="text" name="dg5" /> <br/>
                              <label htmlFor="dg6">DG6:</label> <input id="dg6" type="text" name="dg6" /> <br/>
                              <label htmlFor="dg7">DG7:</label> <input id="dg7" type="text" name="dg7" /> <br/>
                              <label htmlFor="dg8">DG8:</label> <input id="dg8" type="text" name="dg8" /> <br/>
                              <label htmlFor="dg9">DG9:</label> <input id="dg9" type="text" name="dg9" /> <br/>
                              <label htmlFor="dg10">DG10:</label> <input id="dg10" type="text" name="dg10" /> <br/>
                              <label htmlFor="dg11">DG11:</label> <input id="dg11" type="text" name="dg11" /> <br/>
                              <label htmlFor="dg12">DG12:</label> <input id="dg12" type="text" name="dg12" /> <br/>
                              <label htmlFor="dg13">DG13:</label> <input id="dg13" type="text" name="dg13" /> <br/>
                              <label htmlFor="dg14">DG14:</label> <input id="dg14" type="text" name="dg14" /> <br/>
                              <label htmlFor="dg15">DG15:</label> <input id="dg15" type="text" name="dg15" /> <br/>
                              <label htmlFor="dg16">DG16:</label> <input id="dg16" type="text" name="dg16" /> <br/>
                              <label htmlFor="dg17">DG17:</label> <input id="dg17" type="text" name="dg17" /> <br/>
                              <label htmlFor="dg18">DG18:</label> <input id="dg18" type="text" name="dg18" /> <br/>
                              <label htmlFor="dg19">DG19:</label> <input id="dg19" type="text" name="dg19" /> <br/>
                              <label htmlFor="dg20">DG20:</label> <input id="dg20" type="text" name="dg20" /> <br/>
                          </div>
                          <div style={{ float: 'right', marginTop: '15px' }}>
                              <JqxButton ref='okButton' width={80} value='OK' style={{ display: 'inline-block', marginRight: 10 }} className='ok' />
                              <JqxButton ref='cancelButton' width={80} value='Cancel' style={{ display: 'inline-block' }} className='cancel' />
                          </div>
                      </div>
                  </JqxWindow>
                  <div style={{ marginTop: 10 }}>
                      <JqxButton ref='refreshBtn' value='Refresh Data' style={{ float: 'left' }}/>
                      <JqxButton ref='clearBtn' value='Clear' style={{ float: 'left' }}/>
                  </div>
              </div>

          )
      }
}

export default connect(null)(FuncProcesesDataMovesGrid)