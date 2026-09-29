// Simulates: fetch("https://api.mwangifarm.co.ke/milk-records")
const fakeFetch = () => Promise.resolve({
  ok: true,
  json: () => Promise.resolve([
    { cow: "Daisy",   week: 1, litres: 98.5,  feed_kg: 50 },
    { cow: "Bella",   week: 1, litres: 112.0, feed_kg: 55 },
    { cow: "Kamau1",  week: 1, litres: 87.0,  feed_kg: 45 },
    { cow: "Daisy",   week: 2, litres: 105.0, feed_kg: 52 },
    { cow: "Bella",   week: 2, litres: 118.5, feed_kg: 57 },
  ])
});

const loadMilkRecords = async () => {
  try {
    const response = await fakeFetch();
    if (!response.ok) throw new Error("Server error");

    const records = await response.json();
    const totalLitres = records.reduce((sum, r) => sum + r.litres, 0);
    const avgPerCow   = totalLitres / records.length;

    console.log(`Records fetched: ${records.length}`);
    console.log(`Total litres: ${totalLitres.toFixed(1)}`);
    console.log(`Average per record: ${avgPerCow.toFixed(1)} L`);
    console.log("\nWeek 2 records:");
    records
      .filter(r => r.week === 2)
      .forEach(r => console.log(`  ${r.cow}: ${r.litres} L | feed ${r.feed_kg} kg`));
  } catch (err) {
    console.log("Fetch failed:", err.message);
  }
};

await loadMilkRecords();
