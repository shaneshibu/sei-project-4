import React from 'react'
import { Link, withRouter } from 'react-router-dom'

class NavBar extends React.Component {
  constructor() {
    super()

    this.state = {}
    this.toggleNavbar = this.toggleNavbar.bind(this)
  }


  toggleNavbar() {
    this.setState({ navbarOpen: !this.state.navbarOpen})
  }

  componentDidUpdate(prevProps) {
    if (this.props.location.pathname !== prevProps.location.pathname) {
      this.setState({ navbarOpen: false })
    }
  }

  render() {
    return (
      <nav className="navbar is-dark">
        <div className="container">
          <div className="navbar-brand">
            <Link to="/" className="navbar-item">ImageBored</Link>

            <a role="button" className={`navbar-burger ${this.state.navbarOpen ? 'is-active' : ''}`} aria-label="menu" aria-expanded="false" onClick={this.toggleNavbar}>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>
          <div className={`navbar-menu ${this.state.navbarOpen ? 'is-active' : ''}`}>
            <div className="navbar-end">
              <Link to="/register" className="navbar-item">Register</Link>
            </div>
          </div>
        </div>
      </nav>
    )
  }
}

export default withRouter(NavBar)
