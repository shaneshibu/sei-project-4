import React from 'react'
import axios from 'axios'

class IndexPosts extends React.Component {
  constructor() {
    super()

    this.state = {}

  }

  componentDidMount(){
    axios.get('/api/posts')
      .then(res => this.setState({ posts: res.data }))
      .catch(err => console.log(err))
  }

  render() {
    this.state.posts && console.log(this.state.posts[0].post_entries[0].image.url)
    return (
      <div className="container">
        <h1 className="title">Index Posts</h1>
        <div className="columns is-multiline">
          {this.state.posts && this.state.posts.map(post => (
            <div key={post.id} className="column is-one-fifth">
              <p>{post.title}</p>
              <figure className="image">
                {post.post_entries[0] && <img src={post.post_entries[0].image.url} alt={post.title}/>}
              </figure>
            </div>
          ))}
        </div>
      </div>
    )
  }
}

export default IndexPosts
