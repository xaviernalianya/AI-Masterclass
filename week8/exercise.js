//Code Challenge 1 — Greet User
//Write a JavaScript function called greetUser that takes a name parameter and returns the string: Welcome, [name]! Ready to build?

//Call it twice and log the results. Your output must match exactly:

//Welcome, Amerix! Ready to build?
//Welcome, SMP Member! Ready to build?
//Write your JavaScript here
function greetUser(name) {
	return `Welcome, ${name}! Ready to build?`;
}

console.log(greetUser("Amerix"));
console.log(greetUser("SMP Member"));

//Code Challenge 2 — Simple ROI Report
//A man tracked 5 weeks of effort trying to get a woman's attention.
//  Loop through the records below, 
// calculate the totals,
//  compute the reply rate (rounded to the nearest whole number), and 
// print the report. 
// Your output must match exactly:

//Total spent: KES 52000
//Texts sent: 210
//Replies received: 14
//Reply rate: 7%
//Verdict: Cut your losses

//Use this data and this verdict rule: reply rate below 20% = "Cut your losses", below 50% = "She might like you", otherwise = "Keep going".

// const weeks = [
 // { amount_spent: 8000,  texts_sent: 40, texts_replied: 2 },
 // { amount_spent: 12000, texts_sent: 55, texts_replied: 3 },
//  { amount_spent: 9000,  texts_sent: 38, texts_replied: 4 },
//  { amount_spent: 11000, texts_sent: 42, texts_replied: 2 },
 // { amount_spent: 12000, texts_sent: 35, texts_replied: 3 },
//];
const weeks = [
  { amount_spent: 8000,  texts_sent: 40, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 55, texts_replied: 3 },
  { amount_spent: 9000,  texts_sent: 38, texts_replied: 4 },
  { amount_spent: 11000, texts_sent: 42, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 35, texts_replied: 3 },
];
const totalSpent = weeks.reduce((total, week) => total + week.amount_spent, 0);
const totalTextsSent = weeks.reduce((total, week) => total + week.texts_sent, 0);
const totalRepliesReceived = weeks.reduce((total, week) => total + week.texts_replied, 0);
const replyRate = Math.round((totalRepliesReceived / totalTextsSent) * 100);
const verdict = replyRate < 20 ? "Cut your losses" : replyRate < 50 ? "She might like you" : "Keep going";

console.log(`Total spent: KES ${totalSpent}`);
console.log(`Texts sent: ${totalTextsSent}`);
console.log(`Replies received: ${totalRepliesReceived}`);
console.log(`Reply rate: ${replyRate}%`);
console.log(`Verdict: ${verdict}`); 
