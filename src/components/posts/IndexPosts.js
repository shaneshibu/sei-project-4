import React from 'react'
import axios from 'axios'

class IndexPosts extends React.Component {
  constructor() {
    super()

    this.state = {}

  }

  componentDidMount(){
    axios.get('/api/posts')
      .then(res => {
        const totalHeight = res.data.reduce((acc=0, post) => (
          acc + post.post_entries[0].image.height
        ), 0)
        this.el.style.height = `${totalHeight / 3.1}px`
        this.setState({ posts: res.data, totalHeight })
      })
      .catch(err => console.log(err))
  }

  componentDidUpdate(){

  }

  render() {
    this.state.posts && console.log(this.state)
    return (
      <div className="container">
        <h1 className="title">Index Posts</h1>
        <div className="posts-container" ref={el => this.el = el }>
          {this.state.posts && this.state.posts.map(post => (
            <div key={post.id} className="post-item has-text-centered">
              <p>{post.title}</p>
              {post.post_entries[0] && <img src={post.post_entries[0].image.url} alt={post.title}/>}
            </div>
          ))}
        </div>
      </div>
    )
  }
}

export default IndexPosts
