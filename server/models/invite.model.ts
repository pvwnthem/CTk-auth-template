import mongoose from 'mongoose';

const inviteSchema = new mongoose.Schema({
    invite: {
        type: String,
        required: true,
        unique: true
    },
})

const Invite = mongoose.model('Invite', inviteSchema) || mongoose.model('Invite')
export default Invite

