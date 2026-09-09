export const SITE = {
  url: 'https://jiahaoblog.com',
  name: 'Jia-Hao Ji',
  chineseName: '纪家灏',
  author: 'Jia-Hao (Jay) Ji',
  email: 'jhji19@fudan.edu.cn',
  github: 'https://github.com/Biogod2020',
  description: 'Research and writing on biomedical AI, scientific agents, clinical medicine and society by Jia-Hao (Jay) Ji at Fudan University.',
  descriptionZh: '纪家灏的研究与写作：生物医学人工智能、科学智能体、临床医学与社会。',
};
export type Language = 'en' | 'zh-CN';
export type Alternate = { lang: string; href: string };
export const homeAlternates: Alternate[] = [
  { lang: 'en', href: '/' }, { lang: 'zh-CN', href: '/zh/' }, { lang: 'x-default', href: '/' },
];
export const profileAlternates: Alternate[] = [
  { lang: 'en', href: '/about/' }, { lang: 'zh-CN', href: '/about/zh/' },
];
export const research = [
  {
    title: 'Candidate supply and answer selection shape the value of LLM judging in multi-agent systems',
    url: 'https://arxiv.org/abs/2608.25937',
    venue: 'arXiv · 2026',
    label: 'Multi-agent reasoning', labelZh: '多智能体推理',
    description: 'Studying how candidate generation, judge reliability and final answer selection affect the answers a multi-agent system reports.',
    descriptionZh: '研究候选答案生成、评判器可靠性与最终选择规则，如何影响多智能体系统报告的答案。',
  },
  {
    title: 'SpatialDataAgent: Autonomous Spatial Omics Data Curation at Decade Scale',
    url: 'https://www.biorxiv.org/content/10.64898/2026.05.27.727615v1',
    venue: 'bioRxiv · 2026',
    label: 'Scientific data agents', labelZh: '科学数据智能体',
    description: 'An evidence-grounded workflow for recovering and standardizing fragmented spatial-omics records and their paired tissue images.',
    descriptionZh: '从分散的公开记录中恢复、整理空间组学数据及配对组织图像，并保留可核查的数据依据。',
  },
];
export function absoluteURL(path: string): string { return new URL(path, SITE.url).href; }
export function jsonLD(value: unknown): string {
  return JSON.stringify(value).replace(/</g, '\\u003c').replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029');
}
