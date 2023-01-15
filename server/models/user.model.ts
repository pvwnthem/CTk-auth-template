import mongoose from 'mongoose';

const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    invitedwith: {
        type: String,
        required: true
    },
    premium: {
        type: Boolean,
        required: false,
        default: false

    }

    
    
})

const User = mongoose.model('User', userSchema) || mongoose.model('User')
export default User