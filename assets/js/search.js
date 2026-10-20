(() => {
  "use strict";

  const search = document.querySelector(".hoshi-search");
  if (!search || !window.fetch) {
    return;
  }

  const form = search.querySelector("form");
  const input = search.querySelector("input");
  const status = search.querySelector('[role="status"]');
  const results = search.querySelector("ul");
  let documents;
  let requestNumber = 0;
  search.hidden = false;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const request = ++requestNumber;
    const terms = input.value.trim().toLocaleLowerCase().split(/\s+/u).filter(Boolean);
    results.replaceChildren();
    status.textContent = "";
    if (!terms.length) {
      return;
    }

    try {
      if (!documents) {
        const response = await fetch(search.dataset.searchUrl);
        if (!response.ok) {
          throw new Error("Search index unavailable");
        }
        documents = await response.json();
      }
      if (request !== requestNumber) {
        return;
      }

      const matches = documents.filter((document) => {
        const text = `${document.title} ${document.text}`.toLocaleLowerCase();
        return terms.every((term) => text.includes(term));
      });

      for (const match of matches) {
        const item = document.createElement("li");
        const link = document.createElement("a");
        link.href = match.url;
        link.textContent = `${match.section} · ${match.title}`;
        item.append(link);
        results.append(item);
      }

      status.textContent = matches.length
        ? `${status.dataset.count}: ${matches.length}`
        : status.dataset.empty;
    } catch {
      if (request === requestNumber) {
        status.textContent = status.dataset.error;
      }
    }
  });
})();
