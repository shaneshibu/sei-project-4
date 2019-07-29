import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import 'bulma'


import Home from './components/common/Home'
import './style.scss'

const App = () => (
  <BrowserRouter>
    <main>
      <Switch>
        <Route exact path="/" component={Home} />
      </Switch>
    </main>
  </BrowserRouter>
)

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
