// ScrollScrubVideo logic tests — run with: node ScrollScrubVideo.test.js

const sceneBounds = [
    { start: 0, end: 8 },
    { start: 10, end: 17 },
    { start: 19, end: 50 },
    { start: 55, end: 72 },
    { start: 75, end: 85 },
    { start: 88, end: 94 },
]

function getSceneInfo(videoTime, bounds) {
    for (let i = 0; i < bounds.length; i++) {
        if (videoTime >= bounds[i].start && videoTime < bounds[i].end) {
            const duration = bounds[i].end - bounds[i].start
            return {
                inScene: true,
                sceneIndex: i,
                sceneProgress: duration > 0 ? (videoTime - bounds[i].start) / duration : 0,
            }
        }
    }
    for (let i = 0; i < bounds.length - 1; i++) {
        if (videoTime >= bounds[i].end && videoTime < bounds[i + 1].start) {
            return { inScene: false, sceneIndex: i, sceneProgress: 1 }
        }
    }
    if (videoTime < bounds[0].start) {
        return { inScene: true, sceneIndex: 0, sceneProgress: 0 }
    }
    return { inScene: true, sceneIndex: bounds.length - 1, sceneProgress: 1 }
}

function getHighlightedScene(videoTime) {
    const info = getSceneInfo(videoTime, sceneBounds)
    return info.inScene ? info.sceneIndex : Math.min(info.sceneIndex + 1, 5)
}

function goToChapterTarget(i) {
    return i === 0 ? 0 : sceneBounds[i - 1].end
}

let passed = 0
let failed = 0
function test(name, fn) {
    try {
        fn()
        passed++
        console.log(`  ✓ ${name}`)
    } catch (e) {
        failed++
        console.log(`  ✗ ${name}: ${e.message}`)
    }
}
function eq(actual, expected, msg) {
    if (actual !== expected) throw new Error(`${msg || ''} expected ${expected}, got ${actual}`)
}

console.log("\n── getSceneInfo ──")
test("time 0 → scene 0", () => { eq(getSceneInfo(0, sceneBounds).sceneIndex, 0); eq(getSceneInfo(0, sceneBounds).inScene, true) })
test("time 5 → scene 0", () => eq(getSceneInfo(5, sceneBounds).sceneIndex, 0))
test("time 7.9 → scene 0", () => eq(getSceneInfo(7.9, sceneBounds).sceneIndex, 0))
test("time 8 → transition (sceneIndex 0)", () => { eq(getSceneInfo(8, sceneBounds).inScene, false); eq(getSceneInfo(8, sceneBounds).sceneIndex, 0) })
test("time 9 → transition (sceneIndex 0)", () => eq(getSceneInfo(9, sceneBounds).inScene, false))
test("time 10 → scene 1", () => { eq(getSceneInfo(10, sceneBounds).inScene, true); eq(getSceneInfo(10, sceneBounds).sceneIndex, 1) })
test("time 17 → transition (sceneIndex 1)", () => { eq(getSceneInfo(17, sceneBounds).inScene, false); eq(getSceneInfo(17, sceneBounds).sceneIndex, 1) })
test("time 19 → scene 2", () => eq(getSceneInfo(19, sceneBounds).sceneIndex, 2))
test("time 50 → transition (sceneIndex 2)", () => { eq(getSceneInfo(50, sceneBounds).inScene, false); eq(getSceneInfo(50, sceneBounds).sceneIndex, 2) })
test("time 93.9 → scene 5", () => eq(getSceneInfo(93.9, sceneBounds).sceneIndex, 5))

console.log("\n── goToChapter targets ──")
test("chapter 0 → time 0", () => eq(goToChapterTarget(0), 0))
test("chapter 1 → time 8 (s1End)", () => eq(goToChapterTarget(1), 8))
test("chapter 2 → time 17 (s2End)", () => eq(goToChapterTarget(2), 17))
test("chapter 3 → time 50 (s3End)", () => eq(goToChapterTarget(3), 50))
test("chapter 4 → time 72 (s4End)", () => eq(goToChapterTarget(4), 72))
test("chapter 5 → time 85 (s5End)", () => eq(goToChapterTarget(5), 85))

console.log("\n── highlighted scene (transition fix) ──")
test("time 0 → highlight 0", () => eq(getHighlightedScene(0), 0))
test("time 5 → highlight 0", () => eq(getHighlightedScene(5), 0))
test("time 8 (transition) → highlight 1 (next scene)", () => eq(getHighlightedScene(8), 1))
test("time 17 (transition) → highlight 2", () => eq(getHighlightedScene(17), 2))
test("time 50 (transition) → highlight 3", () => eq(getHighlightedScene(50), 3))
test("time 72 (transition) → highlight 4", () => eq(getHighlightedScene(72), 4))
test("time 85 (transition) → highlight 5", () => eq(getHighlightedScene(85), 5))
test("time 10 (in scene 1) → highlight 1", () => eq(getHighlightedScene(10), 1))

console.log("\n── click → highlight chain ──")
test("click chapter 2 → seek 8 → highlight 1", () => {
    const seekTime = goToChapterTarget(1)
    eq(seekTime, 8, "seek target")
    eq(getHighlightedScene(seekTime), 1, "highlighted scene")
})
test("click chapter 3 → seek 17 → highlight 2", () => {
    const seekTime = goToChapterTarget(2)
    eq(seekTime, 17, "seek target")
    eq(getHighlightedScene(seekTime), 2, "highlighted scene")
})
test("click chapter 4 → seek 50 → highlight 3", () => {
    const seekTime = goToChapterTarget(3)
    eq(seekTime, 50, "seek target")
    eq(getHighlightedScene(seekTime), 3, "highlighted scene")
})

console.log(`\n${passed} passed, ${failed} failed\n`)
process.exit(failed > 0 ? 1 : 0)
