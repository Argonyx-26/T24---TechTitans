import React, { useState } from "react";
import "./App.css";

const scenarios = [
  {
    score: 42,
    level: "MEDIUM",
    priority: "MEDIUM",
    response: "Within 30 minutes",
    correlations: 2,
    signals: [
      "Unusual access attempt detected",
      "Low-volume network anomaly",
      "Behavioral deviation identified",
    ],
    physical: 38,
    access: 51,
    network: 43,
    behavior: 46,
  },
  {
    score: 58,
    level: "MEDIUM",
    priority: "HIGH",
    response: "Within 15 minutes",
    correlations: 3,
    signals: [
      "After-hours access detected",
      "Suspicious network connection",
      "Unusual user behavior",
      "Repeated authentication attempt",
    ],
    physical: 54,
    access: 71,
    network: 63,
    behavior: 58,
  },
  {
    score: 67,
    level: "HIGH",
    priority: "HIGH",
    response: "Within 10 minutes",
    correlations: 3,
    signals: [
      "Restricted-area entry detected",
      "After-hours access detected",
      "Suspicious network connection",
      "High network data transfer detected",
    ],
    physical: 76,
    access: 82,
    network: 68,
    behavior: 61,
  },
  {
    score: 74,
    level: "HIGH",
    priority: "HIGH",
    response: "Within 5 minutes",
    correlations: 4,
    signals: [
      "Restricted-area entry detected",
      "Unauthorized access detected",
      "Suspicious network connection",
      "High network data transfer detected",
      "Multiple correlated anomalies",
    ],
    physical: 81,
    access: 86,
    network: 73,
    behavior: 78,
  },
  {
    score: 86,
    level: "CRITICAL",
    priority: "CRITICAL",
    response: "Immediate",
    correlations: 4,
    signals: [
      "Restricted-area entry detected",
      "After-hours access detected",
      "Suspicious network connection",
      "High network data transfer detected",
      "Behavioral anomaly detected",
      "Cross-source correlation confirmed",
    ],
    physical: 91,
    access: 88,
    network: 84,
    behavior: 86,
  },
  {
    score: 94,
    level: "CRITICAL",
    priority: "CRITICAL",
    response: "Immediate",
    correlations: 5,
    signals: [
      "Unauthorized physical access",
      "After-hours access detected",
      "Suspicious network connection",
      "Abnormal data transfer",
      "Repeated behavioral anomaly",
      "Multiple source correlation",
      "Potential coordinated incident",
    ],
    physical: 95,
    access: 92,
    network: 89,
    behavior: 94,
  },
];

const navItems = [
  "Alert Prioritization",
  "Why This Alert?",
  "Incident Timeline",
  "Incident Summary",
  "Live Event Feed",
  "Security Overview",
  "Incident History",
  "Location Awareness",
  "Behavioral Anomaly",
  "Final Demo",
];

function getRiskClass(score) {
  if (score >= 85) return "critical";
  if (score >= 70) return "high";
  if (score >= 40) return "medium";
  return "low";
}

function getRiskLabel(score) {
  if (score >= 85) return "CRITICAL";
  if (score >= 70) return "HIGH";
  if (score >= 40) return "MEDIUM";
  return "LOW";
}

