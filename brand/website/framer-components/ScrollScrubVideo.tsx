import { addPropertyControls, ControlType } from "framer"
import { useRef, useEffect, useMemo, useCallback } from "react"

// ─── Copy per scene ──────────────────────────────────────────────────────────

const SCENE_COPY = [
    {
        headlineNl: "Neem elk gesprek op",
        headlineEn: "Record any appointment",
        descriptionNl:
            "Neem je telefoon mee naar de dokter. Luister thuis het hele gesprek terug.",
        descriptionEn:
            "Take your phone to the doctor. Listen back to the full conversation at home.",
    },
    {
        headlineNl: "Direct een heldere samenvatting",
        headlineEn: "A clear summary, instantly",
        descriptionNl:
            "Wat er besproken is, wat er nu gebeurt en wat je zelf kan doen. In begrijpelijke taal.",
        descriptionEn:
            "What was discussed, what happens next, and what you can do yourself. In plain language.",
    },
    {
        headlineNl: "Voorbereid op wat komt",
        headlineEn: "Prepared for what's next",
        descriptionNl:
            "Slimme vragen voor je volgende afspraak, gebaseerd op wat er besproken is.",
        descriptionEn:
            "Smart questions for your next visit, based on what was discussed.",
    },
    {
        headlineNl: "Moeilijke taal, makkelijk uitgelegd",
        headlineEn: "Complex language, explained",
        descriptionNl:
            "Begrijpelijke uitleg van medische brieven. Alle termen uitgelegd zodat je het snapt.",
        descriptionEn:
            "Medical letters, made clear with all terms explained so that you understand.",
    },
    {
        headlineNl: "Betrek je dierbaren",
        headlineEn: "Keep loved ones close",
        descriptionNl:
            "Voeg je naasten toe aan je zorgkring. Zij blijven op de hoogte, jij houdt de regie.",
        descriptionEn:
            "Add your people to your care circle. They stay informed, you stay in control.",
    },
    {
        headlineNl: "Zorg doe je samen",
        headlineEn: "Navigate care, together",
        descriptionNl:
            "Gebruik Ditto voor je eigen gezondheid of volg mensen van wie je houdt, met Ditto is iedereen op de hoogte.",
        descriptionEn:
            "Whether you're managing your own health or following someone you love, Ditto keeps everyone on the same page.",
    },
]

// ─── Helpers ─────────────────────────────────────────────────────────────────

function clamp(v: number, min = 0, max = 1) {
    return Math.max(min, Math.min(max, v))
}

interface SceneBounds {
    start: number
    end: number
}

