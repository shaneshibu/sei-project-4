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
        <IndexPosts />
      </section>
    )
  }
}

export default Home
