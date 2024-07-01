import React, { useState } from 'react';
import axios from 'axios';

const SummaryPage = () => {
  const [feedback, setFeedback] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:5000/analyze_feedback', { feedback });
      setSummary(response.data);
      console.log(response.data)
    } catch (error) {
      console.error('Error fetching summary:', error);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-2xl w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Feedback Summary</h2>
          
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          
          <div>
            <button
              type="submit"
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              {loading ? 'Summarizing...' : 'Summarize'}
            </button>
          </div>
        </form>
        {summary && (
          <div className="bg-white w-full p-6 rounded-lg shadow-lg mt-8">
            <h3 className="text-lg leading-6 font-medium text-gray-900">Summary:</h3>
            <p className="mt-2 text-base text-gray-600">{summary}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default SummaryPage;
