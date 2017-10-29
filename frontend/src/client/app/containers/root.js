import React, { Component } from 'react'
import { Provider } from 'react-redux'
import configureStore from '../configureStore'
import CosmicApp from './cosmicSizingApp'

const store = configureStore()

export default class Root extends Component {
  render() {
    return (
      <Provider store={store}>
        <CosmicApp />
      </Provider>
    )
  }
}
