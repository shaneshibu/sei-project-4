import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import 'bulma'

import Home from './components/common/Home'
import NavBar from './components/common/Navbar'
import Register from './components/auth/Register'
import Login from './components/auth/Login'
import './style.scss'

const App = () => (
  <BrowserRouter>
    <main>
      <NavBar />
      <Switch>
        <Route exact path="/register" component={Register} />
        <Route path="/login" component={Login}/>
        <Route exact path="/" component={Home} />
      </Switch>
    </main>
  </BrowserRouter>
)

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
