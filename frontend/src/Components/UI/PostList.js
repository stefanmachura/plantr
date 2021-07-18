import React, { useEffect, useState } from 'react'

import Post from './Post';

const axios = require('axios');


export default function PostList() {
    const [posts, setPosts] = useState([])

    useEffect(() => axios('http://localhost:8000/posts').then(res => setPosts(res.data)), [])
    return (
        <ul>
            {posts.map(post => {
                return (<li key={post.id}>
                    <Post title={post.title} creator={post.creator} description={post.description} />
                </li>)
            })} 
        </ul>
    )
}
