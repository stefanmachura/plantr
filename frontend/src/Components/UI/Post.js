import React from 'react'

export default function Post(props) {
    return (
        <div>
            <span style={{fontSize:"2em"}}>{props.title} created by {props.creator.username}</span><br/>{props.description}
        </div>
    )
}
