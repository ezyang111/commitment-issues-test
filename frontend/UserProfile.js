// UserProfile.js

import React, { useState, useEffect } from 'react';

const UserProfile = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch('/api/user')
            .then(response => response.json())
            .then(data => {
                setUser(data);
                setLoading(false);
            })
            .catch(err => {
                console.error('Error fetching user data:', err);
                setError('Failed to load user data.');
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <div>Loading user profile...</div>;
    }

    if (error) {
        return <div className="error">{error}</div>;
    }

    if (!user) {
        return <div>No user data available.</div>;
    }

    return (
        <div className="user-profile">
            <img src={user.avatar} alt="User Avatar" className="avatar" />
            <h2>{user.name}</h2>
            <p>Email: {user.email}</p>
            <p>Address: {user.address}</p>
            <p>Phone: {user.phone}</p>
            {/* More user information */}
        </div>
    );
};

export default UserProfile;
