import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';

class HelloWorldComponentWithValue extends React.Component {
    render() {
        return <h1>Hello</h1>;
    }
}

export default connect(null)(HelloWorldComponentWithValue)