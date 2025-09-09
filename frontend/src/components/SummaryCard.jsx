import React from "react";

function SummaryCard({ summary }) {
  return (
    <div className="p-4 bg-white shadow rounded">
      <h2 className="font-semibold mb-2">Summary</h2>
      <p>{summary}</p>
    </div>
  );
}

export default SummaryCard;
