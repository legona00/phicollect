//Need to make program
const { response } = require('express')
const express = require('express')
const nodemailer = require('nodemailer')
const app = express()
const port = 5000
const myemail = 'tamufiastandards@gmail.com'
const mypassword = 'hnjxzcghxlhmgnmp'

function sendEmail(recipient){
    return new Promise((resolve, reject) => {
        var transporter = nodemailer.createTransport({
            service:'gmail',
            auth:{
                user:myemail,
                pass:mypassword
            }
        })

     const mail_configs ={
        from:myemail,
        to:recipient,
        subject:'TESTING EMAIL',
        text:"JUST CHECKING TEXT"
     }
     transporter.sendMail(mail_configs, function(error, info){
        if(error){
            console.log(error)
            return reject({message:'An error has occurred'})
        }
        return resolve({message:"Email sent succesfuly"})
     })

    })
}

app.get('/',(req,res) => {
    sendEmail()
    .then(response => res.send(response.message))
    .catch(error => res.status(500).send(error.message))
})

app.listen(port, () => {
    console.log('nodemailerProject is listening at http://localhost:5000')
})