function getSceneInfo(
    videoTime: number,
    bounds: SceneBounds[]
): { inScene: boolean; sceneIndex: number; sceneProgress: number } {
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

// ─── Component ───────────────────────────────────────────────────────────────

interface Props {
    videoFile: string
    videoUrl: string
    language: "nl" | "en"
    sectionHeight: number
    maxSpeed: number
    smoothing: number
    transitionSpeedFactor: number
    progressBarTrackColor: string
    progressBarFillColor: string
    progressBarOffset: number
    textPaddingLeft: number
    videoPaddingRight: number
    textMaxWidth: number
    mobileLayout: boolean
    mobileTextPaddingTop: number
    mobileTextPaddingX: number
    bottomFadeEnabled: boolean
    bottomFadeHeight: number
    bottomFadeColor: string
    chapterCircleColor: string
    chapterTextColor: string
    chapterFontFamily: string
    chapterBaseFontSize: number
    s1Start: number; s1End: number
    s2Start: number; s2End: number
    s3Start: number; s3End: number
    s4Start: number; s4End: number
    s5Start: number; s5End: number
    s6Start: number; s6End: number
    style?: React.CSSProperties
}

export default function ScrollScrubVideo(props: Props) {
    const {
        videoFile,
        videoUrl,
        language = "nl",
        sectionHeight = 100,
        maxSpeed = 3,
        smoothing = 0.15,
        transitionSpeedFactor = 0.5,
        progressBarTrackColor = "#E0E0E0",
        progressBarFillColor = "#0D164F",
        progressBarOffset = 0,
        textPaddingLeft = 5,
        videoPaddingRight = 10,
        textMaxWidth = 500,
        mobileLayout = false,
        mobileTextPaddingTop = 60,
        mobileTextPaddingX = 5,
        bottomFadeEnabled = false,
        bottomFadeHeight = 25,
        bottomFadeColor = "#FFFFFF",
        chapterCircleColor = "#0D164F",
        chapterTextColor = "#0D164F",
        chapterFontFamily = "'Bricolage Grotesque', sans-serif",
        chapterBaseFontSize = 20,
        s1Start = 0, s1End = 8,
        s2Start = 10, s2End = 17,
        s3Start = 19, s3End = 50,
        s4Start = 55, s4End = 72,
        s5Start = 75, s5End = 85,
        s6Start = 88, s6End = 94,
        style,
    } = props

    const sectionRef = useRef<HTMLDivElement>(null)
    const videoRef = useRef<HTMLVideoElement>(null)
    const chapterTitleRefs = useRef<(HTMLSpanElement | null)[]>([])
    const chapterDescRefs = useRef<(HTMLDivElement | null)[]>([])
    const progressFillRef = useRef<HTMLDivElement>(null)
    const activeSceneRef = useRef(0)
    const lockedRef = useRef(false)
    const wheelAccumRef = useRef(0)
    const wasOutsideRef = useRef(true)
    const lastTouchYRef = useRef(0)
    const videoDurationRef = useRef(94)
    const pinnedScrollYRef = useRef(-1)

    const isMobile = mobileLayout

    const sceneBounds = useMemo(() => [
        { start: s1Start, end: s1End },
        { start: s2Start, end: s2End },
        { start: s3Start, end: s3End },
        { start: s4Start, end: s4End },
        { start: s5Start, end: s5End },
        { start: s6Start, end: s6End },
    ], [s1Start, s1End, s2Start, s2End, s3Start, s3End,
        s4Start, s4End, s5Start, s5End, s6Start, s6End])

    const videoDuration = useMemo(
        () => Math.max(...sceneBounds.map(b => b.end)),
        [sceneBounds]
    )

    useEffect(() => { videoDurationRef.current = videoDuration }, [videoDuration])

    // ── Main rAF loop ───────────────────────────────────────────────────────

    useEffect(() => {
        const video = videoRef.current
        const section = sectionRef.current
        if (!video || !section) return

        let rafId = 0
        let smoothedRate = 1

        function updateUI() {
            const info = getSceneInfo(video.currentTime, sceneBounds)
            // During transitions, highlight the UPCOMING scene (not the one that ended)
            const highlighted = info.inScene
                ? info.sceneIndex
                : Math.min(info.sceneIndex + 1, SCENE_COPY.length - 1)
            activeSceneRef.current = highlighted

            for (let i = 0; i < SCENE_COPY.length; i++) {
                const titleEl = chapterTitleRefs.current[i]
                const descEl = chapterDescRefs.current[i]
                if (!titleEl || !descEl) continue

                const isActive = i === highlighted
                titleEl.style.fontSize = isActive
                    ? `${chapterBaseFontSize * 1.2}px`
                    : `${chapterBaseFontSize}px`
                titleEl.style.fontWeight = isActive ? "600" : "400"
                titleEl.style.opacity = isActive ? "1" : "0.5"
                descEl.style.opacity = isActive ? "0.8" : "0"
                descEl.style.maxHeight = isActive ? "80px" : "0px"
            }

            if (progressFillRef.current) {
                progressFillRef.current.style.width = `${clamp(info.sceneProgress) * 100}%`
            }

            return info
        }

        function doLock() {
            const rect = section.getBoundingClientRect()
            const sectionDocTop = window.scrollY + rect.top
            window.scrollTo(0, sectionDocTop)
            pinnedScrollYRef.current = sectionDocTop
            lockedRef.current = true
            wasOutsideRef.current = false
            smoothedRate = 1
            video.playbackRate = 1
            video.play().catch(() => {})
            // Physically prevent scrolling
            document.documentElement.style.overflow = "hidden"
            document.body.style.overflow = "hidden"
        }

        function tick() {
            if (!video.duration || !isFinite(video.duration)) {
                rafId = requestAnimationFrame(tick)
                return
            }

            const rect = section.getBoundingClientRect()
            const fullyVisible = rect.top <= 5 && rect.bottom >= window.innerHeight - 5

            if (!fullyVisible) wasOutsideRef.current = true

            // Lock when section fills viewport
            if (!lockedRef.current && fullyVisible && wasOutsideRef.current
                && video.currentTime < videoDuration - 0.3) {
                doLock()
            }

            // Safety net: snap back if scroll drifted while locked
            if (lockedRef.current && pinnedScrollYRef.current >= 0
                && Math.abs(window.scrollY - pinnedScrollYRef.current) > 5) {
                window.scrollTo(0, pinnedScrollYRef.current)
            }

            const info = updateUI()

            if (!lockedRef.current) {
                rafId = requestAnimationFrame(tick)
                return
            }

            // Video done → unlock
            if (video.currentTime >= videoDuration - 0.3) {
                lockedRef.current = false
                pinnedScrollYRef.current = -1
                video.pause()
                wheelAccumRef.current = 0
                document.documentElement.style.overflow = ""
                document.body.style.overflow = ""
                rafId = requestAnimationFrame(tick)
                return
            }

            if (video.paused) video.play().catch(() => {})

            // Speed from wheel accumulator
            const boost = clamp(wheelAccumRef.current / 150, 0, 1)
            wheelAccumRef.current *= 0.9

            let desiredRate = 1 + boost * (maxSpeed - 1)
            if (!info.inScene) {
                desiredRate = 1 + (desiredRate - 1) * transitionSpeedFactor
            }

            const alpha = desiredRate > smoothedRate ? smoothing : smoothing * 2.5
            smoothedRate += (desiredRate - smoothedRate) * alpha
            smoothedRate = Math.max(1, smoothedRate)

            if (Math.abs(smoothedRate - video.playbackRate) > 0.08) {
                video.playbackRate = Math.min(smoothedRate, 16)
            }

            rafId = requestAnimationFrame(tick)
        }

        rafId = requestAnimationFrame(tick)
        return () => {
            cancelAnimationFrame(rafId)
            document.documentElement.style.overflow = ""
            document.body.style.overflow = ""
        }
    }, [sceneBounds, videoDuration, maxSpeed, smoothing, transitionSpeedFactor,
        chapterBaseFontSize, isMobile])

    // ── Scroll hijack ───────────────────────────────────────────────────────

    useEffect(() => {
        const video = videoRef.current
        if (!video) return

        function unlock() {
            lockedRef.current = false
            pinnedScrollYRef.current = -1
            video.pause()
            wheelAccumRef.current = 0
            document.documentElement.style.overflow = ""
            document.body.style.overflow = ""
        }

        function tryPreLock(e: { preventDefault: () => void }) {
            const section = sectionRef.current
            if (!section || !video.duration) return false
            if (video.currentTime >= videoDurationRef.current - 0.3) return false
            if (!wasOutsideRef.current) return false

            const rect = section.getBoundingClientRect()
            // Section approaching viewport top: prevent scroll
            if (rect.top <= 300 && rect.bottom > 0) {
                e.preventDefault()
                // Close enough to snap and lock immediately
                if (rect.top <= 50 && rect.top > -window.innerHeight) {
                    const sectionDocTop = window.scrollY + rect.top
                    window.scrollTo(0, sectionDocTop)
                    pinnedScrollYRef.current = sectionDocTop
                    lockedRef.current = true
                    wasOutsideRef.current = false
                    video.playbackRate = 1
                    video.play().catch(() => {})
                    document.documentElement.style.overflow = "hidden"
                    document.body.style.overflow = "hidden"
                }
                return true
            }
            return false
        }

        function onWheel(e: WheelEvent) {
            if (e.deltaY > 0) {
                if (lockedRef.current) {
                    e.preventDefault()
                    wheelAccumRef.current += e.deltaY
                } else {
                    tryPreLock(e)
                }
            } else if (e.deltaY < -20 && lockedRef.current) {
                unlock()
            }
        }

        function onTouchStart(e: TouchEvent) {
            if (e.touches.length > 0) {
                lastTouchYRef.current = e.touches[0].clientY
            }
        }

        function onTouchMove(e: TouchEvent) {
            const delta = e.touches.length > 0
                ? lastTouchYRef.current - e.touches[0].clientY
                : 0
            if (e.touches.length > 0) lastTouchYRef.current = e.touches[0].clientY

            if (delta > 2) {
                if (lockedRef.current) {
                    e.preventDefault()
                    wheelAccumRef.current += delta * 3
                } else {
                    tryPreLock(e)
                }
            } else if (delta < -15 && lockedRef.current) {
                unlock()
            }
        }

        function onKeyDown(e: KeyboardEvent) {
            if (!lockedRef.current) return
            if (e.key === " " || e.key === "PageDown" || e.key === "ArrowDown") {
                e.preventDefault()
                wheelAccumRef.current += 200
            } else if (e.key === "PageUp" || e.key === "ArrowUp") {
                unlock()
            }
        }

        window.addEventListener("wheel", onWheel, { passive: false, capture: true })
        window.addEventListener("touchstart", onTouchStart, { passive: true })
        window.addEventListener("touchmove", onTouchMove, { passive: false })
        window.addEventListener("keydown", onKeyDown, { capture: true })

        return () => {
            window.removeEventListener("wheel", onWheel, { capture: true } as EventListenerOptions)
            window.removeEventListener("touchstart", onTouchStart)
            window.removeEventListener("touchmove", onTouchMove)
            window.removeEventListener("keydown", onKeyDown, { capture: true } as EventListenerOptions)
        }
    }, [])

    // ── Navigation callbacks ────────────────────────────────────────────────

    const seekAndPlay = useCallback((time: number) => {
        const video = videoRef.current
        if (!video) return
        video.currentTime = time
        if (lockedRef.current) video.play().catch(() => {})
    }, [])

    const goToChapter = useCallback((i: number) => {
        seekAndPlay(i === 0 ? 0 : sceneBounds[i - 1].end)
    }, [sceneBounds, seekAndPlay])

    const exitSection = useCallback(() => {
        const video = videoRef.current
        const section = sectionRef.current
        if (!video || !section) return
        video.currentTime = videoDuration
        video.pause()
        lockedRef.current = false
        pinnedScrollYRef.current = -1
        wasOutsideRef.current = false
        wheelAccumRef.current = 0
        document.documentElement.style.overflow = ""
        document.body.style.overflow = ""
        // Find the next sibling section in the DOM and scroll to it
        const next = section.nextElementSibling
        if (next) {
            requestAnimationFrame(() => {
                next.scrollIntoView({ behavior: "smooth" })
            })
        }
    }, [videoDuration])

    // ── Render ───────────────────────────────────────────────────────────────

    const circleSize = Math.round(chapterBaseFontSize * 1.6)

    return (
        <div
            ref={sectionRef}
            style={{
                ...style,
                height: `${sectionHeight}vh`,
                position: "relative",
                width: "100%",
            }}
        >
            <div
                style={{
                    position: "sticky",
                    top: 0,
                    height: "100vh",
                    width: "100%",
                    display: "flex",
                    ...(isMobile
                        ? {
                              flexDirection: "column" as const,
                              alignItems: "center",
                              justifyContent: "flex-start",
                          }
                        : {
                              alignItems: "center",
                              justifyContent: "flex-end",
                              paddingRight: `${videoPaddingRight}%`,
                          }),
                    overflow: "hidden",
                }}
            >
                {/* Chapter list */}
                <div
                    style={{
                        position: "absolute",
                        ...(isMobile
                            ? {
                                  top: mobileTextPaddingTop,
                                  left: `${mobileTextPaddingX}%`,
                                  right: `${mobileTextPaddingX}%`,
                              }
                            : {
                                  left: `${textPaddingLeft}%`,
                                  top: "50%",
                                  transform: "translateY(-50%)",
                                  maxWidth: textMaxWidth,
                              }),
                        display: "flex",
                        flexDirection: "column" as const,
                        gap: 6,
                        zIndex: 2,
                    }}
                >
                    {SCENE_COPY.map((scene, i) => {
                        const headline = language === "nl" ? scene.headlineNl : scene.headlineEn
                        const description = language === "nl" ? scene.descriptionNl : scene.descriptionEn
                        return (
                            <div key={i}>
                                {/* Circle + Title — only this row is clickable */}
                                <div
                                    onClick={() => goToChapter(i)}
                                    style={{
                                        display: "flex",
                                        alignItems: "center",
                                        gap: 12,
                                        cursor: "pointer",
                                        padding: "6px 0",
                                    }}
                                >
                                    <div style={{
                                        width: circleSize,
                                        height: circleSize,
                                        minWidth: circleSize,
                                        borderRadius: "50%",
                                        backgroundColor: chapterCircleColor,
                                        display: "flex",
                                        alignItems: "center",
                                        justifyContent: "center",
                                        color: "#FFFFFF",
                                        fontFamily: chapterFontFamily,
                                        fontWeight: 600,
                                        fontSize: Math.round(circleSize * 0.5),
                                        lineHeight: 1,
                                    }}>
                                        {i + 1}
                                    </div>
                                    <span
                                        ref={(el) => { chapterTitleRefs.current[i] = el }}
                                        style={{
                                            fontFamily: chapterFontFamily,
                                            fontSize: chapterBaseFontSize,
                                            fontWeight: 400,
                                            color: chapterTextColor,
                                            opacity: 0.5,
                                            lineHeight: 1.3,
                                            transition: "font-size 300ms ease, opacity 300ms ease, font-weight 300ms ease",
                                        }}
                                    >
                                        {headline}
                                    </span>
                                </div>
                                {/* Description — in flow, expands via max-height */}
                                <div
                                    ref={(el) => { chapterDescRefs.current[i] = el }}
                                    style={{
                                        maxHeight: 0,
                                        overflow: "hidden",
                                        opacity: 0,
                                        paddingLeft: circleSize + 12,
                                        transition: "max-height 300ms ease, opacity 300ms ease",
                                    }}
                                >
                                    <p style={{
                                        fontFamily: "'Inter', sans-serif",
                                        fontSize: Math.round(chapterBaseFontSize * 0.8),
                                        fontWeight: 400,
                                        color: chapterTextColor,
                                        lineHeight: 1.45,
                                        margin: "2px 0 8px 0",
                                        opacity: 0.7,
                                    }}>
                                        {description}
                                    </p>
                                </div>
                            </div>
                        )
                    })}
                </div>

                {/* Video + progress bar */}
                <div style={{
                    position: "relative",
                    display: "flex",
                    flexDirection: "column" as const,
                    alignItems: "center",
                    ...(isMobile && { marginTop: "auto", marginBottom: "auto" }),
                }}>
                    <video
                        ref={videoRef}
                        src={videoFile || videoUrl}
                        muted
                        playsInline
                        preload="auto"
                        style={{
                            height: isMobile ? "65vh" : "80vh",
                            width: "auto",
                            objectFit: "contain",
                            pointerEvents: "none",
                        }}
                    />

                    {bottomFadeEnabled && (
                        <div
                            style={{
                                position: "absolute",
                                bottom: 0,
                                left: 0,
                                right: 0,
                                height: `${bottomFadeHeight}%`,
                                background: `linear-gradient(to bottom, transparent 0%, ${bottomFadeColor} 100%)`,
                                pointerEvents: "none",
                            }}
                        />
                    )}

                    <div
                        style={{
                            position: "absolute",
                            bottom: -progressBarOffset,
                            left: "15%",
                            right: "15%",
                            height: 2,
                            borderRadius: 1,
                            backgroundColor: progressBarTrackColor,
                            overflow: "hidden",
                            zIndex: 3,
                        }}
                    >
                        <div
                            ref={progressFillRef}
                            style={{
                                position: "absolute",
                                top: 0,
                                left: 0,
                                height: "100%",
                                width: "0%",
                                backgroundColor: progressBarFillColor,
                                borderRadius: 1,
                            }}
                        />
                    </div>
                </div>

                {/* Skip to next section */}
                <button
                    onClick={exitSection}
                    style={{
                        position: "absolute",
                        bottom: 32,
                        left: "50%",
                        transform: "translateX(-50%)",
                        background: "none",
                        border: "none",
                        cursor: "pointer",
                        padding: 12,
                        opacity: 0.3,
                        transition: "opacity 200ms ease",
                        zIndex: 3,
                    }}
                    onMouseEnter={(e) => { e.currentTarget.style.opacity = "0.6" }}
                    onMouseLeave={(e) => { e.currentTarget.style.opacity = "0.3" }}
                >
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                        stroke="#0D164F" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <polyline points="6 9 12 15 18 9" />
                    </svg>
                </button>
            </div>
        </div>
    )
}

// ─── Framer property controls ────────────────────────────────────────────────

addPropertyControls(ScrollScrubVideo, {
    videoFile: {
        type: ControlType.File,
        title: "Video File",
        allowedFileTypes: ["webm", "mp4"],
    },
    videoUrl: {
        type: ControlType.String,
        title: "Video URL",
        defaultValue: "",
        description: "File upload takes priority if both are set.",
    },
    language: {
        type: ControlType.Enum,
        title: "Language",
        options: ["nl", "en"],
        optionTitles: ["Nederlands", "English"],
        defaultValue: "nl",
    },
    maxSpeed: {
        type: ControlType.Number,
        title: "Max Speed",
        defaultValue: 3,
        min: 1, max: 10, step: 0.5,
        description: "Max playback rate when scrolling fast.",
    },
    smoothing: {
        type: ControlType.Number,
        title: "Smoothing",
        defaultValue: 0.15,
        min: 0.03, max: 0.5, step: 0.01,
        description: "Speed change responsiveness. Lower = more gradual.",
    },
    transitionSpeedFactor: {
        type: ControlType.Number,
        title: "Flip Speed Factor",
        defaultValue: 0.5,
        min: 0.1, max: 1, step: 0.05,
        description: "Speed multiplier during phone flips.",
    },
    mobileLayout: {
        type: ControlType.Boolean,
        title: "Mobile Layout",
        defaultValue: false,
    },
    sectionHeight: {
        type: ControlType.Number,
        title: "Section Height (vh)",
        defaultValue: 100,
        min: 100, max: 300, step: 10,
    },
    textPaddingLeft: {
        type: ControlType.Number,
        title: "Chapter Left Padding (%)",
        defaultValue: 5,
        min: 0, max: 30, step: 1,
    },
    videoPaddingRight: {
        type: ControlType.Number,
        title: "Video Right Padding (%)",
        defaultValue: 10,
        min: 0, max: 30, step: 1,
    },
    textMaxWidth: {
        type: ControlType.Number,
        title: "Chapter Max Width (px)",
        defaultValue: 500,
        min: 200, max: 800, step: 10,
    },
    mobileTextPaddingTop: {
        type: ControlType.Number,
        title: "Mobile Chapter Top (px)",
        defaultValue: 60,
        min: 0, max: 200, step: 5,
        hidden: (props: any) => !props.mobileLayout,
    },
    mobileTextPaddingX: {
        type: ControlType.Number,
        title: "Mobile Chapter Side Padding (%)",
        defaultValue: 5,
        min: 0, max: 20, step: 1,
        hidden: (props: any) => !props.mobileLayout,
    },
    chapterCircleColor: {
        type: ControlType.Color,
        title: "Circle Color",
        defaultValue: "#0D164F",
    },
    chapterTextColor: {
        type: ControlType.Color,
        title: "Chapter Text Color",
        defaultValue: "#0D164F",
    },
    chapterFontFamily: {
        type: ControlType.String,
        title: "Chapter Font",
        defaultValue: "'Bricolage Grotesque', sans-serif",
    },
    chapterBaseFontSize: {
        type: ControlType.Number,
        title: "Chapter Font Size (px)",
        defaultValue: 20,
        min: 10, max: 40, step: 1,
        description: "Base size. Active chapter gets 20% larger.",
    },
    bottomFadeEnabled: {
        type: ControlType.Boolean,
        title: "Bottom Fade",
        defaultValue: false,
    },
    bottomFadeHeight: {
        type: ControlType.Number,
        title: "Fade Height (%)",
        defaultValue: 25,
        min: 5, max: 60, step: 5,
        hidden: (props: any) => !props.bottomFadeEnabled,
    },
    bottomFadeColor: {
        type: ControlType.Color,
        title: "Fade Color",
        defaultValue: "#FFFFFF",
        hidden: (props: any) => !props.bottomFadeEnabled,
    },
    progressBarTrackColor: {
        type: ControlType.Color,
        title: "Progress Track Color",
        defaultValue: "#E0E0E0",
    },
    progressBarFillColor: {
        type: ControlType.Color,
        title: "Progress Fill Color",
        defaultValue: "#0D164F",
    },
    progressBarOffset: {
        type: ControlType.Number,
        title: "Progress Bar Offset (px)",
        defaultValue: 0,
        min: -100, max: 100, step: 2,
    },
    s1Start: { type: ControlType.Number, title: "Scene 1 Start (s)", defaultValue: 0, min: 0, max: 300, step: 0.1 },
    s1End: { type: ControlType.Number, title: "Scene 1 End (s)", defaultValue: 8, min: 0, max: 300, step: 0.1 },
    s2Start: { type: ControlType.Number, title: "Scene 2 Start (s)", defaultValue: 10, min: 0, max: 300, step: 0.1 },
    s2End: { type: ControlType.Number, title: "Scene 2 End (s)", defaultValue: 17, min: 0, max: 300, step: 0.1 },
    s3Start: { type: ControlType.Number, title: "Scene 3 Start (s)", defaultValue: 19, min: 0, max: 300, step: 0.1 },
    s3End: { type: ControlType.Number, title: "Scene 3 End (s)", defaultValue: 50, min: 0, max: 300, step: 0.1 },
    s4Start: { type: ControlType.Number, title: "Scene 4 Start (s)", defaultValue: 55, min: 0, max: 300, step: 0.1 },
    s4End: { type: ControlType.Number, title: "Scene 4 End (s)", defaultValue: 72, min: 0, max: 300, step: 0.1 },
    s5Start: { type: ControlType.Number, title: "Scene 5 Start (s)", defaultValue: 75, min: 0, max: 300, step: 0.1 },
    s5End: { type: ControlType.Number, title: "Scene 5 End (s)", defaultValue: 85, min: 0, max: 300, step: 0.1 },
    s6Start: { type: ControlType.Number, title: "Scene 6 Start (s)", defaultValue: 88, min: 0, max: 300, step: 0.1 },
    s6End: { type: ControlType.Number, title: "Scene 6 End (s)", defaultValue: 94, min: 0, max: 300, step: 0.1 },
})
