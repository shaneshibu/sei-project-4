import React from 'react'

import IndexPosts from '../posts/IndexPosts'

class Home extends React.Component {
  constructor() {
    super()

    this.state = {}

  }

  render() {
    return (
      <section className="section">
        <div className="container">
          <h1 className="title">Home Page</h1>
          <IndexPosts />
        </div>
      </section>
    )
  }
}

export default Home
