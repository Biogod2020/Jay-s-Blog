// Markdown images are below the article title. Raw HTML and interactive demos are left intact.
export default function lazyMarkdownImages() {
  return function transform(tree) {
    function visit(node) {
      if (node.type === 'image') {
        node.data ??= {};
        node.data.hProperties = { loading: 'lazy', decoding: 'async', ...node.data.hProperties };
      }
      for (const child of node.children ?? []) visit(child);
    }
    visit(tree);
  };
}
