import express from 'express';
import mongoose from 'mongoose';
import Invite from '../../models/invite.model';
import User from '../../models/user.model';
import bodyparser from 'body-parser';
import bcrypt from 'bcryptjs';
mongoose.connect(process.env.MONGO_URI!)

const router = express.Router();
router.use(bodyparser.json())
router.post('/register', async (req, res) => {
    const { username, password, invite } = req.body
    if (!username || !password || !invite) {
        res.status(400).send('Missing username, password or invite')
    }
    const inviteCode = await
        Invite
            .findOne({ invite: invite })
    if (!inviteCode) {
        res.status(400).send('Invalid invite code')
    }
    const user = await
        User.create({
            username: username,
            password: bcrypt.hashSync(password, 10),
            invitedwith: invite

}).catch((err) => {
        res.status(400).send(err)
    })
    


    
}
)

export default router;
