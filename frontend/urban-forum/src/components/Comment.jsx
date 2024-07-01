import React, { useState } from 'react';
import { ArrowUpIcon, ArrowDownIcon, PaperAirplaneIcon } from '@heroicons/react/24/outline';

function Comment({ comment }) {
    const [replies, setReplies] = useState(comment.replies);
    const [replyText, setReplyText] = useState('');
    const [likes, setLikes] = useState(comment.likes || 0);
    const [dislikes, setDislikes] = useState(comment.dislikes || 0);

    const handleAddReply = () => {
        if (!replyText.trim()) return;
        const newReply = {
            id: replies.length + 1,
            user: "Current User",  // Ideally replace with actual user session data
            comment: replyText
        };
        setReplies([...replies, newReply]);
        setReplyText('');
    };

    const handleLike = () => setLikes(likes + 1);
    const handleDislike = () => setDislikes(dislikes + 1);

    return (
        <div className="bg-white p-4 rounded shadow mb-4">
            <h2 className="text-lg text-black font-bold">{comment.user} - {comment.idea}</h2>
            <p className='text-black'>{comment.comment}</p>
            {replies.map((reply) => (
                <p key={reply.id} className="ml-4 mt-2 text-gray-600"><strong>{reply.user}:</strong> {reply.comment}</p>
            ))}
            <div className="mt-2 flex items-center space-x-2">
                <input
                    type="text"
                    value={replyText}
                    onChange={(e) => setReplyText(e.target.value)}
                    placeholder="Type your reply..."
                    className="border p-1 w-full rounded text-black bg-white"
                />
                <PaperAirplaneIcon 
                    className="h-5 w-5 text-blue-500 hover:text-blue-700 cursor-pointer"
                    onClick={handleAddReply}
                    aria-label="Send reply"
                />
            </div>
            <div className="flex items-center justify-between mt-2">
                <span className="flex items-center gap-1">
                    <ArrowUpIcon 
                        className="h-5 w-5 text-green-600 hover:text-green-800 cursor-pointer" 
                        onClick={handleLike}
                        aria-label="Like"
                    />
                    <span className="text-green-600">({likes})</span>
                </span>
                <span className="flex items-center gap-1">
                    <ArrowDownIcon 
                        className="h-5 w-5 text-red-600 hover:text-red-800 cursor-pointer" 
                        onClick={handleDislike}
                        aria-label="Dislike"
                    />
                    <span className="text-red-600">({dislikes})</span>
                </span>
            </div>
        </div>
    );
}

export default Comment;
