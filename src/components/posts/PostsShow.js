import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import moment from 'moment'

class PostsShow extends React.Component {
  constructor() {
    super()

    this.state = {}

  }

  componentDidMount(){
    axios.get(`/api/posts/${this.props.match.params.id}`)
      .then(res => {
        this.setState({ post: res.data })
      })
      .catch(err => console.log(err))
  }

  render() {
    let post = null
    if (this.state.post) post = this.state.post
    return (
      <section className="section">
        <div className="container">
          {post &&
            <h1 className="title">{post.title}</h1>
          }
          <div className="columns is-multiline">
            {post && post.post_entries.map(entry => (
              <div key={entry.position} className="column is-8 is-offset-2">
                <figure className="image">
                  <img src={entry.image.url} alt={entry.caption}/>
                  <p>{entry.caption}</p>
                </figure>
              </div>
            ))}
          </div>
          {post &&
            <div className="box">
              <p>
                <Link to={`/users/${post.creator.id}`}>
                  <strong>Posted By: {post.creator.username}</strong>
                </Link>
                <br/>
                <small>{moment(post.created_at).fromNow()}</small>
              </p>
            </div>
          }
        </div>

      </section>
    )
  }
}

export default PostsShow
