<h2><a href="https://codeforces.com/contest/1209/problem/G1" target="_blank" rel="noopener noreferrer">1209G1 — Into Blocks (easy version)</a></h2>

| | |
|---|---|
| **Difficulty** | 2000 |
| **Language** | PyPy 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1209G1](https://codeforces.com/contest/1209/problem/G1) |

## Topics
`data structures` `dsu` `greedy` `implementation` `two pointers`

---

## Problem Statement

<div class="header"><div class="title">G1. Into Blocks (easy version)</div><div class="time-limit"><div class="property-title">time limit per test</div>5 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p><span class="tex-font-style-it">This is an easier version of the next problem. In this version, $$$q = 0$$$</span>.</p><p>A sequence of integers is called <span class="tex-font-style-it">nice</span> if its elements are arranged in blocks like in $$$[3, 3, 3, 4, 1, 1]$$$. Formally, if two elements are equal, everything in between must also be equal.</p><p>Let's define <span class="tex-font-style-it">difficulty</span> of a sequence as a minimum possible number of elements to change to get a nice sequence. However, if you change at least one element of value $$$x$$$ to value $$$y$$$, you must also change all other elements of value $$$x$$$ into $$$y$$$ as well. For example, for $$$[3, 3, 1, 3, 2, 1, 2]$$$ it isn't allowed to change first $$$1$$$ to $$$3$$$ and second $$$1$$$ to $$$2$$$. You need to leave $$$1$$$'s untouched or change them to the same value.</p><p>You are given a sequence of integers $$$a_1, a_2, \ldots, a_n$$$ and $$$q$$$ updates.</p><p>Each update is of form "$$$i$$$ $$$x$$$" — change $$$a_i$$$ to $$$x$$$. Updates are not independent (the change stays for the future).</p><p>Print the difficulty of the initial sequence and of the sequence after every update.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains integers $$$n$$$ and $$$q$$$ ($$$1 \le n \le 200\,000$$$, $$$q = 0$$$), the length of the sequence and the number of the updates.</p><p>The second line contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le 200\,000$$$), the initial sequence.</p><p>Each of the following $$$q$$$ lines contains integers $$$i_t$$$ and $$$x_t$$$ ($$$1 \le i_t \le n$$$, $$$1 \le x_t \le 200\,000$$$), the position and the new value for this position.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print $$$q+1$$$ integers, the answer for the initial sequence and the answer after every update.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0021564022832965335" id="id006280001372992131" class="input-output-copier">Copy</div></div><pre id="id0021564022832965335">5 0
3 7 3 7 3
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007924921024277116" id="id000930370735738082" class="input-output-copier">Copy</div></div><pre id="id007924921024277116">2
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id005237234419841588" id="id008439008501029333" class="input-output-copier">Copy</div></div><pre id="id005237234419841588">10 0
1 2 1 2 3 1 1 1 50 1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id009772158693135484" id="id007431919445107377" class="input-output-copier">Copy</div></div><pre id="id009772158693135484">4
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id009069239514477262" id="id00022337683660674235" class="input-output-copier">Copy</div></div><pre id="id009069239514477262">6 0
6 6 3 3 4 4
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id006280060094171581" id="id005261511354133185" class="input-output-copier">Copy</div></div><pre id="id006280060094171581">0
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0010148988065717313" id="id009983534054438198" class="input-output-copier">Copy</div></div><pre id="id0010148988065717313">7 0
3 3 1 3 2 1 2
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id00072858710139319" id="id004372993378445993" class="input-output-copier">Copy</div></div><pre id="id00072858710139319">4
</pre></div></div></div>