function App() {
  const [activeStep, setActiveStep] = useState(0);
  const [scenarioIndex, setScenarioIndex] = useState(2);

  const data = scenarios[scenarioIndex];

  const refreshAnalysis = () => {
    setScenarioIndex((current) => (current + 1) % scenarios.length);
  };

  const scrollToSection = (index) => {
    setActiveStep(index);

    const element = document.getElementById(`step-${index + 1}`);

    if (element) {
      element.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  };

  return (
    <div className="app-shell">

      {/* ================= SIDEBAR ================= */}

      <aside className="sidebar">

        <div className="brand">
          <div className="brand-mark">A</div>

          <div>
            <div className="brand-name">ARGUS AI</div>
            <div className="brand-subtitle">SECURITY INTELLIGENCE</div>
          </div>
        </div>

        <div className="backend-status">
          <span className="status-dot"></span>
          <span>BACKEND ONLINE</span>
        </div>

        <div className="sidebar-heading">
          SECURITY OPERATIONS
        </div>

        <nav className="navigation">

          {navItems.map((item, index) => (
            <button
              key={item}
              className={`nav-item ${
                activeStep === index ? "active" : ""
              }`}
              onClick={() => scrollToSection(index)}
            >
              <span className="nav-number">
                {String(index + 1).padStart(2, "0")}
              </span>

              <span className="nav-icon">
                {["△", "⌕", "◷", "▤", "⊙", "◇", "□", "⌖", "⬡", "▶"][index]}
              </span>

              <span>{item}</span>
            </button>
          ))}

        </nav>

        <div className="sidebar-footer">
          <div>SYSTEM</div>
          <strong>ARGUS AI v1.0</strong>

          <div className="sync-label">LAST SYNCHRONIZATION</div>
          <strong>03:59:28</strong>
        </div>

      </aside>

      {/* ================= MAIN ================= */}

      <main className="main-content">

        {/* TOP HEADER */}

        <header className="top-header">

          <div>
            <div className="top-title">
              AUTONOMOUS SECURITY OPERATIONS CENTER
            </div>

            <div className="top-subtitle">
              Unified Threat Intelligence & Incident Correlation
            </div>
          </div>

          <div className="system-online">
            <span className="online-dot"></span>
            SYSTEM ONLINE
          </div>

        </header>

        {/* =========================================================
            STEP 1
        ========================================================== */}

        <section id="step-1" className="page-section">

          <div className="section-eyebrow">
            01 / ALERT PRIORITIZATION
          </div>

          <div className="section-heading-row">

            <div>
              <h1>Alert Prioritization</h1>

              <p>
                Automated assessment and prioritization of security
                incidents using fused intelligence.
              </p>
            </div>

            <button
              className="refresh-button"
              onClick={refreshAnalysis}
            >
              ↻ REFRESH ANALYSIS
            </button>

          </div>

          {/* MAIN SCORE */}

          <div className="main-risk-card">

            <div className="risk-card-header">

              <div>
                <div className="mini-label">
                  ARGUS AI / RISK ENGINE
                </div>

                <h2>Security Risk Profile</h2>

                <p>
                  Current assessment across independent security
                  dimensions.
                </p>
              </div>

              <div className="live-badge">
                <span></span>
                LIVE ANALYSIS
              </div>

            </div>

            <div className="risk-overview">

              <div className="overall-score">

                <div className="mini-label">
                  OVERALL RISK SCORE
                </div>

                <div
                  className={`large-score ${getRiskClass(data.score)}`}
                >
                  {data.score}
                  <span>/100</span>
                </div>

                <div
                  className={`risk-badge ${getRiskClass(data.score)}`}
                >
                  {data.level}
                </div>

                <div className="progress-track">
                  <div
                    className={`progress-value ${getRiskClass(
                      data.score
                    )}`}
                    style={{ width: `${data.score}%` }}
                  />
                </div>

              </div>

              <div className="priority-box">

                <div className="mini-label">
                  ALERT PRIORITY
                </div>

                <strong
                  className={`priority-text ${getRiskClass(
                    data.score
                  )}`}
                >
                  {data.priority}
                </strong>

                <span>REQUIRED RESPONSE</span>

                <strong>{data.response}</strong>

              </div>

              <div className="correlation-box">

                <div className="mini-label">
                  CROSS-SOURCE CORRELATION
                </div>

                <div className="correlation-number">
                  {data.correlations}
                </div>

                <span>
                  correlation patterns identified
                </span>

              </div>

            </div>

          </div>

          {/* SOURCE CARDS */}

          <div className="subsection-header">

            <div>
              <div className="mini-label">
                FUSED INTELLIGENCE
              </div>

              <h2>Source Risk Assessment</h2>

              <p>
                Risk contribution from independent security sources.
              </p>
            </div>

            <div className="source-count">
              04 SOURCES
            </div>

          </div>

          <div className="risk-grid">

            <RiskCard
              title="CCTV ANALYSIS"
              subtitle="Physical Risk"
              score={data.physical}
              icon="◉"
              description="Physical security activity"
            />

            <RiskCard
              title="ACCESS CONTROL"
              subtitle="Access Risk"
              score={data.access}
              icon="⌁"
              description="Authentication and access activity"
            />

            <RiskCard
              title="NETWORK ANALYSIS"
              subtitle="Network Risk"
              score={data.network}
              icon="⌘"
              description="Network traffic intelligence"
            />

            <RiskCard
              title="BEHAVIOR ANALYSIS"
              subtitle="Behavioral Risk"
              score={data.behavior}
              icon="◇"
              description="User and system behavior"
            />

          </div>

          <div className="two-column">

            <InfoCard
              title="Why ARGUS AI raised this alert"
              eyebrow="PRIORITIZATION REASON"
            >
              <div className="reason-content">

                <div className="warning-icon">!</div>

                <div>
                  <strong>
                    Multiple security sources indicate correlated
                    suspicious activity.
                  </strong>

                  <p>
                    ARGUS AI evaluates physical, access, network
                    and behavioral signals together to identify
                    incidents that may not be visible from a single
                    source.
                  </p>
                </div>

              </div>
            </InfoCard>

            <InfoCard
              title="Detected Security Signals"
              eyebrow="THREAT DETECTION"
            >

              <div className="signal-list">

                {data.signals.map((signal, index) => (
                  <div className="signal-row" key={signal}>

                    <span className="signal-index">
                      {String(index + 1).padStart(2, "0")}
                    </span>

                    <span>{signal}</span>

                    <span className="detected">
                      DETECTED
                    </span>

                  </div>
                ))}

              </div>

            </InfoCard>

          </div>

        </section>

        {/* =========================================================
            STEP 2
        ========================================================== */}

        <section id="step-2" className="page-section">

          <SectionTitle
            number="02"
            title="Why This Alert?"
            description="Explainable security intelligence behind the current alert."
          />

          <div className="explanation-grid">

            <div className="explanation-card">

              <div className="explanation-number">
                {data.score}
              </div>

              <div>
                <div className="mini-label">
                  CURRENT THREAT SCORE
                </div>

                <h3>
                  {getRiskLabel(data.score)} security condition
                </h3>

                <p>
                  The current score is generated from multiple
                  independent security observations and their
                  cross-source correlation.
                </p>
              </div>

            </div>

            <div className="explanation-card">

              <div className="explanation-number">
                {data.correlations}
              </div>

              <div>
                <div className="mini-label">
                  CORRELATION ENGINE
                </div>

                <h3>
                  Cross-source patterns detected
                </h3>

                <p>
                  ARGUS AI connects related CCTV, access-control,
                  network and behavioral events into a unified
                  incident view.
                </p>
              </div>

            </div>

          </div>

        </section>

        {/* =========================================================
            STEP 3
        ========================================================== */}

        <section id="step-3" className="page-section">

          <SectionTitle
            number="03"
            title="Incident Timeline"
            description="Chronological view of events contributing to the incident."
          />

          <div className="timeline">

            <TimelineItem
              time="21:42:08"
              source="CCTV"
              title="Restricted-area activity detected"
              description="Movement detected in a monitored restricted zone."
            />

            <TimelineItem
              time="21:44:17"
              source="ACCESS"
              title="After-hours access recorded"
              description="Access-control system registered an unusual entry."
            />

            <TimelineItem
              time="21:46:32"
              source="NETWORK"
              title="Suspicious connection identified"
              description="Network monitoring detected abnormal communication."
            />

            <TimelineItem
              time="21:48:05"
              source="ARGUS AI"
              title="Cross-source correlation completed"
              description="Related security signals were correlated into one incident."
              highlight
            />

          </div>

        </section>

        {/* =========================================================
            STEP 4
        ========================================================== */}

        <section id="step-4" className="page-section">

          <SectionTitle
            number="04"
            title="Incident Summary"
            description="Consolidated view of the detected security incident."
          />

          <div className="summary-grid">

            <SummaryCard
              label="THREAT SCORE"
              value={`${data.score}/100`}
              status={data.level}
            />

            <SummaryCard
              label="CORRELATION"
              value={data.correlations}
              status="PATTERNS"
            />

            <SummaryCard
              label="SIGNALS"
              value={data.signals.length}
              status="DETECTED"
            />

            <SummaryCard
              label="RESPONSE"
              value={data.response}
              status="REQUIRED"
            />

          </div>

          <div className="summary-panel">

            <div className="mini-label">
              INCIDENT ASSESSMENT
            </div>

            <h3>
              Correlated security activity requires investigation.
            </h3>

            <p>
              ARGUS AI has combined multiple independent signals
              into a consolidated incident assessment. Security
              personnel can use the correlated evidence to begin
              investigation and verification.
            </p>

          </div>

        </section>

        {/* =========================================================
            STEP 5
        ========================================================== */}

        <section id="step-5" className="page-section">

          <SectionTitle
            number="05"
            title="Live Event Feed"
            description="Current security events received by the intelligence layer."
          />

          <div className="event-table">

            <div className="event-header">
              <span>TIME</span>
              <span>SOURCE</span>
              <span>EVENT</span>
              <span>STATUS</span>
            </div>

            <EventRow
              time="21:42:08"
              source="CCTV"
              event="Restricted-area entry"
            />

            <EventRow
              time="21:44:17"
              source="ACCESS_LOG"
              event="After-hours access"
            />

            <EventRow
              time="21:46:32"
              source="NETWORK"
              event="Suspicious connection"
            />

            <EventRow
              time="21:48:05"
              source="BEHAVIOR"
              event="Abnormal activity pattern"
            />

          </div>

        </section>

        {/* =========================================================
            STEP 6
        ========================================================== */}

        <section id="step-6" className="page-section">

          <SectionTitle
            number="06"
            title="Security Overview"
            description="High-level operational status across security dimensions."
          />

          <div className="overview-grid">

            <OverviewMetric
              label="PHYSICAL SECURITY"
              value={data.physical}
            />

            <OverviewMetric
              label="ACCESS CONTROL"
              value={data.access}
            />

            <OverviewMetric
              label="NETWORK SECURITY"
              value={data.network}
            />

            <OverviewMetric
              label="BEHAVIORAL ANALYSIS"
              value={data.behavior}
            />

          </div>

        </section>

        {/* =========================================================
            STEP 7
        ========================================================== */}

        <section id="step-7" className="page-section">

          <SectionTitle
            number="07"
            title="Incident History"
            description="Recent incidents recorded by the ARGUS AI platform."
          />

          <div className="history-list">

            <HistoryRow
              id="INC-2026-091"
              date="26 SEP 2026"
              type="Access anomaly"
              severity="HIGH"
            />

            <HistoryRow
              id="INC-2026-090"
              date="25 SEP 2026"
              type="Network anomaly"
              severity="MEDIUM"
            />

            <HistoryRow
              id="INC-2026-089"
              date="24 SEP 2026"
              type="Physical security event"
              severity="HIGH"
            />

            <HistoryRow
              id="INC-2026-088"
              date="23 SEP 2026"
              type="Behavioral anomaly"
              severity="MEDIUM"
            />

          </div>

        </section>

        {/* =========================================================
            STEP 8
        ========================================================== */}

        <section id="step-8" className="page-section">

          <SectionTitle
            number="08"
            title="Location Awareness"
            description="Security activity mapped to monitored facility zones."
          />

          <div className="location-layout">

            <div className="facility-map">

              <div className="map-label">SECURITY ZONE MAP</div>

              <div className="map-zone zone-a">
                A
                <span>MAIN ENTRY</span>
              </div>

              <div className="map-zone zone-b active-zone">
                B
                <span>SERVER ROOM</span>
              </div>

              <div className="map-zone zone-c">
                C
                <span>CONTROL ROOM</span>
              </div>

              <div className="map-zone zone-d">
                D
                <span>RESTRICTED AREA</span>
              </div>

            </div>

            <div className="location-panel">

              <div className="mini-label">
                CURRENT ACTIVITY
              </div>

              <h3>SERVER ROOM / ZONE B</h3>

              <p>
                Elevated security activity detected in the
                monitored zone.
              </p>

              <div className="location-stat">
                <span>ACTIVITY LEVEL</span>
                <strong>{data.level}</strong>
              </div>

              <div className="location-stat">
                <span>MONITORED SOURCES</span>
                <strong>04</strong>
              </div>

            </div>

          </div>

        </section>

        {/* =========================================================
            STEP 9
        ========================================================== */}

        <section id="step-9" className="page-section">

          <SectionTitle
            number="09"
            title="Behavioral Anomaly Detection"
            description="Analysis of deviations from expected user and system behavior."
          />

          <div className="behavior-grid">

            <div className="behavior-card">

              <div className="mini-label">
                BEHAVIORAL RISK
              </div>

              <div className="behavior-score">
                {data.behavior}
                <span>/100</span>
              </div>

              <div
                className={`risk-badge ${getRiskClass(
                  data.behavior
                )}`}
              >
                {getRiskLabel(data.behavior)}
              </div>

            </div>

            <div className="behavior-details">

              <BehaviorRow
                label="Access frequency deviation"
                value="Elevated"
              />

              <BehaviorRow
                label="Login time deviation"
                value="Detected"
              />

              <BehaviorRow
                label="Network usage deviation"
                value="Detected"
              />

              <BehaviorRow
                label="Cross-source consistency"
                value="Confirmed"
              />

            </div>

          </div>

        </section>

        {/* =========================================================
            STEP 10
        ========================================================== */}

        <section id="step-10" className="page-section final-section">

          <SectionTitle
            number="10"
            title="Final Demo Test"
            description="Unified demonstration of ARGUS AI threat intelligence."
          />

          <div className="final-demo">

            <div className="demo-status">
              <span className="large-status-dot"></span>

              <div>
                <div className="mini-label">
                  SYSTEM STATUS
                </div>

                <h2>ARGUS AI OPERATIONAL</h2>

                <p>
                  All intelligence modules are available for
                  demonstration.
                </p>
              </div>
            </div>

            <div className="final-score">

              <div className="mini-label">
                CURRENT THREAT SCORE
              </div>

              <strong className={getRiskClass(data.score)}>
                {data.score}
              </strong>

              <span>/100</span>

            </div>

            <button
              className="final-refresh"
              onClick={refreshAnalysis}
            >
              RUN NEW DEMO SCENARIO
            </button>

          </div>

        </section>

        <footer className="main-footer">
          ARGUS AI • AUTONOMOUS SECURITY OPERATIONS CENTER
          <span>DEMO ENVIRONMENT</span>
        </footer>

      </main>

    </div>
  );
}


/* =========================================================
   COMPONENTS
========================================================= */

function RiskCard({
  title,
  subtitle,
  score,
  icon,
  description,
}) {
  const riskClass = getRiskClass(score);

  return (
    <div className={`risk-source-card ${riskClass}`}>

      <div className="risk-source-top">

        <div className="source-icon">
          {icon}
        </div>

        <div>
          <div className="source-title">
            {title}
          </div>

          <div className="source-subtitle">
            {subtitle}
          </div>
        </div>

      </div>

      <div className="source-score">
        <strong>{score}</strong>
        <span>/100</span>
      </div>

      <div className="source-level">
        {getRiskLabel(score)}
      </div>

      <div className="source-progress">
        <div
          className={`source-progress-fill ${riskClass}`}
          style={{ width: `${score}%` }}
        />
      </div>

      <p>{description}</p>

    </div>
  );
}


function SectionTitle({ number, title, description }) {
  return (
    <div className="section-title">

      <div className="section-eyebrow">
        {number} / SECURITY OPERATIONS
      </div>

      <h2>{title}</h2>

      <p>{description}</p>

    </div>
  );
}


function InfoCard({ eyebrow, title, children }) {
  return (
    <div className="info-card">

      <div className="mini-label">
        {eyebrow}
      </div>

      <h3>{title}</h3>

      {children}

    </div>
  );
}


function TimelineItem({
  time,
  source,
  title,
  description,
  highlight,
}) {
  return (
    <div className={`timeline-item ${highlight ? "highlight" : ""}`}>

      <div className="timeline-time">
        {time}
      </div>

      <div className="timeline-line">
        <span></span>
      </div>

      <div className="timeline-content">

        <div className="timeline-source">
          {source}
        </div>

        <h3>{title}</h3>

        <p>{description}</p>

      </div>

    </div>
  );
}


function SummaryCard({ label, value, status }) {
  return (
    <div className="summary-card">

      <div className="mini-label">
        {label}
      </div>

      <strong>{value}</strong>

      <span>{status}</span>

    </div>
  );
}


function EventRow({ time, source, event }) {
  return (
    <div className="event-row">

      <span>{time}</span>

      <strong>{source}</strong>

      <span>{event}</span>

      <span className="event-status">
        RECEIVED
      </span>

    </div>
  );
}


function OverviewMetric({ label, value }) {
  const riskClass = getRiskClass(value);

  return (
    <div className="overview-card">

      <div className="mini-label">
        {label}
      </div>

      <div className="overview-score">
        {value}
        <span>/100</span>
      </div>

      <div className="progress-track">
        <div
          className={`progress-value ${riskClass}`}
          style={{ width: `${value}%` }}
        />
      </div>

      <div className={`overview-level ${riskClass}`}>
        {getRiskLabel(value)}
      </div>

    </div>
  );
}


function HistoryRow({
  id,
  date,
  type,
  severity,
}) {
  return (
    <div className="history-row">

      <strong>{id}</strong>

      <span>{date}</span>

      <span>{type}</span>

      <span
        className={`history-severity ${getRiskClass(
          severity === "HIGH" ? 75 : 50
        )}`}
      >
        {severity}
      </span>

    </div>
  );
}


function BehaviorRow({ label, value }) {
  return (
    <div className="behavior-row">

      <span>{label}</span>

      <strong>{value}</strong>

    </div>
  );
}

export default App;
