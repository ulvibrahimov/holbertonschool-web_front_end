#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  const sortedArgs = args.sort((a, b) => b - a);
  const uniqueSorted = [...new Set(sortedArgs)];
  if (uniqueSorted.length <= 1) {
    console.log(0);
  } else {
    console.log(uniqueSorted[1]);
  }
}
