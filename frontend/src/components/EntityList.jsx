import React from "react";

function EntityList({ entities }) {
  return (
    <div className="p-4 bg-white shadow rounded">
      <h2 className="font-semibold mb-2">Entities</h2>
      <ul className="list-disc list-inside">
        {entities.map((e, idx) => (
          <li key={idx}>
            {e.word} <span className="text-gray-500">({e.entity})</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EntityList;
