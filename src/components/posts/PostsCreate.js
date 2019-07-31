import React from 'react'

class PostsCreate extends React.Component {
  constructor() {
    super()

    this.state = {}
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange({ target }){
    this.setState({ [target.name]: target.value })
  }

  render() {
    console.log(this.state)
    return (
      <section className="section">
        <div className="container">
          <h1 className="title">Create New Post</h1>
          <form>
            <input
              type="text"
              className="input"
              name="title"
              placeholder='Your Post Title Here'
              value={this.state.title || ''}
              onChange={this.handleChange}
            />
          </form>
        </div>
      </section>
    )
  }
}

export default PostsCreate
