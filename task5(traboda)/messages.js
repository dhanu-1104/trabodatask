const TelegramBot = require('node-telegram-bot-api');
const token = '5756980284:AAEqT-HpknIwbZ3D43-UggHg3lBsWCxN6pA';
const bot = new TelegramBot(token, {polling: true});
const chatid='1190129745'
const message= 'hi abekaesh!';
let i=0;
function sendmessage(){
    bot.sendMessage(chatid,message);
    if(i<50){
      setTimeout(sendmessage,1000);
    }
}
sendmessage();