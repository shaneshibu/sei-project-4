import React from 'react'
import axios from 'axios'
import moment from 'moment'


class UsersShow extends React.Component {
  constructor() {
    super()

    this.state = { tab: 'Images' }
    this.handleTabClick = this.handleTabClick.bind(this)
  }

  componentDidMount(){
    axios.get(`/api/users/${this.props.match.params.id}`)
      .then(res => {
        this.setState({ user: res.data })
      })
      .catch(err => console.log(err))
  }

  handleTabClick({ target }){
    this.setState({ tab: target.innerHTML })
  }

  render() {
    console.log(this.state)
    return (
      <section className="section">
        {this.state.user &&
          <div className="container">
            <div className="box">
              <article className="media">
                <div className="media-left">
                  <figure className="image is-256x256">
                    <img className="is-rounded" src={this.state.user.picture} />
                  </figure>

                </div>
                <div className="media-content has-text-centered">
                  <div className="content">
                    <h2 className="title">{this.state.user.username}</h2>
                    <p className="subtitle">Joined {moment(this.state.user.created_at).fromNow()}</p>
                  </div>
                </div>
              </article>
            </div>
            <div className="tabs is-centered">
              <ul>
                <li
                  onClick={this.handleTabClick}
                  className={this.state.tab === 'Images' ? 'is-active' : ''}
                >
                  <a>Images</a>
                </li>
                <li
                  onClick={this.handleTabClick}
                  className={this.state.tab === 'Posts' ? 'is-active' : ''}
                >
                  <a>Posts</a>
                </li>
                <li
                  onClick={this.handleTabClick}
                  className={this.state.tab === 'Comments' ? 'is-active' : ''}
                >
                  <a>Comments</a>
                </li>
              </ul>
            </div>
            <div className="user-images">
              {this.state.user.uploaded_images.length && this.state.user.uploaded_images.map(image => (
                <img key={image.id} src={image.url} alt="Image" className="image"/>
              ))}
            </div>
          </div>
        }
      </section>
    )
  }
}

export default UsersShow
