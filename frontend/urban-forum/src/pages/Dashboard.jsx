// Dashboard.jsx
import React from 'react';
import Comment from '../components/Comment';

const comments = [
    {
        id: 1,
        user: "Alice Johnson",
        idea: "Green Spaces in Urban Areas",
        comment: "Increasing green spaces can significantly improve urban air quality and provide residents with places to relax and exercise.",
        replies: [
            { id: 1, user: "John Doe", comment: "Absolutely agree! It also helps with reducing noise pollution." }
        ],
        likes: 10,
        dislikes: 2
    },
    {
        id: 2,
        user: "Bob Smith",
        idea: "Public Transportation Improvements",
        comment: "Enhancing public transport can reduce traffic congestion and pollution, making cities more efficient and livable.",
        replies: [],
        likes: 5,
        dislikes: 1
    }
];

function Dashboard() {
    return (
        <div className="min-h-screen bg-gray-100 flex flex-col items-center">
            <h1 className="text-2xl text-black font-bold text-center my-6">Urban Planning Ideas Dashboard</h1>
            <div className="w-full md:w-2/3">
                {comments.map(comment => <Comment key={comment.id} comment={comment} />)}
            </div>
        </div>
    );
}

export default Dashboard;
