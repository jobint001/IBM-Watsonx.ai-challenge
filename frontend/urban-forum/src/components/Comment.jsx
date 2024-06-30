// Comment.jsx
import React, { useState } from 'react';

function Comment({ comment }) {
    const [replies, setReplies] = useState(comment.replies);
    const [replyText, setReplyText] = useState('');
    const [likes, setLikes] = useState(comment.likes || 0);
    const [dislikes, setDislikes] = useState(comment.dislikes || 0);

    const handleAddReply = () => {
        if (replyText.trim() === '') return; // Prevent empty replies
        const newReply = {
            id: replies.length + 1,
            user: "Current User",  // Ideally should be the logged-in user's name
            comment: replyText
        };
        setReplies([...replies, newReply]);
        setReplyText('');
    };

    const handleLike = () => {
        setLikes(likes + 1);
    };

    const handleDislike = () => {
        setDislikes(dislikes + 1);
    };

    return (
        <div className="bg-white p-4 rounded shadow mb-4">
            <h2 className="text-lg font-bold">{comment.user} - {comment.idea}</h2>
            <p>{comment.comment}</p>
            {replies && replies.length > 0 && (
                <div>
                    {replies.map((reply) => (
                        <p key={reply.id} className="ml-4 mt-2 text-gray-600"><strong>{reply.user}:</strong> {reply.comment}</p>
                    ))}
                </div>
            )}
            <div className="mt-2">
                <input
                    type="text"
                    value={replyText}
                    onChange={(e) => setReplyText(e.target.value)}
                    placeholder="Type your reply..."
                    className="border p-1 w-full rounded"
                />
                <button onClick={handleAddReply} className="mt-1 bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded">
                    Reply
                </button>
            </div>
            <div className="flex items-center justify-between mt-2">
                <button onClick={handleLike} className="flex items-center gap-1 text-green-600">
                    👍 {likes}
                </button>
                <button onClick={handleDislike} className="flex items-center gap-1 text-red-600">
                    👎 {dislikes}
                </button>
            </div>
        </div>
    );
}

export default Comment;
