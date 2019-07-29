import React from 'react'
import axios from 'axios'

class Register extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, errors: {} }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(e) {
    const data = {...this.state.data, [e.target.name]: e.target.value}
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/register', this.state.data)
      .then(() => this.props.history.push('/login'))
      .catch(err => this.setState({ errors: err.response.data }))
  }

  render() {
    console.log(this.state)
    return (
      <section className="section">
        <div className="container">
          <form onSubmit={this.handleSubmit}>
            <h2 className="title">Register</h2>
            <div className="field">
              <label className="label">Username</label>
              <div className="control">
                <input
                  type="text"
                  className={`input ${this.state.errors.username ? 'is-danger' : ''}`}
                  name="username"
                  placeholder="Username"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            {this.state.errors.username && <small className="help is-danger">{this.state.errors.username}</small>}
            <div className="field">
              <label className="label">Email</label>
              <div className="control">
                <input
                  type="text"
                  className={`input ${this.state.errors.email ? 'is-danger' : ''}`}
                  name="email"
                  placeholder="Email"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            {this.state.errors.email && <small className="help is-danger">{this.state.errors.email}</small>}
            <div className="field">
              <label className="label">Password</label>
              <div className="control">
                <input
                  type="password"
                  className={`input ${this.state.errors.password ? 'is-danger' : ''}`}
                  name="password"
                  placeholder="Password"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            {this.state.errors.password && <small className="help is-danger">{this.state.errors.password}</small>}
            <div className="field">
              <label className="label">Password Confirmation</label>
              <div className="control">
                <input
                  type="password"
                  className={`input ${this.state.errors.password_confirmation ? 'is-danger' : ''}`}
                  name="password_confirmation"
                  placeholder="Password Confirmation"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            {this.state.errors.password_confirmation &&
              <small className="help is-danger">{this.state.errors.password_confirmation}</small>}
            <button className="button is-info">Register</button>
          </form>
        </div>
      </section>
    )
  }
}

export default Register
