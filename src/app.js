import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import 'bulma'


import Home from './components/common/Home'
import NavBar from './components/common/Navbar'
import Register from './components/auth/Register'
import './style.scss'

const App = () => (
  <BrowserRouter>
    <main>
      <NavBar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/register" component={Register} />
      </Switch>
    </main>
  </BrowserRouter>
)

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
