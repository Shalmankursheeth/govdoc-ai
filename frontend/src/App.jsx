import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import SummaryCard from "./components/SummaryCard";
import DecisionCard from "./components/DecisionCard";
import EntityList from "./components/EntityList";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4 text-center">GovDoc-AI Dashboard</h1>
      <UploadForm setResult={setResult} />

      {result && (
        <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
          <SummaryCard summary={result.summary} />
          <DecisionCard decisions={result.decisions} />
          <EntityList entities={result.entities} />
        </div>
      )}
    </div>
  );
}

export default App;
