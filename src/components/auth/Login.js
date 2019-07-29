import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

class Login extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, error: '' }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({ target: {name, value} }) {
    const data = {...this.state.data, [name]: value}
    this.setState({ data, error: '' })
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        this.props.history.push('/')
      })
      .catch((err) => {
        const message = err.response.data.message === 'Unauthorized' ?
          'Invalid Credentials' : err.response.data.message
        this.setState({ error: message })
      })
  }

  render() {
    //console.log(this.state.data)
    return(
      <section className="section">
        <div className="container">
          <form onSubmit={this.handleSubmit}>
            <h2 className="title">Login</h2>
            <div className="field">
              <label className="label">Username or Email</label>
              <div className="control">
                <input
                  type="text"
                  className={`input ${this.state.error ? 'is-danger' : ''}`}
                  name="username"
                  placeholder="Enter your username or email"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Password</label>
              <div className="control">
                <input
                  type="password"
                  className={`input ${this.state.error ? 'is-danger' : ''}`}
                  name="password"
                  placeholder="Password"
                  onChange={this.handleChange}
                />
              </div>
              {this.state.error && <small className="help is-danger">{this.state.error}</small>}
            </div>
            <button className="button is-info">Login</button>
          </form>
        </div>
      </section>
    )
  }

}

export default Login
