import React from "react";

function DecisionCard({ decisions }) {
  return (
    <div className="p-4 bg-white shadow rounded">
      <h2 className="font-semibold mb-2">Decisions</h2>
      <ul className="list-disc list-inside">
        {decisions.map((d, idx) => (
          <li key={idx}>{d}</li>
        ))}
      </ul>
    </div>
  );
}

export default DecisionCard;
